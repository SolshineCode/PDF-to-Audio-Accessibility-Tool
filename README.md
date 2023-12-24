# PDF-to-Audio-Accessibility-Tool
This tool converts PDF text into audio files, AKA PDF to Speech, enhancing accessibility especially for neurodivergent and visually impaired individuals.
LICENSE: Hippocratic License 3.0 with most modules
[![Hippocratic License HL3-BDS-CL-ECO-EXTR-FFD-LAW-MEDIA-MIL-MY-SV-TAL](https://img.shields.io/static/v1?label=Hippocratic%20License&message=HL3-BDS-CL-ECO-EXTR-FFD-LAW-MEDIA-MIL-MY-SV-TAL&labelColor=5e2751&color=bc8c3d)](https://firstdonoharm.dev/version/3/0/bds-cl-eco-extr-ffd-law-media-mil-my-sv-tal.html)

# README

## PDF to Audio Converter: An Accessibility Tool

This Python script is a powerful accessibility tool designed to convert text from PDF files into audio. It's particularly useful for neurodivergent individuals, people with visual impairments, or anyone who benefits from multimodal content. By transforming written information into audio, we can make content more accessible and inclusive.

### Features

- Extracts text from a PDF file.
- Splits the text into manageable chunks.
- Converts each chunk of text into speech.
- Merges all the audio files into one.
- Saves the final audio file.

### Installation

Before running the script, you need to install several Python libraries. Open your terminal and run the following commands:

```bash
pip install PyPDF2
pip install pyttsx3
pip install pydub
```

### Usage

1. Clone this repository to your local machine.
2. Open the `PDF_to_Text_Transformers_Direct.py` file in a text editor.
3. Replace `'your_file.pdf'` on line 7 with the path to your PDF file.
4. Replace `'C:\\Users\\....wav'` on line 42 with the path to your output file and intended file name.
5. Save the changes and close the text editor.
6. Run the script from the terminal with the command `python PDF_to_Text_Transformers_Direct.py`.

### Note

This script uses the pyttsx3 library, which uses the speech synthesis engines that come with the operating system. Therefore, it doesn't require an internet connection. However, the quality and characteristics of the speech might vary depending on the system's speech synthesis engine.

By using this tool, we hope to make information more accessible and learning more inclusive. Enjoy your new audio files!
