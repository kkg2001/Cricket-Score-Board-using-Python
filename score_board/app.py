import streamlit as st
import subprocess

st.title("Cricket Score Card Web Application")

if st.button("Generate Cricket Scores"):
    result=subprocess.run(["python","main.py"],capture_output=True,text=True)
    st.code(result.stdout)