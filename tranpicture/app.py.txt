# File: app.py
import streamlit as st
import tempfile
from ocr_module import image_to_text

st.set_page_config(page_title="OCR Ảnh thành Văn bản", layout="centered")

st.title("🖼️➡️📝 Chuyển Hình ảnh Thành Văn bản")

uploaded_file = st.file_uploader("📤 Chọn file ảnh để nhận dạng văn bản:", type=["jpg", "jpeg", "png", "bmp", "tiff"])

lang = st.selectbox("🌐 Chọn ngôn ngữ nhận dạng:", options=["eng", "vie"], format_func=lambda x: "Tiếng Anh" if x=="eng" else "Tiếng Việt")

if uploaded_file is not None:
    # Lưu file tạm thời
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    with st.spinner('🔍 Đang nhận dạng...'):
        try:
            result_text = image_to_text(tmp_path, lang=lang)
            st.success("✅ Nhận dạng thành công!")
            st.text_area("📋 Kết quả văn bản:", value=result_text, height=300)
        except Exception as e:
            st.error(f"Lỗi: {e}")

    # Cho phép tải kết quả về file txt
    st.download_button(
        label="📥 Tải kết quả về (.txt)",
        data=result_text,
        file_name="ocr_result.txt",
        mime="text/plain"
    )
