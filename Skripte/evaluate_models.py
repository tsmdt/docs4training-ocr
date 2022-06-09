import imghdr
import itertools
import os
import time
from collections import defaultdict
from pathlib import Path
from subprocess import run, check_output, CalledProcessError, DEVNULL

import click
from tqdm import tqdm


def multiprocessing_process(jobs, process_id):
    """ Cli process to start a multiprocessing job with sem (GNU parallel) """
    return f"sem -j {jobs} --id {process_id} "


def ocr_process(model, filepath, textfile):
    """ Cli process to ocr a file with a given model/language """
    return f"tesseract -l {model} {str(filepath.resolve())} {str(textfile.with_suffix('').resolve())}; "


def normalization_process(normalize, delete_empty_lines):
    """ Cli process normalize glyphs in the ocr result """
    normalize = itertools.chain.from_iterable(
        [[n.replace('"', '\"')] if not n.startswith('@') else Path(n[1:]).read_text().replace('"', '\"').strip().split(
            '\n') if Path(n[1:]).exists() else "" for n in
         normalize])
    if normalize or delete_empty_lines:
        norm_process_expr = [f"'s|{expr.split('-->')[0]}|{expr.split('-->')[1]}|g'"
                             for expr in normalize if len(expr.split('-->')) == 2]
        if delete_empty_lines: norm_process_expr.extend(["'/^[[:space:]]*$/d'"])
        return f"sed -i -e " + " -e ".join(norm_process_expr) + ' '
    return None


def accuracy_process(filepath, textfile):
    """ Cli process to generate an accuracy report with ocreval (https://github.com/eddieantonio/ocreval) """
    return f"accuracy {str(filepath.with_suffix('.gt.txt').resolve())} {str(textfile.resolve())} " \
           f"{str(textfile.with_suffix('.accuracy').resolve())}"


def wait_for_process(process_id):
    """ Cli process to wait till the sem jobs are finished """
    return f"sem --id {process_id} --wait"


@click.command()
@click.argument('filepaths', nargs=-1, type=click.Path(exists=True))
@click.option('-j', '--jobs', default="1", help="Jobs to parallelize the ocr job in numbers or percentage")
@click.option('-s', '--skip', is_flag=True, default=False, help="Skip already existing textfiles")
@click.option('-r', '--rank-all', is_flag=True, default=False, help="Rank all existing textfiles in the folder")
@click.option('-n', '--normalize', multiple=True, help="Normalizes the textfiles. (e.g. long s to short s ſ-->s or "
                                                       "provide a file with normalizations with @filepath)")
@click.option('-d', '--delete-empty-lines', is_flag=True, default=False, help="Delete all lines which are empty")
@click.option('-m', '--models', multiple=True,
              help="Tesseract models to get validate. To check all models from a subfolder use '{subfoldername}*'")
@click.option('--summarized-report', default="", type=click.Path(),
              help="Filepath to store a summarized report")
def evaluate_models(filepaths, jobs, skip, rank_all, normalize, delete_empty_lines, models, summarized_report):
    """ Evaluate tesseract models and ranks them """
    filepaths = itertools.chain.from_iterable([[Path(filepath)] if os.path.isfile(filepath) else [filename for
                                                                                                  filename in
                                                                                                  Path(filepath).glob(
                                                                                                      '*') if (
                                                                                                              filename.is_file() and imghdr.what(
                                                                                                          filename))]
                                               for filepath in filepaths])
    try:
        available_models = check_output(['tesseract', '--list-langs']).decode('utf-8').split('\n')[1:]
        models = set([available_model for model in models for available_model in available_models if
                      (model.endswith('*') and available_model.startswith(model[:-1])) or model == available_model])
    except CalledProcessError:
        print('Could not found tesseract on the system.')
        return
    textfilefolders = defaultdict(list)
    start_process = time.time()
    process_id = f'validate_ocraccuracy_{start_process}'
    normalize_process = normalization_process(normalize, delete_empty_lines)
    print(f"🕵 Automatic model evaluation\n"
          f"🎽 Competing: {len(models)} models\n"
          f"📈 Start evaluation\n")
    for filepath in tqdm(filepaths, desc="Files", leave=None):
        for model in tqdm(models, desc="Models", leave=None):
            process = multiprocessing_process(jobs, process_id)
            textfile = Path(str(filepath.with_suffix('').resolve()).replace('.', '_')).joinpath(
                filepath.with_suffix('.' + model.replace('/', '_')).name + '.txt')
            textfile.parent.mkdir(exist_ok=True)
            textfilefolders[textfile.parent].append(textfile)
            if not (skip and textfile.exists()):
                process += ocr_process(model, filepath, textfile)
                if normalize and normalize_process:
                    process += normalize_process + f"{textfile.resolve()}; "
            process += accuracy_process(filepath, textfile)
            run(process.split(), stderr=DEVNULL)
    run(wait_for_process(process_id).split())
    print("🏅 Create ranking")
    medals = {0: "🥇", 1: "🥈", 2: "🥉"}
    accuracy_sum = defaultdict(float)
    for folder, textfiles in textfilefolders.items():
        print(f"📁 Top models for {folder.resolve()} ")
        accuracy_single = defaultdict(float)
        if rank_all:
            textfiles = folder.glob('*.txt')
        for textfile in textfiles:
            accfile = textfile.with_suffix('.accuracy')
            if accfile.exists():
                modelname = accfile.name.split('.', 1)[1].rsplit('.', 1)[0]
                modelacc = float(accfile.read_text().split("\n")[4].strip().split(" ")[0][:-1])
                accuracy_sum[modelname] = (accuracy_sum[modelname] + modelacc) / 2 if \
                    accuracy_sum.get(modelname, False) else modelacc
                accuracy_single[modelname] = modelacc
        with open(folder.joinpath(folder.name + ".accuracy_ranking"), 'w') as fout:
            for model_index, model in enumerate(sorted(accuracy_single, key=accuracy_single.get, reverse=True)):
                fout.write(f"{model_index:02d} {accuracy_single[model]:.2f}  \t{model}\n")
                if model_index < 20:
                    print(f"{medals.get(model_index, '☁️')}   {accuracy_single[model]:.2f}  \t{model}")
    summarized_report = Path(summarized_report) if summarized_report != "" else None
    if summarized_report and summarized_report.exists():
        summarized_report.unlink()
        summarized_report.parent.mkdir(exist_ok=True)
    if len(textfilefolders.keys()) > 1:
        print(f"🎽 Top models over all")
        for model_index, model in enumerate(sorted(accuracy_sum, key=accuracy_sum.get, reverse=True)):
            if model_index < 20:
                print(f"{medals.get(model_index, '☁️')}   {accuracy_sum[model]:.2f}  \t{model}")
            if summarized_report:
                summarized_report.open('a').write(f"{model_index:02d} {accuracy_sum[model]:.2f}  \t{model}\n")
    print(f"\n⏰ Finished evaluating models in {round(time.time() - start_process)} seconds")
    return


if __name__ == '__main__':
    evaluate_models()
