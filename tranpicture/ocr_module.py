import cv2
import pytesseract

def image_to_text(image_path, lang='eng'):
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Không tìm thấy file ảnh: {image_path}")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    gray = cv2.medianBlur(gray, 3)
    config = "--oem 3 --psm 6"
    text = pytesseract.image_to_string(gray, lang=lang, config=config)
    return text
