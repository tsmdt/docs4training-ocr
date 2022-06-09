# Training mit Tesseract und Tesstrain

Stand: 21.02.2022 // Thomas Schmidt und Jan Kamlah

## 1. Voraussetzungen

Neben den benötigten Programmen (Python, Tesseract und Tesstrain) wird ein aktiver **GitHub Account** (https://github.com) sowie der grundlegende Umgang mit diesem Dienst vorausgesetzt. Das Training selbst hat außer etwas Arbeitsspeicherbedarf keine hohen Anforderungen an das System: jeder Office-PC sollte in der Lage sein, dass Training zu absolvieren.

Der Trainings-Workflow für Tesseract wird über die Kommandozeile durchgeführt.

### 1.1 Benötigte Programme

* Python >= 3.6
* Tesseract > 4.1.x / 5.x.x **mit Trainings Tools**
* Tesstrain

### 1.2 Installation benötigter Programme

#### 1.2.1 Python >= 3.6

Je nach Betriebssystem kann die Installation von Python >= 3.6 variieren. Eine hilfreiche Anleitung findet sich auf [Real Python](https://realpython.com/installing-python/).

#### 1.2.2 Tesseract 5.x.x mit Trainings Tools

[Installations Guide](https://github.com/tesseract-ocr/tessdoc/blob/main/Compiling-%E2%80%93-GitInstallation.md#build-with-training-tools) für Tesseract 5.x.x.

#### 1.2.3 Tesstrain

1. [Tesstrain](https://github.com/tesseract-ocr/tesstrain) von Github über die Kommandozeile klonen:

```
git clone https://github.com/tesseract-ocr/tesstrain.git

# oder via SSH

git clone git@github.com:tesseract-ocr/tesstrain.git
```

2. In den Tesstrain-Ordner wechseln:

```
cd tesstrain
```

3. Für Tesstrain relevante Packages installieren:

```
pip install -r requirements.txt

# oder 

python3 -m pip -r requirements.txt
```

## 2. Tesseract Modell-Training mit Tesstrain

1. Tesstrain stellt einen Trainingsworkflow für Tesseract zur Verfügung, der mit Hilfe bereitgestellter Ground Truth neue Tesseract-Modelle trainieren kann. Darüber hinaus ist auch das Finetuning (Nachtraining) eines bereits existierenden Tesseract-Modells mit Tesstrain möglich. (siehe Punkt 2.2.)
2. Ein Tesseract-Training mit Tesstrain wird über die Kommandozeile ausgeführt.
3. Grundsätzlich können zwei Trainings-Modi unterschieden werden:

* Training from scratch (Training eines neuen Modells): Ein *training from scratch* erstellt auf Grundlage bereitgestellter Ground Truth **ein neues Tesseract-Modell**
* Finetuning / Nachtraining: Das Finetuning bzw. Nachtraining eines *bestehenden* Tesseract-Models erfolgt mit bereitgestellter Ground Truth und ist im Allgemeinen auf das Nachtraining einzelner, bestimmter (Sonder-)Zeichen und Buchstaben konzentriert, die in einem bestehenden Modell nicht enthalten oder von diesem nur schlecht erkannt werden.

4. Die für das Training verwendete Ground Truth muss in Form von Bild-Textzeilen-Paaren vorliegen:

![Image](./Images/001.png)

Hinweise:

* Die Bilder müssen als `TIF`oder `PNG` vorliegen. Erlaubt sind folgende Dateiendungen: `.tif`, `.png`, `.bin.png` oder `.nrm.png`
* Die mit den Bildern korrespondierenden Textzeilen müssen im `TXT`-Format vorliegen und die Dateiendung `.gt.txt` besitzen
* Die Dateinamen eines Bild-Textzeilen-Paares müssen, bis auf die Dateiendung, miteinander wie im obigen Beispiel übereinstimmen. (Anmerkung: Sollten die GT-Daten in einem anderen Format, wie hOCR, PAGE- oder ALTO-XML, vorliegen, müssen diese zunächst in Bild-Textzeilen-Paare konvertiert werden. (siehe <https://github.com/uniwue-zpd/PAGETools>, <https://github.com/cneud/alto-tools>))

### 2.1 Training From Scratch

*work in progress*

### 2.2 Finetuning / (werkspezifisches) Nachtraining

1. Für ein Finetuning / Nachtraining mit Tesstrain muss ein bereits existierendes Tesseract-Modell vorhanden sein. Tesseract unterscheidet zwei Arten von Modellen: „best-Modelle“ basierend auf Fließkommazahlen (float) und „fast-Modelle“ basierend auf Ganzzahlen (integer). Es können nur best-Modelle nachtrainiert werden. Bei einem Trainingsversuch auf ein fast–Modell würde der Fehler auftreten, dass ein Training mit einem integer (fast) Modell nicht fortgeführt werden kann.

![Image](./Images/002.png)

2. Der Pfad zu dem Tesseract-Modell, das nachtrainiert werden soll, muss bekannt sein. Üblicherweise werden Modelle nachtrainiert, die sich im tessdata-Ordner befinden. Über folgenden Befehl können alle Tesseract-Modelle angezeigt werden, die sich im tessdata-Ordner befinden:

```
tesseract --list-langs
```

![Image](./Images/003.png)

3. Tesseract-Modelle besitzen die Dateiendung `.traineddata`.

![Image](./Images/004.png)

4. Im folgenden Beispiel wird das Tesseract-Modell [Fraktur.traineddata](https://github.com/tesseract-ocr/tessdata/blob/4767ea922bcc460e70b87b1d303ebdfed0897da8/script/Fraktur.traineddata) mit zusätzlicher Ground Truth nachtrainiert.

![Image](./Images/005.png)

5. Zunächst muss die zusätzliche Ground Truth bereitgestellt werden. Hierfür wird in der Kommandozeile in den tesstrain-Ordner gewechselt:

```
cd Pfad/zu/tesstrain-Ordner
```

![Image](./Images/006.png)

6. Falls noch nicht vorhanden, muss ein neuer Ordner mit dem Namen `data` im Ordner `tesstrain` erstellt werden:

```
mkdir data
```

![Image](./Images/007.png)

7. Im Ordner `data` einen weiteren Ordner erstellen, in dem die für das Nachtraining verwendete Ground Truth abgelegt wird. Der Dateiname des Ordners muss folgende Struktur besitzen (auf *Unter- und Bindestriche achten*!):

```
tesstrain/data/<MODEL_NAME>-ground-truth
```

Beispiel

```
mkdir data/Fraktur_Finetune-ground-truth
```

Ergebnis

```
tesstrain/data/Fraktur_Finetune-ground-truth
```

![Image](./Images/008.png)

8. Die für das Nachtraining zu verwendende Ground Truth in den neu erstellten Ordner via Windows Explorer / MacOS Finder etc. kopieren. Alternativ können die Kommandozeilen-Befehle verschieben (`mv`) oder kopieren (`cp`) verwendet werden:

```
cp -a Pfad/zu/GT-Daten/. Pfad/zu/GT-Daten-Ordner
```

Beispiel

```
cp -a ~/Beispiel/Ordner/Ground-Truth/Fraktur_Finetune/. ~/tesstrain/data/Fraktur_Finetune-ground-truth
```

Ergebnis

![Image](./Images/009.png)

 9. Der Nachtrainingsworkflow via Tesstrain wird über den Kommandozeilen-Befehl `$ make training` angestoßen. Der Befehl muss aus dem tesstrain-Verzeichnis ausgeführt werden.
10. Die Ausführung des `$ make training` Befehls bedarf folgender Grundstruktur und Parameter:

```
make training MODEL_NAME=Name_des_nachtrainierten_Modells START_MODEL=Name_des_existierenden_Basismodells TESSDATA=Pfad/zu/tessdata/Ordner GROUND_TRUTH_DIR=Pfad/zu/GT-Daten MAX_ITERATIONS=Anzahl-Trainingswiederholungen
```

Erläuterung der Parameter:

* `MODEL_NAME` = Name des neuen (nachtrainierten) Modells; kann frei vergeben werden
* `START_MODEL` = Name des Basismodells im tessdata-Ordner ohne Dateiendung `.traineddata` (Bsp.: `Fraktur` statt `Fraktur.traineddata`)
* `TESSDATA` = Pfad zum Ordner `tessdata` (oder Unterordner im `tessdata`-Ordner), in dem sich das Basismodell befindet
* `GROUND_TRUTH_DIR` = Pfad zum Ground Truth-Verzeichnis im `tesstrain/data`-Ordner
* `MAX_ITERATIONS`= Anzahl von Wiederholungen des Trainingsprozesses; Die Zahl an Wiederholungen kann frei gewählt werden. Als Ausgangspunkt und Test sollte die vorhandene Ground Truth um den Faktor 10 multipliziert werden (Bsp: 120 Ground Truth Bild-Zeilen-Paare \* 10 = 1200 Iterationen). Alternativ zu `MAX_ITERATIONS` kann auch der Parameter `EPOCHS` verwendet werden; Eine Epoche bezeichnet einen vollständigen Trainingsdurchlauf über alle Ground Truth Daten (eine Epoche über 120 Ground Truth Bild-Zeilen-Paare umfasst somit 120 Iterationen; 10 Epochen = 1200 Iterationen). Bsp.: `EPOCHS = 10`

Beispiel

```
make training MODEL_NAME=Fraktur_Finetune START_MODEL=Fraktur TESSDATA=/usr/local/share/tessdata/tessdata_best/script GROUND_TRUTH_DIR=/home/thschmidt/tesstrain/data/Fraktur_Finetune-ground-truth MAX_ITERATIONS=1200
```

![Image](./Images/010.png)

11. Nach Bestätigung des `make training` Befehls werden im Ground Truth Ordner `lstm`- und `box`-Dateien für jedes Bild-Text-Paar erstellt, die für das Training verwendet werden:

![Image](./Images/011.png)

12. Nach Abschluss dieses Schritts beginnt der eigentliche Trainingsprozess. Standardmäßig wird nach 100 Iterationen eine Meldung über den Trainingsfortschritt in der Kommandozeile ausgegeben. Bei größeren Trainingsfortschritten wird ein Checkpoint in `tessdata/data/MODEL_NAME/checkpoints` gespeichert.

![Image](./Images/012.png) *Erklärungen zu den ausgegebenen Daten sind [hier](https://tesseract-ocr.github.io/tessdoc/tess4/TrainingTesseract-4.00.html#iterations-and-checkpoints) zu finden.*

13. Nach Abschluss des Trainings wird eine weitere Meldung ausgegeben, welche die `minimal error rate` (`BCER`, Bag-of-Character Error Rate) des zuletzt gespeicherten Checkpoint anzeigt.

![Image](./Images/013.png)

14. Abschließend müssen die gespeicherten checkpoints in `.traineddata`-Dateien umgewandelt werden. Hierfür wird der Befehl `make traineddata` verwendet. Der Befehl um alle Checkpoints umwandeln:

```
make traineddata MODEL_NAME=<Name des nachtrainierten Modells>
```

Beispiel

```
make traineddata MODEL_NAME=Fraktur_Finetune
```

![Image](./Images/014.png)

Der Befehl wandelt alle Checkpoints in `.traineddata`-Dateien um und erstellt im Ordner `tessdata/data/MODEL_NAME` zwei weitere Ordner: `tessdata_best` und `tessdata_fast`. In diesen Ordnern finden sich die Checkpoints / Modelle des Nachtrainings.

![Image](./Images/015.png)

15. Für die Evaluation der unterschiedlichen Checkpoints / Modelle empfiehlt es sich, einen entsprechenden Ordner im `tessdata`-Verzeichnis anzulegen und die Modelle in diesen Ordner zu verschieben (`mv`) oder kopieren (`cp`):

```
cp -a Pfad/zu/Neuen_Modellen/. Pfad/zu/tessdata-Ordner/
```

Beispiel

```
cp -a ~/tesstrain/data/Fraktur_Finetune/tessdata_fast/. /usr/local/share/tessdata/Fraktur_Finetune_EVAL
```

![Image](./Images/016.png)

16. Über den Befehl `tesseract --list-langs `werden diese Modelle nun auch angezeigt und können für die Texterkennung via Tesseract verwendet werden:

```
tesseract --list-langs
```

![Image](./Images/017.png)

## 3. Evaluation trainierter Modelle

1. Im Folgenden wird beispielhaft eine Evaluation von mit Tesseract und Tesstrain (nach-)trainierten Checkpoints / Modellen durchgeführt. Für die Evaluation wird das Python-Skript `evaluate_models.py `verwendet, das sich im Skripte-Ordner dieser Anleitung befindet.
2. Für die Evaluation müssen Ground Truth-Daten genutzt werden, die **nicht** im Trainingsprozess verwendet worden sind. (Bspw. reale Buchseiten, an denen die neu trainierten Modelle getestet werden sollen).

Beispiel

![Image](./Images/018.png)

Hinweis

* Die Bilddateien müssen im `PNG`, `JPG` oder `TIF` Format vorliegen.
* Die zugehörige Transkription muss als `TXT`-Datei vorliegen und die Dateiendung `.gt.txt` besitzen.
* Die Dateinamen von Bild- sowie zugehöriger Textdatei müssen, bis auf die Dateiendungen, identisch sein. Beispiel: `eval_beispiel-01.png` und `eval_beispiel-01.gt.txt`

3. **Ablauf der Evaluation**: Die Evaluation startet für jede Ground-Truth-Bilddatei (wie im Beispiel `eval_beispiel-01.jpg`), die für den Evaluationszweck bereitgestellt wurde, eine Texterkennung mit Tesseract. Die für die Texterkennung verwendeten Tesseract-Modelle können im Voraus angegeben werden (= unter Punkt 2. neu trainierte Modelle). Die Ergebnisse der Texterkennung mit diesen Modellen werden abschließend mit der Text-Ground-Truth (wie im Beispiel `eval_beispiel-01.gt.txt`) des zugehörigen Bildes verglichen. (Siehe Punkt 3.3.)

### 3.1. Setup zur Evaluation

1. Einen neuen Ordner für die Evaluation anlegen. In diesem Ordner werden die Auswertungen der Modelle gespeichert. Der Name des Ordners kann frei vergeben werden; für unser Beispiel verwenden wir den Ordnernamen `evaluation`:

```
mkdir evaluation
```

2. In diesen Ordner müssen die Dateien `evaluate_models.py` und `requirements.txt` aus dem Skripte-Ordner dieser Anleitung kopiert werden.

![Image](./Images/021.png)

3. Installation der Python-Skript:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

![Image](./Images/022.png)

4. Vor jeder Benutzung des Evaluationsskriptes `evaluate_models.py` muss die virtuelle Pyhtonumgebung gestartet werden, die oben mit dem Befehl `python3 -m venv venv` angelegt worden ist. Hierfür muss in den Ordner `evaluation` gewechselt und der Befehl `source venv/bin/activate` ausgeführt werden:

   ```
   cd evaluation
   source venv/bin/activate
   ```

   ![Image](./Images/023.png)Hinweis: Vor dem Benutzernamen sollte nun der Begriff `venv` erscheinen, der angibt, dass die virtuelle Pythonumgebung aktiviert wurde und das Evaluationsskript ausgeführt werden kann.
5. Zusätzlich basieren die Auswertungen auf den Evaluationsreportings von ocreval. Eine Schritt-für-Schritt Installationsanleitung für das Programm findet sich unter <https://github.com/eddieantonio/ocreval>.

### 3.2. Bereitstellung der Ground-Truth-Daten für die Evaluation

1. Im Ordner `evaluation` einen weiteren Ordner für die Ground Truth erstellen. Auch dieser Ordnername kann frei vergeben werden. Für unser Beispiel verwenden wir `eval-data` und kopieren die für die Evaluation zu verwendende Ground Truth in diesen Ordner:

```
cd evaluation
mkdir eval-data
cp -a ~/Ordner/der/GT/zur/Evaluation/. ~/evaluation/eval-data
```

![Image](./Images/024.png)

### 3.3. Durchführung der Evaluation

1. Um die Evaluation zu starten, wird das Python-Skript `evaluate_models.py` ausgeführt und der Pfad zur Ground Truth angegeben, die für die Evaluation verwendet werden soll. Das Skript startet eine Texterkennung mit Tesseract über die bereit gestellte Ground Truth im `eval-data` Ordner und verwendet hierfür die angegebenen Tesseract-Modelle.

Beispiel

```
python3 evaluate_models.py -m 'Fraktur_Finetune_EVAL*' -j 60% -r /home/thschmidt/evaluation/eval-data
```

Erläuterung

* `python3 evaluate_models.py` = startet das Python-Skript
* `-m 'Fraktur_Finetune_EVAL*'` = gibt den Ordner im `tessdata`-Ordner an, in dem die Tesseract-Checkpoints / Modelle abliegen, die unter Punkt 2.2. trainiert worden sind. Die Trunkierung `*` gibt an, dass alle Modelle, die im Ordner `Fraktur_Finetune_EVAL` abliegen, evaluiert werden sollen
* `-j 60%` = Parallelisiert die Evaluation, um die Auswertung zu beschleunigen und verwendet in diesem Fall 60 % der zur Verfügung stehenden Prozessorkerne
* `-r` = gibt an, das alle im Ordner `eval-data` existierenden Ground Truth Daten evaluiert werden sollen
* `/home/thschmidt/evaluation/eval-data` = Pfad zum Ordner, in dem die für die Evaluation bereit gestellte Ground Truth abliegt.

*Hinweis*: mit dem Befehl `python3 evaluate_models.py --help` kann eine Hilfe in der Kommandozeile ausgegeben werden, die alle zur Verfügung stehenden Parameter des Evaluationsskriptes anzeigt.

2. Nach dem Start des Python-Skriptes wird die Evaluation angestoßen, die, je nach Umfang der zur Auswertung verwendeten Ground Truth, einige Minuten dauern kann. In der Kommandozeile wird der Fortschritt der Evaluation sowie die an der Evaluation teilnehmenden Tesseract-Modelle angegeben.

![Image](./Images/025.png)

3. Nach Abschluss der Evaluation wird das Ranking der Modelle in der Kommandozeile ausgegeben.

![Image](./Images/026.png)

Erläuterung

* Das Ranking gibt die Fehlerrate aller Modelle getrennt nach den in der Evaluation verwendeten Ground-Truth-Daten an.
* Der erste Block zeigt das Ergebnis für das Ground-Truth-Paar `eval_beispiel-01`, der zweite Block das Ergebnis für das Ground-Truth-Paar `eval_beispiel-02`, der Dritte und letzte Block (`Top models over all`) gibt die durchschnittlich besten Modelle aus.
* Die Zahlen vor jedem Modell geben die Zeichnerkennungsrate des Modells an. `99.15` bedeutet, dass das Modell `Fraktur_Finetune_1.380000_147_600` im `tessdata`-Ordner `Fraktur_Finetune_EVAL` für die bereit gestellte Ground-Truth-Datei `eval_beispiel-01.jpg` eine Zeichnerkennungsrate von 99.15 % erzielt, also eine Zeichenfehlerrate (CER) von 0.85 % erzeugt.
* Für jede Bilddatei, die in der Evaluation verwendet wurde, wurden im Ordner `evaluation/eval-data/`ein Unterordner erstellt, in denen die OCR-Ergebnisse der zu evaluierenden Modelle abgelegt werden.

![Image](./Images/027.png)

* Die OCR-Ergebnisse liegen im `TXT`-Format vor und sind mit den Modell-Namen benannt, die an der Evaluation teilgenommen haben.

![Image](./Images/028.png)