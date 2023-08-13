#This is a timer app that takes user input and sets the timer!

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


#set the title of the app and place it in the center:
# col1,col2,col3 = sl.columns(3)
# with col2:
#     sl.title("Pomodoro")

sl.markdown(
    """
<style>
h1 { text-align : center;
    color: white;
</style>
<h1>
Welcome to Pomodoro 
</h1>
    """,
    unsafe_allow_html=True
)

#taking user inputs:
sets = sl.number_input("Enter number of sets",min_value=1, max_value=4)
study_time = sl.time_input("Enter number of minutes you want to study", value= datetime.time(0,0,0), step = datetime.timedelta(seconds=1500))
break_time = sl.time_input("Enter number of minutes you want to take a break", value = datetime.time(0,0,0), step = datetime.timedelta(seconds = 300))

#calculating times in seconds:
study_time = study_time.hour*3600 + study_time.minute*60 + study_time.second
break_time = break_time.hour*3600 + break_time.minute*60 + break_time.second

#creating the start button:
cols = sl.columns(7)
with cols[3]:
    button =  sl.button("START")

#if the button is clicked:
if button:
    #create containers to display a messages1
    Message1   = sl.empty()
    
    #create the progress bar:
    bar = sl.progress(0)

    #create containers to display a messages2
    percentage = sl.empty()
    Message2   = sl.empty()
    
    #for each set:
    for set in range(sets):
        #creating study time:
        #changing the progress bar color
        sl.markdown(
            """
            <style>
                .stProgress > div > div > div >div {
                    background-color: red;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
        #displaying the message1:
        Message1.write(":red[Study Time]")

        #study time loop:
        lv = study_time//100
        for i in range(lv,study_time+lv,lv):
            #updating the progress:
            bar.progress(i//lv)

            #updating the percentage:
            percentage.write(str(i//lv)+"%")

            #updating the message2:
            if i//lv <25:
                Message2.write("Effort!")
            elif 25<=i//lv <50:
                Message2.write("We can do this!")
            elif 50<=i//lv <75:
                Message2.write("We are getting there!")
            elif 75<=i//lv<100:
                Message2.write("Almost there!")
            else:
                Message2.write("Great Job!")
            
            #setting sleep time:
            ts.sleep(lv)
        
        #creating break time:
        #changing the progress bar color
        sl.markdown(
            """
            <style>
                .stProgress > div > div > div >div {
                    background-color: green;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
        #displaying the message1:
        Message1.write(":green[Break Time!] :sunglasses:")

        #break time loop:
        lv = break_time//100
        for i in range(lv,break_time+lv,lv):
            #updating the progress:
            bar.progress(i//lv)

            #updating the percentage:
            percentage.write(str(i//lv)+"%")

            #updating the message2:
            if i//lv <25:
                Message2.write("Great job!")
            elif 25<=i//lv <50:
                Message2.write("Relax!")
            elif 50<=i//lv <75:
                Message2.write("Impressive!")
            elif 75<=i//lv<100:
                Message2.write("start warming up!")
            else:
                Message2.write("Effort!")
            #setting sleep time:
            ts.sleep(lv)
    
    #closing messages:
    Message1.write("You have finished the set")
    Message2.write("Congratulations!!")
    percentage.write("100%")
    bar.progress(100)

    sl.caption("click the button to restart the timer!")
            
#else prompt the user to start the timer
else:
    sl.caption("Click the start button to start the timer!")

