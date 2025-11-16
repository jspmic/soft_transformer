import openpyxl


class Converter:
    def __init__(self, path: str) -> None:
        self.file_path = path
        self.workbook = openpyxl.load_workbook(self.file_path)
        self.sheet = self.workbook.active
        self.rows = self.workbook.max_row
        self.columns = self.workbook.max_column


if __name__ == "__main__":
    exit(0)
