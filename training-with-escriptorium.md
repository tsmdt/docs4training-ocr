# Training with eScriptorium (*step-by-step guide*)

*eScriptorium is a platform for manual or automated segmentation and text recognition of historical manuscripts and prints* [[Wikipedia](https://de.wikipedia.org/wiki/EScriptorium)]. In addition, the platform enables user-friendly training and (work-specific) fine-tuning of own layout segmentation and text recognition models directly in the browser. eScriptorium is open-source and free of charge. The trained models can be downloaded and used without restrictions.

The following step-by-step guide provides an introduction to the use of eScriptorium for training own OCR or HTR models.

## 1. How does training work?

For all automated layout segmentation and text recognition tasks, eScriptorium uses the open-source OCR engine [Kraken](https://kraken.re/main/index.html). The models used for layout segmentation and text recognition can be trained directly in eScriptorium with just a few clicks. Both completely new models can be trained (*training from scratch*) and existing models can be fine-tuned (*fine-tuning*) for specific use cases or domains. The training of OCR models is often carried out via the command line and requires appropriate knowledge. Since eScriptorium provides a graphical user interface, users without command line knowledge can also carry out trainings. 

It is necessary to understand the area of application of the two training variants mentioned: 

- **`Training from scratch`**: The training of a completely new model (that is not based on an already existing model) is called *training from scratch*. So-called *ground truth* is used for training, e.g. images of book pages with corresponding transcriptions that capture the text content of the pages. In order to generate robust OCR models with a training from scratch, a large amount of data is usually required (sometimes several hundred thousand lines of text). This amount can lead to problems with eScriptorium. For example, an eScriptorium project that is to be used for training from scratch with several thousand digitised documents and transcriptions can reach memory and usability limits. In such cases, training from scratch outside of eScriptorium via command line is recommended.
  
- **`Fine-tuning`**: Fine-tuning, or work-specific fine-tuning, involves taking an existing model and specifically adapting it to a new use case or domain (*work-specific* in this context means that the fine-tuning is undertaken with a specific work (e.g. a historical document, manuscript or book) or group of similar works in mind). For example, a basic OCR model trained to recognize standard alphanumeric Latin characters can be unable to identify currency symbols like the Euro (€), Pound (£), or Yen (¥). To fine-tune this model for a financial domain, additional training is done using a dataset that includes these specific currency symbols. This process adjusts the model's parameters to become more sensitive to these new symbols, enabling it to accurately recognize and interpret them in financial documents where they frequently appear.

## 2. How to train in eScriptorium
In order to `train from scratch` or to `fine-tune` an existing model you must provide training data (= *ground truth*). In eScriptorium this training data is provided inside a project. Training data consists of **images** (digitised pages of books, manuscripts, documents etc.) and corresponding **transcriptions**. The transcriptions attempt to capture the text content of the images as accurately as possible. If you don't have any ground truth to train with you can create it inside eScriptorium (i.e. create transcriptions for images you upload to an eScriptorium project). 

Here is an example in eScriptorium:
<img src="./Images/training-eS-03.png" width="100%" height="100%">

With the provided ground truth you are able to start the training process. 

## 3. How to fine-tune a model in eScriptorium

### Step 1: Create a new project
Start with creating a new eScriptorium project by browsing to the eScriptorium start page and clicking on **"My Projects"** in the upper right corner of the screen.

<img src="./Images/training-eS-00.png" width="50%" height="50%">

Next, click on the green **"Create new Project"** button.

<img src="./Images/training-eS-01.png" width="50%" height="50%">

Name your project on the next screen.

<img src="./Images/training-eS-04.png" width="50%" height="50%">



### Step 2: Import your images
### Step 3: Test run layout segmentation and text-recognition on your data
### Step 4: Search for an existing model that works (somewhat)
### Step 5: Create ground truth
### Step 6: Train
### Step 7: Test and evaluate
### Step 8: Iterate
