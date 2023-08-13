
import streamlit as sl
import pandas as pd
import time as ts
import datetime

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

sl.markdown(
    """
    <h1 style = 'text-align:center;'>
    User Registration
    </h1>
    """,
    unsafe_allow_html=True
)

#method1 :  form object
form = sl.form("form1")
form.text_area("Tell a story")
form.form_submit_button("Submit")

#method2 :  with
with sl.form("form2"):
    col1,col2 = sl.columns(2)
    col1.text_input("First Name", placeholder="John",)
    col2.text_input("Last Name", placeholder="Doe")
    sl.text_input("Email Address", placeholder="johndoe@gmail.com")
    sl.text_input("Password")
    sl.text_input("Confirm Password")
    sl.form_submit_button("Submit")

