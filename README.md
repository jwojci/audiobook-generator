# audiobook-generator
audiobook generator that uses PyMuPDF, pydub and OpenAI TTS API </br>
It is not finished yet but the main functionality is pretty much done. </br>
How it works: </br>
Read the pdf or epub using PyMuPDF </br>
Get table of contents using PyMuPDF </br>
Then it processes each chapter by splitting them into chunks that will fit OpenAIs token limit </br>
Then for each chunk of each chapter audio is generated </br>
and using pydub I merge the audio together for each chapter </br> </br>

(This is still WIP as I ran out of api credits to properly finish generating the whole book :|, but I did get about an hour of audio and it was fine.) </br>
