import streamlit as st
import imageio as iio
import os

def app():

    st.markdown(
        """
        # MP4 to GIF Converter
        """
    )
    
    with st.form("Upload MP4 here"):
        uploaded_file = st.file_uploader("Choose a file")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            with open(uploaded_file.name, "wb") as f:
                f.write((uploaded_file).getbuffer())
            st.success("File Saved")
    
    reader = iio.get_reader(uploaded_file.name, format="FFMPEG")
    writer = []
    for im in reader:
        writer.append(im)
    iio.mimsave('converted.gif',writer)
    with open("converted.gif","rb") as file:
        btn = st.download_button(
            label = "Download GIF",
            data=file,
            file_name="Converted.gif",
        )
    
