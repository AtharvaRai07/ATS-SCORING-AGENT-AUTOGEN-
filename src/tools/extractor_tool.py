import pdfplumber
import docx
import mimetypes


class FileTextExtractor:
    """Extract text from PDF, DOCX, or TXT files without textract."""

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.file_type, _ = mimetypes.guess_type(file_path)

    def extract_text(self) -> tuple[str, str]:
        """Extract text and return (file_type, text_content)."""
        if self.file_type == 'application/pdf':
            return self.file_type, self._extract_pdf()
        elif self.file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            return self.file_type, self._extract_docx()
        elif self.file_type == "text/plain":
            return self.file_type, self._extract_txt()
        else:
            raise ValueError(f"Unsupported file type: {self.file_type}")

    def _extract_pdf(self) -> str:
        with pdfplumber.open(self.file_path) as pdf:
            text = "\n".join(page.extract_text() or "" for page in pdf.pages)
        return text.strip()

    def _extract_docx(self) -> str:
        doc_file = docx.Document(self.file_path)
        text = "\n".join(para.text for para in doc_file.paragraphs)
        return text.strip()

    def _extract_txt(self) -> str:
        with open(self.file_path, "r", encoding="utf-8") as f:
            text = f.read()
        return text.strip()
