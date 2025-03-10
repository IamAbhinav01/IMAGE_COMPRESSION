import streamlit as st
from PIL import Image
import io
st.title("Ai Powered Image Compression Tool")
uploaded_file = st.file_uploader("upload an image",type=["png","jpg","jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    output_io = io.BytesIO()
    image.save(output_io, format="JPEG", quality=20)  # Reduce quality to 20
    compressed_size = output_io.tell() / 1024  # Get size in KB

    st.success(f"✅ Compressed Image Size: {compressed_size:.2f} KB")
    st.download_button(
        label="Download Compressed Image",
        data=output_io.getvalue(),
        file_name="compressed_image.jpg",
        mime="image/jpeg"
    )