import platform
import streamlit as st
import pytesseract
from PIL import Image

if platform.system()=="Windows":
  pytesseract.pytesseract.tesseract_cmd =r"C:\Program Files\Tesseract-OCR\tesseract.exe"


uploaded_file=st.file_uploader("Upload an Image",type=["jpg","png","jpeg"])

if uploaded_file:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",width=300)
    if st.button("Extract text"):
        text=pytesseract.image_to_string(image)
        st.text_area("Extracted text",text,height=200)
        st.download_button("Download",text,file_name="extracted.txt")
        pass
    pass
