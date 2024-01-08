# Training with Tesseract and Tesstrain

## 1. Requirements
In addition to the required software (Python, Tesseract and Tesstrain), an active **GitHub account** (https://github.com) and basic user knowledge of this service are required. The training itself does not have high system requirements apart from some memory requirements: any office PC should be able to complete the training.

The training workflow for Tesseract is carried out via the command line.

### 1.1 Required software
* Python >= 3.6
* Tesseract > 4.1.x / 5.x.x **with training tools**
* Tesstrain

### 1.2 Installation of required software

#### 1.2.1 Python >= 3.6
Depending on the operating system, the installation of Python >= 3.6 may vary. A helpful guide can be found on [Real Python](https://realpython.com/installing-python/).

#### 1.2.2 Tesseract 5.x.x with trainings tools
[Installation guide for Tesseract *with* training tools](https://github.com/tesseract-ocr/tessdoc/blob/main/Compiling-%E2%80%93-GitInstallation.md#build-with-training-tools).

#### 1.2.3 Tesstrain

1. Clone [Tesstrain](https://github.com/tesseract-ocr/tesstrain) from Github via the command line:

```
git clone https://github.com/tesseract-ocr/tesstrain.git

# or via SSH

git clone git@github.com:tesseract-ocr/tesstrain.git
```

2. Change to the Tesstrain folder:

```
cd tesstrain
```

3. Install packages relevant for Tesstrain:

```
pip install -r requirements.txt

# or 

python3 -m pip -r requirements.txt
```

## 2. Tesseract model training with Tesstrain
1. Tesstrain provides a training workflow for Tesseract that can train new Tesseract models with the help of provided ground truth. It is also possible to fine-tune (retrain) an existing Tesseract model with Tesstrain. (see point 2.2.)
2. Tesseract training with Tesstrain is carried out via the command line.
3. Two basic training modes can be distinguished:

* Training from scratch (training of a new model): A *training from scratch* creates **a new Tesseract model** based on the ground truth provided
* Fine-tuning / retraining: The fine-tuning or retraining of an *existing* Tesseract model is carried out with the ground truth provided and generally focuses on the retraining of individual, specific (special) characters and letters that are not contained in an existing model or are poorly recognised by it.

4. The ground truth used for the training must be available in the form of image-text line pairs:

![Image](./Images/001.png)

Notes:

* The images must be available as `TIF` or `PNG`. The following file extensions are permitted: `.tif`, `.png`, `.bin.png` or `.nrm.png`.
* The text lines corresponding to the images must be in `TXT` format and have the file extension `.gt.txt`.
* The file names of an image-text line pair must match, except for the file extension, as in the example above. (Note: If the GT data is in a different format, such as hOCR, PAGE or ALTO-XML, it must first be converted into image-text line pairs. (see <https://github.com/uniwue-zpd/PAGETools>, <https://github.com/cneud/alto-tools>))

### 2.1 Training from scratch
*work in progress*

### 2.2 Finetuning / (work-specific) Fine-tuning
1. An existing Tesseract model must be available for fine-tuning / retraining with Tesstrain. Tesseract distinguishes between two types of models: "best models" based on floating point numbers (float) and "fast models" based on integer numbers (integer). Only best models can be retrained. If training is attempted on a fast model, the error would occur that training cannot be continued with an integer (fast) model.

![Image](./Images/002.png)

2. The path to the Tesseract model that is to be retrained must be known. Models located in the tessdata folder are usually retrained. The following command can be used to display all Tesseract models located in the tessdata folder:

```
tesseract --list-langs
```

![Image](./Images/003.png)

3. Tesseract models have the file extension `.traineddata`.

![Image](./Images/004.png)

4. In the following example, the Tesseract model [Fraktur.traineddata](https://github.com/tesseract-ocr/tessdata/blob/4767ea922bcc460e70b87b1d303ebdfed0897da8/script/Fraktur.traineddata) is retrained with additional ground truth.

![Image](./Images/005.png)

5. Firstly, the additional ground truth must be provided. To do this, switch to the tesstrain folder in the command line:

```
cd path/to/tesstrain-folder
```

![Image](./Images/006.png)

6. If not already present, a new folder with the name `data` must be created in the `tesstrain` folder:

```
mkdir data
```

![Image](./Images/007.png)

7. Create another folder in the `data` folder in which the ground truth used for the fine-tuning is stored. The file name of the folder must have the following structure (pay attention to *underscores and hyphens*!):

```
tesstrain/data/<MODEL_NAME>-ground-truth
```

Example:

```
mkdir data/Fracture_Finetune-ground-truth
```

Result:

```
tesstrain/data/Fracture_Finetune-ground-truth
```
