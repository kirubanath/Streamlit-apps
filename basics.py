import streamlit as sl
import pandas as pd

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
#to run the code use: python -m streamlit run <filename>.py
sl.code("python -m streamlit run main.py")

#to close the server: ctrl+c
sl.write("`to close the server : ctrl+c`")

################################################################################################
#Basic HTML elements:
sl.title("Streamlit application")
sl.subheader("subheader")
sl.header("This is a header")
sl.text("Alternate to the paragraph tag")

################################################################################################
sl.markdown("---")
#Markdown text:
sl.markdown("**Hello** *World*")
#for more reference the cheat sheet:
#https://www.markdownguide.org/cheat-sheet/

################################################################################################
sl.markdown("---")
#displaying a link:
url = "https://www.markdownguide.org/cheat-sheet/"
sl.markdown(f'Cheet seet: {url}')

#displaying link 2:
sl.markdown("[Google](https://www.google.com)")

################################################################################################
sl.markdown("---")
#writing a caption:
sl.caption("im a caption")

################################################################################################
sl.markdown("---")
#wrting latex: REMEMBER TO USE r for raw string
sl.markdown(f'''refer for latex : {"https://katex.org/docs/supported.html"}''')
sl.latex(r"a'")
sl.latex(r"\begin{bmatrix}a&b\\c&d\end{bmatrix}")

################################################################################################
sl.markdown("---")
#embedding json into the website:
#this will allow the user to copy the json to their clipboard!!
json = {"a":[1,2,3],"b":"hello"}#a dictionary
sl.json(json)

################################################################################################
sl.markdown("---")
#Emebdding code in the website:
#again this will allow the user to copy the code in their clipboard!!
code = """
print("This is a code for multiplication")
def fun(x,y):
    return x*y
"""
sl.code(code, language="python")

################################################################################################
sl.markdown("---")
#Write function :  swiss army knife! 
sl.markdown("[write function](https://docs.streamlit.io/library/api-reference/write-magic/st.write)")

sl.write("[emojis](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app)")
sl.write("hello *world!* :sunglasses:")
sl.write(pd.DataFrame(
    {'a':[1,2,3,4],'b':[5,6,7,8]}
))

################################################################################################
sl.markdown("---")
#creating metrics:
sl.metric(label="Car speed", value = "100ms⁻¹", delta = "-0.1ms⁻¹")

#creating table :  this can be done with the write function as well(alt to sl.dataframe)!
df = pd.DataFrame(
    {"col1":[1,2,3,4,5],
     "col2":[6,7,8,9,10]}
)
sl.table(df)#this is static!
sl.dataframe(df) #this allows us to order the elements!


################################################################################################
sl.write("---")
#Embedding audio, images and videos:
#image width scales both width and height!
sl.image("images.jpeg", caption = "example image", width = 500)

#auido:
sl.audio("Hamari Adhuri Kahani (Title Track)(PagalWorld.com.se).mp3")

#video:
sl.video("the-egyptian-pyramids-funny-animated-short-film-full-hd.mp4")

################################################################################################
sl.markdown("---")
#rerun button
if sl.button('Rerun'):
    sl.experimental_rerun()

################################################################################################
sl.markdown("---")
#interactive widget:

#1. checkbox
state = sl.checkbox("Check me")

if state:
    sl.write(":green[checked]") #:color[text here] gives the color to the text
else:
    sl.write(":red[check me please]")


def func1():
    print(sl.session_state.abc) #state of the checkbox by key reference 

state2 = sl.checkbox("checkbox2", value = True, on_change=func1, key = "abc")

#2. Radio buttons:
radio = sl.radio("Select one option", options=("opt1","opt2","opt3"))
sl.write(radio)

#3. button:
def func2():
    print("button clicked")
btn = sl.button("click me", on_click=func2)

#4. selectbox:
select = sl.selectbox("select one option", options=("opt1","opt2","opt3"))
#print(select)

#5. muliselect:
multiselect = sl.multiselect("select any number of options",  options=("opt1","opt2","opt3"))
#print(multiselect)
sl.write(multiselect)

#6. slider:
slider = sl.slider("this is a slider", min_value=-0.5, max_value=0.5,label_visibility="visible")
sl.write(slider)

select_slider = sl.select_slider("this is a select slider", options = ["low","medium","high"])
sl.write(select_slider)

#7. text input:
text = sl.text_input("enter a text:", max_chars=10, placeholder="max 10")
sl.write(text)

#8. number input:
number = sl.number_input("enter a number:", min_value=1, max_value=10)
sl.write(number)

#9. text area:
text_area = sl.text_area(":red[enter a text]",height=20,max_chars=100)

#10. date/time input:
date = sl.date_input("enter a date")
sl.write(date)

time_delta = sl.time_input("enter a time")
sl.write(time_delta)

#11. progress bar:
bar = sl.progress(0.6, text=":red[Progress bar]")

#12. sidebar:
#?

################################################################################################
sl.markdown("---")


