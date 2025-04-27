import easyocr

# Khởi tạo Reader một lần cho đỡ tốn tài nguyên
reader = easyocr.Reader(['en', 'vi'], gpu=False)

def image_to_text(image_path, lang='en'):
    results = reader.readtext(image_path, detail=0)
    return "\n".join(results)
