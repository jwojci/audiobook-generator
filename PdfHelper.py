import fitz


class PdfHelper:
    """Class for PDF related functions"""

    def __init__(self, read_file_path) -> None:
        self.file = read_file_path

    def get_doc(self):
        return fitz.open(self.file)

    def get_doc_path(self):
        return self.file
