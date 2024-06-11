from PyPDF2 import PdfReader


def get_annotations_with_urls(pdf_path):
    reader = PdfReader(pdf_path)

    annotations = []

    for page in reader.pages:
        for annotation in page['/Annots']:
            annotation_content = annotation.get_object()

            if annotation_content['/A']['/URI'] is not None:
                annotations.append({
                    "page_num": 0,
                    "rect": annotation_content["/Rect"],
                    "uri": annotation_content['/A']['/URI']
                })

    return annotations
