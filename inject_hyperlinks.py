
from extract_text_position import extract_text_with_positions
from get_annotations import get_annotations_with_urls


def format_text_with_hyperlinks(pdf_path):
    annotations = get_annotations_with_urls(pdf_path)
    text_positions = extract_text_with_positions(pdf_path)

    formatted_text = ""
    next_element = "["

    for text in text_positions:
        for annotation in annotations:
            rect = annotation["rect"]

            if (
                rect[0] <= text["x0"]
                and text["x1"] <= rect[2]
                and rect[1] <= text["y0"]
                and text["y1"] <= rect[3]
                and next_element == "["
            ):
                formatted_text += next_element
                next_element = "]"

            if (
                text["x1"] >= rect[2]
                and text["y1"] >= rect[3]
                and next_element == "]"
            ):
                formatted_text = formatted_text + next_element
                formatted_text += f"({annotation['uri']})"
                next_element = "["

        formatted_text += text["text"]

    return "".join(formatted_text)
