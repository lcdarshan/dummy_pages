from dotenv import load_dotenv
load_dotenv() # loading all the environment variables
 
import streamlit as st
import os
import google.generativeai as genai
 
Api_key="AIzaSyCXcRs39a4Si3_vJBZSW69KS0x62YWXZSs"
genai.configure(api_key=Api_key)
 
# function to load gemini pro model and responces
model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text
 
#initialize our streamlip application
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")
 
# User input
input = st.text_area("Input:", height=None)

#submit button
submit=st.button("Ask the question")
 
if submit:
    response=get_gemini_response(input)
    st.subheader("Response:")
    st.write(response)




# # Loop for asking questions
# for i in range(10):
# # User input
#     input = st.text_area("Input:", height=None)

# #submit button
#     submit=st.button("Ask the question")
 
#     if submit:
#         response=get_gemini_response(input)
#         st.subheader("Response:")
#         st.write(response)