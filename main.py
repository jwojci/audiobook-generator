import sys, pathlib, fitz, os
from dotenv import load_dotenv
from AudioMerger import AudioMerger
from DocProcessor import DocProcessor
from PdfHelper import PdfHelper
from AudioGenerator import AudioGenerator

# load .env to read API key
load_dotenv()

# --------------------------------
# Read the book and process its contents
# --------------------------------

# Read the book file
pdfHelper = PdfHelper(read_file_path="docs\examplebook.pdf")
doc = pdfHelper.get_doc()

# Get table of contents
toc = doc.get_toc()

# For every chapter save its contents in a separate file

docProcessor = DocProcessor(doc, output_path="outputs")
docProcessor.save_chapters()

# Get each saved chapters file path

chapter_paths = docProcessor.get_chapter_paths()

# Split each chapter into chunks that can be fed into OpenAIs TTS model

chunks = docProcessor.split_chapters(chapter_paths)

# --------------------------------
# Generate audio for the book/doc
# --------------------------------

audioGenerator = AudioGenerator(audio_output_path="audio")
audioGenerator.generateAudio(chunks)

# --------------------------------
# Merge generated mp3 files together
# --------------------------------

audioMerger = AudioMerger(audio_folder="audio")
audioMerger.merge_audio_files()
