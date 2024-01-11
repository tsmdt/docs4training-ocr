# Training with eScriptorium (*a step-by-step guide*)
**version 1.0 | January 2024**

"eScriptorium is a platform for manual or automated segmentation and text recognition of historical manuscripts and prints" [[Wikipedia](https://de.wikipedia.org/wiki/EScriptorium)]. In addition, the platform enables user-friendly training and (work-specific) fine-tuning of own layout segmentation and text recognition models directly in the browser. eScriptorium is open-source and free of charge. The trained models can be downloaded and used without restrictions.

The following step-by-step guide provides an introduction to the use of eScriptorium for training own OCR or HTR models.

# Contents

0. [Who is this guide for?](#0-who-is-this-guide-for)
1. [How does training work?](#1-how-does-training-work)
2. [How to train in eScriptorium?](#2-how-to-train-in-escriptorium)
   2.1. [Provide or create training data (ground truth)](#21-provide-or-create-training-data-ground-truth) 
   2.2. [Where to find models](#22-where-to-find-models)
   2.3. [How to choose a model for a specific use case](#23-how-to-choose-a-model-for-a-specific-use-case)
3. [Fine-tuning in eScriptorium](#3-fine-tuning-in-escriptorium)
   3.1. [How to fine-tune a text recognition model](#31-how-to-fine-tune-a-text-recognition-model)
   3.2. [How to fine-tune a layout segmentation model](#32-how-to-fine-tune-a-layout-segmentation-model)
4. [Training from scratch in eScriptorium](#4-training-from-scratch-in-escriptorium)
5. [Additional hints and tips]()
   5.1. [Using the virtual keyboard in eScriptorium](#51-using-the-virtual-keyboard-in-escriptorium)
   5.2. [Ground truth guidelines for text recogntion](#52-ground-truth-guidelines-for-text-recogntion)
   5.3. [Ground truth guidelines for layout segmentation](#53-ground-truth-guidelines-for-layout-segmentation)
6. [License](#6-license)

## 0. Who is this guide for?
This guide is for *intermediate* eScriptorium users with a basic understanding of the graphical interface and functionality of the platform. A video tutorial that introduces the main functions and tools can be found on YouTube: [youtube.com/watch?v=aQuwh3OaKqg](https://www.youtube.com/watch?v=aQuwh3OaKqg) (automatically generated subtitles in English are available). It should be sufficient to follow this guide.

Although an attempt was made to keep the guide as accessible as possible, certain technical terms could not be avoided. Where these are to be found in the guide, we try to explain them as clearly as possible. 

This guide was created during the 3rd [OCR-D](https://ocr-d.de/en/) funding phase in the module project *Workflow for work-specific training based on generic models with OCR-D as well as ground truth enhancement* at the [Mannheim University Library](https://www.bib.uni-mannheim.de/en/about/projects-of-the-university-library/). The module project was funded by the German Research Foundation (DFG) between 2021-2023.

**Feedback is always welcome!**
- [Jan Kamlah](https://orcid.org/0000-0002-0417-7562): `jan.kamlah[at]uni-mannheim[dot]de`
- [Thomas Schmidt](https://orcid.org/0000-0003-3620-3355): `thomas.schmidt[at]uni-mannheim[dot]de`

## 1. How does training work?
For all automated layout segmentation and text recognition tasks, eScriptorium uses the open-source OCR/HTR engine [kraken](https://kraken.re/main/index.html). The models used for layout segmentation and text recognition can be trained directly in eScriptorium with just a few clicks. Both completely new models can be trained (`training from scratch`) and existing models can be fine-tuned (`fine-tuning`) for specific use cases or domains. The training of OCR models is often carried out via the command line and requires appropriate knowledge. Since eScriptorium provides a graphical user interface, users without command line knowledge can also carry out trainings. 

It is necessary to understand the area of application of the two training variants mentioned: 

- **`Training from scratch`**: The training of a completely new model (that is not based on an already existing model) is called *training from scratch*. So-called *ground truth* is used for training, e.g. images of book pages with corresponding transcriptions that capture the text content of the pages. In order to generate robust OCR models with a training from scratch, a large amount of data is usually required (sometimes several hundred thousand lines of text). This amount can lead to problems with eScriptorium. For example, an eScriptorium project that is to be used for training from scratch with several thousand digitised documents and transcriptions can reach memory and usability limits. In such cases, training from scratch outside of eScriptorium via command line is recommended. 
- **`Fine-tuning`**: Fine-tuning, or work-specific fine-tuning, involves taking an existing model and specifically adapting it to a new use case or domain (*work-specific* in this context means that the fine-tuning is undertaken with a specific work (e.g. a historical document, manuscript or book) or group of similar works in mind). For example, a basic OCR model trained to recognize standard alphanumeric Latin characters can be unable to identify currency symbols like the Euro (€), Pound (£), or Yen (¥). To fine-tune this model for a financial domain, additional training is done using a dataset that includes these specific currency symbols. This process adjusts the model's parameters to become more sensitive to these new symbols, enabling it to accurately recognize and interpret them in financial documents where they frequently appear.

## 2. How to train in eScriptorium
### 2.1. Provide or create training data (ground truth)
In order to `train from scratch` or to `fine-tune` an existing model you must provide training data (*ground truth*). In eScriptorium this training data is provided inside a project. Training data consists of **images** (digitised pages of books, manuscripts, documents etc.) and corresponding **transcriptions** or **layout segmentations**. 

#### Ground truth for text recognition models

As the name suggests, text recognition models are used to automatically recognise the text content of an image. If you want to train or fine-tune a text recogntion model you need **images** and **transcriptions**. Here is an example in eScriptorium:

<img src="./Images/training-eS-03.png" width="80%" height="80%"><br/>

The transcriptions attempt to capture the text content of the images as accurately as possible. If you don't have any ground truth to train with you can create it inside eScriptorium (i.e. create transcriptions for images you upload to an eScriptorium project). 

#### Ground truth for layout segmentation models

Layout segmentation models are used to automatically recognise all text regions and text lines on an image and are a preliminary stage to text recognition itself. If you want to train or fine-tune a layout segmentation model you need **images** and **layout segmentation data**. Here is an example in eScriptorium:

<img src="./Images/training-eS-24.png" width="80%" height="80%"><br/>

> **Note:** Chapters [3.1. How to fine-tune a text recognition model](#3-how-to-fine-tune-a-model) and [3.2. How to fine-tune a layout segmentation model](#32-how-to-fine-tune-a-layout-segmentation-model) provide a detailed introduction to the creation of ground truth for text recognition and layout segmentation training.

### 2.2. Where to find models 
Especially for fine-tuning already existing layout segmentation or text recognition models are needed. Here is a list of places where `kraken` models (the OCR/HTR engine eScriptorium uses in the background) can be found:

- **Zenodo**: [zenodo.org/communities/ocr_models](https://zenodo.org/communities/ocr_models)

All downloaded models can be uploaded to eScriptorium by clicking on **"My Models"** on the upper right corner of the screen. Click on **"Upload a model"** in the next screen an choose the model you want to upload.

<img src="./Images/training-eS-10.png" width="80%" height="80%">

### 2.3. How to choose a model for a specific use case
The performance of a model depends on various factors and must be tested for each use case. For example a model trained only on traditional Chinese characters might not perform well on German documents printed in the typeface Fraktur.

Here are some points for orientation that can help with the assessment of a model:
- Has the model been trained on **printed work** or **handwritten** documents?
- Which **languages** (e.g. English, German, Hebrew ...) and **writing systems** (e.g. Latin, Arabic, Chinese ...) does the model cover?
- Which **historical period** and which **historical typefaces** does the model cover? (i.e. is the model suitable for recognising Fraktur fonts, for example?)

> **Note:** As a rule of thumb try testing **generic models** first for your use case. *Generic* or *base models* are usually trained on a wide variety of data (different documents, typefaces etc.) of a specific domain (e.g. printed documents in French of the 18th century). If the model name and description somewhat fit the use case at hand, try testing that generic model first.

## 3. Fine-tuning in eScriptorium
In many cases, `fine-tuning` can be a time- and resource-efficient method for improving an existing layout segmentation or text recognition model for a new use case. In order to carry out fine-tuning, an existing model is required, which is adapted to the new use case during the fine-tuning training process. 

To fine-tune a model in eScriptorium, we recommend the following workflow:

1. Upload the images to be used for training
2. Test the automatic layout segmentation and text recognition for the uploaded images and evaluate the results
3. Improve layout segmentations and transcriptions that were automatically generated in `step 2`
4. Fine-tune the model used in `step 2` with the ground truth created in `step 3`
5. Evaluate the results and repeat `step 3` and `step 4` if necessary

The following steps describe this workflow in detail.

### 3.1. How to fine-tune a text recognition model 
#### Step 1: Create a new project and document
Start with creating a new eScriptorium project by browsing to the eScriptorium start page and clicking on **"My Projects"** in the upper right corner of the screen.

<img src="./Images/training-eS-00.png" width="40%" height="40%">

Next, click on the green **"Create new Project"** button.

<img src="./Images/training-eS-01.png" width="40%" height="40%">

Name your project on the next screen and click on **"Create"**.

<img src="./Images/training-eS-04.png" width="80%" height="80%">

Once the project has been created, the project overview is displayed. The project you have just created should be displayed here. Click on it.

<img src="./Images/training-eS-05.png" width="80%" height="80%">

Create a new document inside your project by clicking on the green **"Create new Document"** button.

<img src="./Images/training-eS-06.png" width="80%" height="80%">

On the next screen, give the document a name and click on **"Create"** (or **"Update"**). A message should appear in the upper right corner that the document has been created successfully.

<img src="./Images/training-eS-07.png" width="80%" height="80%">

#### Step 2: Import your images

Switch to the **"Images"** tab and upload your images either by clicking into the **"Drop images here or click to upload"** section or by clicking the **"Import"** button.

Here are the differences of both options:
- `Drop images here or click to upload`: Upload images from your hard drive in different file formats (`PNG`, `JPG`, `TIFF` etc.)
- `Import` button: Import images via `IIIF` protocol or upload `PDF` documents.

<img src="./Images/training-eS-08.png" width="80%" height="80%">

As soon as all images have been uploaded, they will appear as a preview at the bottom of the screen.

<img src="./Images/training-eS-09.png" width="80%" height="80%">

#### Step 3: Run layout segmentation on your data

> **Note:** Step 3 involves automatic layout segmentation. The aim here is to find a model that already works well for the uploaded images in order to improve this model afterwards in the fine-tuning step (and make them perform even better on the available data). Refer to [chapter 2.2 Where to find models](#22-where-to-find-models) if you are searching for layout segmentation and text recognition models.

Select all images by clicking on the **"Select all"** button. All images in the current document should now be highlighted. 

Next, click on the **"Segment"** button.

<img src="./Images/training-eS-11.png" width="80%" height="80%">

A pop-up (*"Select a model"*) should appear in which the layout segmentation can be set:

<img src="./Images/training-eS-12.png" width="80%" height="80%">

- **1st drop-down**: Choose a layout segmentation model
- **2nd drop-down**: Choose the layout parts that you want to segment (*If no layout segmentation has been carried out so far, the "Lines and regions" setting should be selected.*)
- **3rd drop-down**: Defines the reading direction of the text (e.g. Horizontal from left to right = *Horizontal l2r*)

Next, click on the blue **"Segment"** button to start the layout segmentation. 

An orange-coloured button in the image preview shows the running layout segmentation. As soon as the segmentation for a page is complete, a message (*"Segmentation done!"*) appears in the top right-hand corner of the screen.

<img src="./Images/training-eS-13.png" width="80%" height="80%">

#### Step 4: Check the layout segmentation
Once the layout segmentation has been completed, the pages must be checked. Click on the **blue button** of the first image to activate eScriptorium's editing view.

<img src="./Images/training-eS-14.png" width="80%" height="80%">

Your screen should look like this:

<img src="./Images/training-eS-15.png" width="80%" height="80%">

On the left side of the editing view you find a preview of the image with a the automatically generated layout segments in different colors. eScriptorium differentiates *3 layout regions* or *segments*:

<img src="./Images/training-eS-16.png" width="80%" height="80%"><br/>

1. **Text regions**: A text region usually contains several lines of text. Examples of a text region are: a paragraph, a column of text or a complete page of text. The structre of one or more text regions should correspond to the reading order and layout structure of the respective page.
2. **Line masks** (sometimes called *text lines*): A polygon mask representing a single text lines that covers all characters of the text line. eScriptorium automatically generates line masks from baselines. Therefore: while correcting the results of the automatic layout segmentation, concentrate on text regions and baselines first, as line masks will be automatically recalculated after you adjusted a baseline.
3. **Baselines**: The baseline is the line upon which most letters of a single text line sit. It's especially noticeable in handwritten or printed text, where letters without descending elements (like the lower part of "g" or "p") align along this line.

> **Note**: If the layout segmentation is correct continue with [Step 8: Run text recognition on your data](#step-8-run-text-recognition-on-your-data).

#### Step 5: Correct the text regions
Start by correcting the text regions first. Click on the **blue region icon** to toggle the "region mode":

<img src="./Images/training-eS-17.png" width="80%" height="80%"><br/>

Make sure that the text regions include all text content in a meaningful way. Adjust the text regions accordingly. 

**Example:** On the following page two text columns were segmented as one single text region. The adjustment reflects the actual page layout. 

<img src="./Images/training-eS-18.png" width="80%" height="80%"><br/>

<img src="./Images/training-eS-19.png" width="80%" height="80%"><br/>

#### Step 6: Correct the baselines and line masks
Continue by correcting the baselines. Deactivate region mode by clicking on the **blue region icon** again. Toggle the line mask mode by clicking on the **mask icon** till your preview looks like this:

<img src="./Images/training-eS-20.png" width="80%" height="80%"><br/>

Adjust the baselines in such a way that:
- one single baseline corresponds to one single line of text
- the start of a baseline is marked by a pink stroke (see the screenshot above) and should correspond with the start of the text line
- all characters of the text line sit on the baseline

**Example:** The following screenshots show incorrect baselines and their correction. For example, individual baselines extend beyond the text column boundary so that two separate lines of text are segmented as one. In addition, individual baselines do not run along the baseline of the text line.

<img src="./Images/training-eS-21.png" width="80%" height="80%"><br/>
<img src="./Images/training-eS-22.png" width="80%" height="80%"><br/>

> **Note:** After adjusting a baseline, eScriptorium automatically recalculates the corresponding line masks. Toggle those line masks by clicking on the **blue mask icon** again until the masks are shown. If a line mask should be calculated incorrectly you can adjust it by clicking on it and changing the polygon.

#### Step 7: Correct the layout segmentation for all pages
Repeat steps 5 and 6 for all available pages. Ensuring correct layout segmentation on all pages helps to improve the text recognition quality.

> **Note:** If it is neccessary to correct a large amount of data, it is possible to fine-tune a layout segmentation model by repeating steps 5 and 6 for a small amount of pages, thus creating a set of training data (*ground truth*). After creating the training data, you can fine-tune a layout segmentation model and re-run the automatic layout segmentation (i.e., repeat [Step 3: Run layout segmentation on your data](#step-3-run-layout-segmentation-on-your-data)) with this fine-tuned model, in order to improve the segmentation results. Check [chapter 3.2. How to fine-tune a layout segmentation model](#32-how-to-fine-tune-a-layout-segmentation-model) for further details.

#### Step 8: Run text recognition on your data
> **Note:** Step 8 involves automatic text recognition. The aim here is to find a model that already works well for your data in order to improve this model further through fine-tuning it . Refer to [chapter 2.2 Where to find models](#22-where-to-find-models) if you are searching for layout segmentation and text recognition models.

After completing steps 3 - 6, switch back to **"Images"** tab and click on the **"Select all"** button. 

Next, click on the blue **"Transcribe"** button.

<img src="./Images/training-eS-23.png" width="80%" height="80%"><br/>

A pop-up should appear that lets you choose a text recogntion model:

<img src="./Images/training-eS-25.png" width="80%" height="80%"><br/>

- **Select a model**: Choose a text recognition model
- **Select a transcription**: Select `--New--`

Click on the blue **"Transcribe"** button to start the automatic text recognition.

An orange-coloured button in the image preview shows the running text recognition. As soon as the text recognition for a page is complete, a message (*"Transcription done!"*) appears in the top right-hand corner of the screen.

<img src="./Images/training-eS-26.png" width="80%" height="80%"><br/>

#### Step 9: Check the transcriptions
Once text recognition has been completed, the automatically generated transcriptions must be checked.

1. Click on the **Edit** tab.
2. Next, click on the **"Segmentation view"** button in order to deactivate the layout segmentation view. 
3. Click on the **"Transcription view"** button afterwards to activate the transcription view.
4. Choose the transcription you created during `step 8` in the drop-down menu. The name of the transcription follows this structure: `OCR-engine-name:OCR-model-name`. Example: In `step 8` we chose the model `german_print` for the engine `kraken`. Hence the corresponding name of the transcription is: `kraken:german_print`.

<img src="./Images/training-eS-33.png" width="80%" height="80%"><br/>

If you hover your mouse cursor over one of the text lines in the transcription view on the right side of your screen, the corresponding text line of the image will be highlighted. 

<img src="./Images/training-eS-28.png" width="80%" height="80%"><br/>

Clicking on a text line in the transcription preview will open a pop-up:

<img src="./Images/training-eS-29.png" width="80%" height="80%"><br/>

The automatically generated transcriptions can be checked for errors in this window. The original line of text is shown in the upper part of the pop-up. The lower part displays the transcription of the text line. The cursor keys on the keyboard (`↑` and `↓`) can be used to scroll through all available text lines.

> **Note:** Instead of improving transcription errors at this moment, first check for the approximate number of errors on each page. If the majority of the transcriptions are erroneous, it is advised to test another text recognition model for better results (i.e. repeat [Step 8: Run text recognition on your data](#step-8-run-text-recognition-on-your-data) with a different model). However, if there are only a few errors on each page (rule of thumb: 1 to 2 errors every 2 to 3 text lines), you can continue with improving the transcriptions in [Step 10: Improve the transcriptions and create ground truth](#step-10-improve-the-transcriptions-and-create-ground-truth).

#### Step 10: Improve the transcriptions and create ground truth

`Step 10` corrects transcription errors in order to generate training data (*ground truth*) for fine-tuning a text-recognition model. 

1. Click on the **Edit** tab.
2. Next, click on the **"Segmentation view"** button in order to deactivate it. 
3. Click on the **"Text view"** button afterwards to enable the plain text view.
4. Choose the transcription you created during `step 8` in the drop-down menu.

<img src="./Images/training-eS-27.png" width="80%" height="80%"><br/>

Select **all text lines** (`STRG + A` on Windows or `⌘ + A` on Mac) in the text view and **copy** them (`STRG + C` on Windows or `⌘ + C` on Mac):

<img src="./Images/training-eS-31.png" width="80%" height="80%"><br/>

Choose **"manual"** in the transcription drop-down and **paste** (`STRG + V` on Windows or `⌘ + V` on Mac) the transcription you just copied into the text view:

<img src="./Images/training-eS-32.png" width="80%" height="80%"><br/>

> **Note:** This copying process has the following purpose: In the "manual" transcription, we record the **correct transcription** (= *ground truth*) of the text content of the respective page, which will later be used for training. The automatically generated transcription (created in step 8), which still contains errors, serves as the basis for the correction. The corrections are made in the "manual" transcription, as this ensures that there is only one transcription in our document in which checked and corrected training data can be found, namely the "manual" transcription.

Next, deactivate the **"text view"** and activate the **"transcription view"**:

<img src="./Images/training-eS-34.png" width="80%" height="80%"><br/>

Click on the first text line in the **"transcription view"**. The example below shows an error in the generated transcription. We fix it so that the transcription matches the original text line:

<img src="./Images/training-eS-30.png" width="80%" height="80%"><br/>

After the first text line has been corrected, press the `Enter ↲` key to check and correct the next text line. The cursor keys on the keyboard (`↑` and `↓`) can also be used to scroll through all available text lines of the current page. 

After you have finished correcting the current page, proceed with the next one. *Be sure to follow all instructions of `step 10` (i.e. using the "manual" transcription workflow).*

#### How much training data (ground truth) do I need for fine-tuning?
> Experience has shown that even a **small amount of training data** is enough to start fine-tuning an existing text recognition model. With regard to fine-tuning, an **iterative approach** should be followed: 
> 1. Create 2 to 3 pages of training data by correcting the automatically generated transcriptions as shown in step 10. 
> 2. [Fine-tune the text recognition model](#step-11-fine-tune-a-text-recognition-model) you have used in step 8 with the corrected ground truth . 
> 3. [Test and evaluate](#step-12-re-run-text-recognition-and-evaluate-your-fine-tuned-model) if the fine-tuned model yields better transcriptions on your data than before.
> 4. If not, repeat 1 to 3 to create more training data. Fine-tune new models and evaluate them on your data until the results are satisfactory.

#### Step 11: Fine-tune a text recognition model

If you have created a sufficient amount of training data (refer to section [How much training data (ground truth) do I need for fine-tuning?](#how-much-training-data-ground-truth-do-i-need-for-fine-tuning)), the fine-tuning process itself is simple.

1. Click on the **"Images"** tab.
2. Click on the **"Select all"** button.
3. Click on the blue **"Train"** button.
4. Click on **"Recognizer"**.

<img src="./Images/training-eS-35.png" width="80%" height="80%"><br/>

A pop-up should open, that looks like this:

<img src="./Images/training-eS-36.png" width="80%" height="80%"><br/>

- **1st drop-down**: Choose the "manual" transcription where you saved the corrected ground truth
- **2nd drop-down**: Choose a name for your fine-tuned model
   - *We recommend using descriptive names, that should capture the following information (as this helps later when identifying a model in a large number of other models)*:
      - `Name of parent model`: name of the model you fine-tune. In our example `german_print`.
      - `Name of the documents you train with`: a descriptive name for identifying the data you used for fine-tuning. In our example we use the abbreviation `CharlAmtsschriftum` as we are training with pages from this respective collection.
      - `Model number`: Record the number or generation of the new model. `M1`, as in the example, means: the first fine-tuned model.
- **3rd drop-down**: Select the text recognition model you want to fine-tune. This should be the model you worked with in [step 8](#step-8-run-text-recognition-on-your-data), i.e. the text recognition model that already worked quite well on your data.  In our example this model is `german_print`.

Lastly, click on the blue **"Train"** button to start the fine-tuning. 

A running training is shown as below:

<img src="./Images/training-eS-37.png" width="80%" height="80%"><br/>

If you want to view the training progress, click on **"My models"**:

<img src="./Images/training-eS-38.png" width="80%" height="80%"><br/>

The model you are currently training will appear in this overview. By clicking on the button **"Toggle versions"** you can view all currently finished training epochs as well. You will be notified as soon as the training has finished.

#### Step 12: Re-run text recognition and evaluate your fine-tuned model
#### Step 13: Iterate 

### 3.2. How to fine-tune a layout segmentation model 

## 4. Training from scratch in eScriptorium

## 5. Additional hints and tips

### 5.1. Using the virtual keyboard in eScriptorium
### 5.2. Ground truth guidelines for text recogntion
### 5.3. Ground truth guidelines for layout segmentation
## 6. License
This guide is licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).