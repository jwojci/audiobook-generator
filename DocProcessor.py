import nltk
import os


class DocProcessor:
    """Class for processing the document"""

    def __init__(self, doc, output_path) -> None:
        self.doc = doc
        if not os.path.exists(output_path):
            os.mkdir(output_path)
        self.output_path = output_path

    def write_chapter_contents(self, chapterPage, writer):
        """Gets document page and writes it to file"""
        text = self.doc.get_page_text(chapterPage).encode("utf8")
        writer.write(text)
        writer.write(bytes((12,)))

    def save_chapters(self):
        """Iterates through table of contents and saves every chapter to a separate file"""

        toc = self.doc.get_toc()
        for i in range(len(toc)):
            chapterPage = toc[i][2]

            if i + 1 < len(toc):
                nextChapterPage = toc[i + 1][2]
            else:
                nextChapterPage = None

            if nextChapterPage is not None:
                title = toc[i][1]
                title = title.replace(":", "")
                save_to = os.path.join(self.output_path, f"{title}.txt")
                with open(save_to, "wb") as out:
                    if (nextChapterPage - chapterPage) > 1:
                        for i in range(chapterPage - 1, nextChapterPage - 1):
                            self.write_chapter_contents(i, out)
                    else:
                        self.write_chapter_contents(chapterPage - 1, out)
            else:
                pass  # TODO: implement saving last pages

    def get_chapter_paths(self):
        """Returns an array with each chapters file path from the outputs directory"""
        file_paths = []
        outputs = sorted(
            os.listdir(self.output_path),
            key=lambda x: (
                int(x.split()[0]) if x.split()[0].isdigit() else float("inf"),
                x,
            ),
        )
        for file in outputs:
            file_paths.append(os.path.join(self.output_path, file))

        return file_paths

    def split_chapter(self, file_path, max_sentences_per_chunk=33):
        """Splits the chapter text into sentences
        and bundles them into chunks that fit OpenAI 4096 character limit"""

        with open(file_path, "r", encoding="utf-8") as file:
            chapter_text = file.read()

        sentences = nltk.sent_tokenize(chapter_text)
        chunks = []
        current_chunk = []

        for sentence in sentences:
            if len(current_chunk) < max_sentences_per_chunk:
                current_chunk.append(sentence)
            else:
                chunks.append(" ".join(current_chunk))
                current_chunk = [sentence]

        if current_chunk:
            chunks.append(" ".join(current_chunk))

        return chunks

    def split_chapters(self, chapter_paths):
        """Runs each chapter in chapter_paths through split_chapter function"""
        chapter_chunks = {}
        for path in chapter_paths:
            chapter_name = path.split(self.output_path + "\\")[1].split(".")[0]
            chunks = self.split_chapter(path)
            chapter_chunks[chapter_name] = chunks

        return chapter_chunks
