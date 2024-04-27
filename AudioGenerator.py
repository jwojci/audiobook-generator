from openai import OpenAI
import os


class AudioGenerator:
    def __init__(self, audio_output_path) -> None:
        self.audio_output_path = audio_output_path
        self.set_OpenAiClient()

    def set_OpenAiClient(self):
        self.openai_client = OpenAI()

    def generateAudio(self, chunks):
        chunk_num = 0
        for chapter_name in chunks:
            chapter_path = os.path.join(self.audio_output_path, chapter_name)
            if not os.path.exists(chapter_path):
                os.mkdir(chapter_path)

            for chunk in chunks[chapter_name]:
                with self.openai_client.audio.speech.with_streaming_response.create(
                    model="tts-1-hd",
                    voice="alloy",
                    input=chunk,
                ) as response:
                    response.stream_to_file(
                        f"{self.audio_output_path}/{chapter_path}/{chunk_num}.mp3"
                    )
                chunk_num += 1
