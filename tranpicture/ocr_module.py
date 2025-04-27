import easyocr

def image_to_text(image_path, lang='en'):
    reader = easyocr.Reader([lang], gpu=False)
    results = reader.readtext(image_path, detail=0)
    return "\n".join(results)
