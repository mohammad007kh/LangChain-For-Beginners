import streamlit as st
import os
from langchain.chat_models import ChatOpenAI
from langchain_community.utilities import WikipediaAPIWrapper
import serpapi


st.set_page_config(page_title="دستیار هوشمند فارسی با LangChain", page_icon="🤖")
st.title("🧠 دستیار هوشمند فارسی با LangChain")
st.markdown("""
<div dir="rtl" align="right">
این اپلیکیشن سه ابزار دارد:
- ماشین حساب
- جستجوی ویکی‌پدیا
- جستجوی گوگل با ترجمه خودکار

سؤال خود را به فارسی وارد کنید و ابزار مناسب به طور خودکار انتخاب می‌شود.
</div>
""", unsafe_allow_html=True)

# User input for API keys
st.sidebar.header("API Keys")
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
serpapi_api_key = st.sidebar.text_input("SerpAPI Key", type="password")

# Set environment variables for libraries that require them
if openai_api_key:
    os.environ["OPENAI_API_KEY"] = openai_api_key
if serpapi_api_key:
    os.environ["SERPAPI_API_KEY"] = serpapi_api_key

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
serp_client = serpapi.Client(api_key=serpapi_api_key)
wikipedia = WikipediaAPIWrapper()

def calculator(expression: str) -> str:
    try:
        return str(eval(expression))
    except Exception as e:
        return f"خطا: {e}"

def persian_google_search(query_fa: str) -> str:
    translation_prompt = f"Translate this Persian question to English (just the translation):\n{query_fa}"
    translated_query = llm.invoke(translation_prompt).content.strip()
    result = serp_client.search(
        engine="google",
        q=translated_query,
        location="United States",
        hl="en",
        gl="us",
        num=5
    )
    organic_results = result.get("organic_results", [])
    english_summary = "\n".join(f"- {r.get('title')}: {r.get('snippet')}" for r in organic_results if r.get("snippet"))
    if not english_summary:
        return "نتیجه‌ای یافت نشد."
    summary_prompt = f"Please translate this English text to Persian:\n{english_summary}"
    translated_answer = llm.invoke(summary_prompt).content.strip()
    return translated_answer

def wikipedia_search(query: str) -> str:
    return wikipedia.run(query)



query = st.text_input("سؤال خود را به فارسی وارد کنید:")

def route_tool(query_fa: str):
    routing_prompt = (
        "You are a smart Persian assistant. "
        "Choose the best tool for the user's question, or answer directly if no tool is needed. "
        "Available tools: ماشین حساب (calculator), ویکی‌پدیا (wikipedia), جستجوی گوگل با ترجمه خودکار (google_search), پاسخ مستقیم (direct_answer). "
        "Return ONLY the tool name (calculator, wikipedia, google_search, direct_answer) and nothing else."
        f"\nQuestion: {query_fa}"
    )
    tool_name = llm.invoke(routing_prompt).content.strip().lower()
    if "calculator" in tool_name:
        answer = calculator(query_fa)
        service = "ماشین حساب (Calculator)"
    elif "wikipedia" in tool_name:
        answer = wikipedia_search(query_fa)
        service = "ویکی‌پدیا (Wikipedia)"
    elif "google_search" in tool_name:
        answer = persian_google_search(query_fa)
        service = "جستجوی گوگل با ترجمه خودکار (Google Search)"
    elif "direct_answer" in tool_name or "پاسخ مستقیم" in tool_name:
        answer = llm.invoke(query_fa).content.strip()
        service = "پاسخ مستقیم از مدل زبانی (Direct LLM Answer)"
    else:
        answer = "ابزار مناسب پیدا نشد. لطفاً سؤال خود را واضح‌تر وارد کنید."
        service = "نامشخص (Unknown)"
    return answer, service

if st.button("دریافت پاسخ") and query:
    with st.spinner("در حال پردازش..."):
        answer, service = route_tool(query)
        st.markdown(f"<div dir='rtl' align='right'><b>پاسخ:</b><br>{answer}<br><br><b>سرویس استفاده‌شده:</b> {service}</div>", unsafe_allow_html=True)
