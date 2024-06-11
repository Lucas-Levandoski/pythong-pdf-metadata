from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTAnno
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser


def extract_text_with_positions(pdf_path):
    laparams = LAParams()
    text_content = []

    with open(pdf_path, 'rb') as file:
        parser = PDFParser(file)
        document = PDFDocument(parser)

        rsrcmgr = PDFResourceManager()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        for page_num, page in enumerate(PDFPage.create_pages(document)):
            interpreter.process_page(page)
            layout = device.get_result()
            for element in layout:
                if isinstance(element, LTTextBox):
                    for line in element:
                        if isinstance(line, LTTextLine):
                            for char in line:
                                if isinstance(char, LTAnno):
                                    continue
                                text_content.append({
                                    "text": char.get_text(),
                                    "x0": char.x0,
                                    "y0": char.y0,
                                    "x1": char.x1,
                                    "y1": char.y1,
                                    "page_num": page_num
                                })
    return text_content
