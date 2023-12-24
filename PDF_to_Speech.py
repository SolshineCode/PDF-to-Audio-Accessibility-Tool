import PyPDF2
from transformers import pipeline
from pydub import AudioSegment
from PyPDF2 import PdfReader

# Step 1: Read the PDF
pdf_file = open(r'C:\Users\..., 'rb')
                #Replace the ... with the path to your PDF file
pdf_reader = PdfReader(pdf_file)
text = ''
for page in pdf_reader.pages:
    text += page.extract_text()
    
# Step 2: Split the text into 200-word chunks
words = text.split()
chunks = [' '.join(words[i:i+200]) for i in range(0, len(words), 200)]

# Step 3: Initialize the TTS model
tts = pipeline('text-to-speech')

from gtts import gTTS
import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

# Step 4: Generate and save the audio files
audio_files = []
for i, chunk in enumerate(chunks):
    audio_file = f'audio_{i}.wav'
    engine.save_to_file(chunk, audio_file)
    engine.runAndWait()
    audio_files.append(audio_file)

    #You may also be left with the chunked pieces of the spoken document saved additionally on your machine unless a function is added here to delete them after combining them

# Step 5: Merge the audio files
combined = AudioSegment.empty()
for audio_file in audio_files:
    sound = AudioSegment.from_wav(audio_file)
    combined += sound

# Step 6: Save the final audio file
combined.export(r"C:\Users\....wav", format="wav")
                    #Replace the ... with the path to your output file and intended file name
