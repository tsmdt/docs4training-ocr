# Training with eScriptorium

*eScriptorium is a platform for manual or automated segmentation and text recognition of historical manuscripts and prints* [[Wikipedia](https://de.wikipedia.org/wiki/EScriptorium)]. In addition, the platform enables user-friendly training and (work-specific) fine-tuning of own layout segmentation and text recognition models directly in the browser. eScriptorium is open-source and free of charge. The trained models can be downloaded and used without restrictions.

The following step-by-step guide provides an introduction to the use of eScriptorium for training own OCR or HTR models.

## 1. How does training in eScriptorium work?

For all automated layout segmentation and text recognition tasks, eScriptorium uses the open-source OCR engine [Kraken](https://kraken.re/main/index.html). The models used for layout segmentation and text recognition can be trained directly in eScriptorium with just a few clicks. Both completely new models can be trained (*training from scratch*) and existing models can be fine-tuned (*fine-tuning*) for specific use cases or domains. The training of OCR models is often carried out via the command line and requires appropriate knowledge. Since eScriptorium has a graphical user interface, users without command line knowledge can also carry out trainings. 

It is necessary to understand the area of application of the two training variants mentioned: 
- **Training from scratch**: The training of a completely new model that is not based on any other model is called training from scratch. So-called ground truth is used for training, e.g. images of book pages with corresponding transcriptions that capture the text content of the book pages. In order to generate high-quality and robust OCR models with training from scratch, a very large amount of data is usually required (sometimes several hundred thousand lines of text).  



