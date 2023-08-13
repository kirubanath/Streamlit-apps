
import streamlit as sl
import pandas as pd 

sl.title("files upload")
################################################################################################
#codes to remove the hamburger icon the watermark
sl.markdown('''
<style>
.css-6q9sum.ef3psqc3{
            visibility:hidden;
}
.css-cio0dv.ea3mdgi1{
            visibility:hidden;
}         
</style>
''', unsafe_allow_html=True)

################################################################################################
sl.markdown("---")
uploader = sl.file_uploader("ipload a file here", type = ["mp3","mp4","jpeg"],accept_multiple_files=True)
if uploader is not None:
    for file in uploader:
        type = file.type.split("/")
        if type[0] == 'video':
            sl.video(file)
        elif type[0] == 'audio':
            sl.audio(file)
        elif type[0] == 'image':
            sl.image(file, width=500)

