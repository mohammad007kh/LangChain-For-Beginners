import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

import os

# Set Streamlit page config for RTL
st.set_page_config(page_title="تولید عنوان و توضیح", layout="centered")
st.markdown("""
    <style>
    body, .stApp { direction: rtl; text-align: right; font-family: Tahoma, Arial, sans-serif; }
    label, input, textarea, .stTextInput, .stTextArea, .stSelectbox, .stButton { direction: rtl; text-align: right; }
    </style>
    """, unsafe_allow_html=True)

st.title("تولید عنوان و توضیح")
st.write("این برنامه با استفاده از LangChain و مدل GPT-3.5-Turbo به شما کمک می‌کند برای آموزش‌های خود عنوان و توضیح کوتاه تولید کنید.")

# User input for API key
st.sidebar.header("API Key")
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

# Set environment variable for libraries that require it
if openai_api_key:
    os.environ["OPENAI_API_KEY"] = openai_api_key


# User inputs
col1, col2 = st.columns(2)
language = col1.selectbox("زبان", ["Persian", "English"], index=0)
tone_options = [
    "دوستانه / Friendly",
    "رسمی / Formal",
    "طنز / Funny",
    "الهام‌بخش / Inspirational"
]
tone = col2.selectbox("لحن پیام", tone_options, index=0)
message = st.text_area("موضوع یا پیام کوتاه آموزش", "آموزش LangChain برای مبتدیان")

generate = st.button("تولید عنوان و توضیح")

if generate:
    tone_map = {
        "دوستانه / Friendly": "friendly",
        "رسمی / Formal": "formal",
        "طنز / Funny": "funny",
        "الهام‌بخش / Inspirational": "inspirational"
    }
    tone_val = tone_map.get(tone, tone)

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.6)

    prompt_title = PromptTemplate(
        template="Generate a catchy tutorial title in {language} and in a {tone} tone for: {message}",
        input_variables=["tone", "message", "language"],
    )
    prompt_desc = PromptTemplate(
        template="Write a short description for a tutorial titled '{title}' in {language} and in a {tone} tone. The topic is: {message}",
        input_variables=["tone", "message", "language", "title"],
    )
    output_parser = StrOutputParser()
    title_chain = prompt_title | llm | output_parser
    desc_chain = (
        RunnablePassthrough.assign(title=title_chain)
        | prompt_desc
        | llm
        | output_parser
    )
    inputs = {"tone": tone_val, "language": language, "message": message}
    title = title_chain.invoke(inputs)
    description = desc_chain.invoke(inputs)
    st.subheader("عنوان پیشنهادی:")
    st.success(title)
    st.subheader("توضیح کوتاه:")
    st.info(description)
