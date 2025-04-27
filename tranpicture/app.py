import streamlit as st
import os
from ocr_module import image_to_text

st.set_page_config(page_title="OCR Hình Ảnh ➔ Văn Bản (EasyOCR)", layout="centered")
st.title("🖼️➡️📄 Chuyển Hình Ảnh thành Văn Bản (EasyOCR)")

uploaded_file = st.file_uploader("Tải lên ảnh (jpg, png,...)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Lưu file tạm
    with open("temp_image.png", "wb") as f:
        f.write(uploaded_file.read())
    
    st.image("temp_image.png", caption="Ảnh đã tải lên", use_container_width=True)

    lang = st.selectbox("Chọn ngôn ngữ OCR", ["en (English)", "vi (Tiếng Việt)"])
    lang_code = lang.split(" ")[0]

    if st.button("🧐 Thực hiện OCR"):
        with st.spinner("Đang nhận dạng..."):
            try:
                result_text = image_to_text("temp_image.png", lang=lang_code)
                st.success("🎉 Nhận dạng thành công!")
                st.text_area("Kết quả văn bản", result_text, height=300)
            except Exception as e:
                st.error(f"Lỗi: {str(e)}")
