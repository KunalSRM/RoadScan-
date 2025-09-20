import streamlit as st
from src.predict import predict_image
from PIL import Image

st.title("🛣️ RoadScan – Pothole Detection")
st.write("Upload a road image, and the AI will detect potholes.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg","png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("Detecting potholes...")
    
    # Save uploaded image temporarily
    temp_path = "temp.jpg"
    image.save(temp_path)
    
    results = predict_image(temp_path)
    st.image(f"predictions/{results.imgs[0].shape[1]}.jpg", caption="Detected Potholes")
