# audiobook-generator
audiobook generator that uses PyMuPDF, pydub and OpenAI TTS API 
It is not finished yet but the main functionality is pretty much done.
How it works:
Read the pdf or epub using PyMuPDF
Get table of contents using PyMuPDF
Then it processes each chapter by splitting them into chunks that will fit OpenAIs token limit
Then for each chunk of each chapter audio is generated
and using pydub I merge the audio together for each chapter

(This is still WIP as I ran out of api credits to properly finish generating the whole book :|, but I did get about an hour of audio and it was fine.) 
