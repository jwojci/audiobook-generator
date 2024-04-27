from pydub import AudioSegment
import os


class AudioMerger:
    def __init__(self, audio_folder) -> None:
        self.audio_folder = audio_folder

    def merge_audio_files(self):
        """Merges audio chunks of each chapter into one for each chapter"""
        audio_segments = []
        audio_merged = 0
        audio_path = self.audio_folder
        for dir in os.listdir(audio_path):
            for chapter in os.listdir(os.path.join(audio_path), dir):
                for file in chapter:
                    audio_segments.append(
                        AudioSegment.from_file(
                            os.path.join(audio_path, dir, file), "mp3"
                        )
                    )

                for audio in audio_segments:
                    audio_merged += audio

            audio_merged.export(f"{chapter}.mp3", format="mp3")
