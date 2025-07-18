[برای مشاهده توضیحات فارسی اینجا کلیک کنید.](#آموزش-لانگ-چین-برای-مبتدیان)


# LangChain for Beginners | لنگ‌چین برای مبتدیان

This repository contains a beginner-friendly, hands-on tutorial for learning LangChain with practical code samples, a Streamlit app, and explanations in Persian (Farsi).

---


## Folder Structure
```
LangChain-For-Beginners/
├─ README.md           # Main documentation
├─ LICENSE             # MIT license
├─ requirements.txt    # Python dependencies
├─ .env.example        # Sample API keys file
├─ notebooks/          # All Jupyter tutorial notebooks
│   ├─ 01_langchain_intro.ipynb
│   ├─ 02_langchain_agents.ipynb
│   ├─ 03_langchain_websearch_agent.ipynb
│   ├─ 04_langchain_groq.ipynb
│   ├─ 05_langchain_memory.ipynb
│   └─ 06_langchain_chains.ipynb
├─ streamlit/          # Streamlit apps for interactive demos
│   ├─ 01_langchain_intro_streamlit.py
│   └─ 03_langchain_websearch_agent_streamlit.py
├─ assets/             # Images and other assets
│   └─ images/
```

**Explanation:**
- `notebooks/`: Contains all step-by-step Jupyter notebooks for each episode.
- `streamlit/`: Interactive Streamlit apps for hands-on demos.
- `assets/images/`: Screenshots or visual assets (optional).
- `.env.example`: Template for API keys (copy and rename to `.env`).
- `requirements.txt`: All required Python packages for notebooks and apps.


## Quick Start
1. **Clone the repo:**
   ```bash
   git clone <repo-url>
   cd LangChain-For-Beginners
   ```
2. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```
   - The `requirements.txt` file is located in the root of the repository and contains all necessary Python packages for the notebooks and Streamlit app.
3. **Add your API keys:**
   - Create a `.env` file and add your keys (e.g. `OPENAI_API_KEY`, `GROQ_API_KEY`).
4. **Run a notebook or Streamlit app:**
   - Open notebooks in Jupyter/VS Code
   - Or run:
     ```bash
     streamlit run 01_langchain_intro_streamlit.py
     ```

---

## Requirements
- Python 3.9+
- langchain
- streamlit
- python-dotenv
- groq (if using Groq LLM)
- openai (if using OpenAI LLM)

---

## Episodes
- **Episode 1:** Step-by-step Jupyter notebook (`01_langchain_intro.ipynb`)
  - *Intro, setup, and basic LangChain usage.*
- **Episode 2:** Agents and tool-using assistant notebook (`02_langchain_agents.ipynb`)
  - *How to use tools and agents, with Persian responses.*
- **Episode 3:** Web search agent demo (`03_langchain_websearch_agent.ipynb`)
  - *Multi-tool agent demo, including Wikipedia and Google search.*
- **Episode 4:** Groq LLM demo (`04_langchain_groq.ipynb`)
  - *Switching LLM from ChatGPT to Groq (Mixtral, Llama3, etc.).*
- **Episode 5:** Memory in LangChain (`05_langchain_memory.ipynb`)
  - *How to use memory in chains and agents, with practical examples.*
- **Episode 6:** Chains in LangChain (`06_langchain_chains.ipynb`)
  - *Modern chain patterns, LCEL, and best practices for multi-step workflows.*

Other features:
- Explanations and code for prompt templates, chains, agents, memory, and more
- Right-to-left markdowns for Persian learners
- [YouTube Video Playlist for the Course](https://www.youtube.com/playlist?list=PLHSUcJ83dbdE_vTqh5ZweZaE-iC-a8flp)

---

## Troubleshooting
- **API Key Errors:** Make sure your `.env` file is present and keys are correct.
- **Package Issues:** Run `pip install -r requirements.txt` to install all dependencies.
- **Streamlit not found:** Install with `pip install streamlit`.
- **Other issues:** Check the Issues tab or open a new issue for help.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Credits
- Mohammad007kh (repo owner)
- LangChain team and contributors
- All viewers and contributors

---

## How to Run
- To run the notebooks: open them in Jupyter or VS Code.
- To run the Streamlit app:
  ```bash
  streamlit run 01_langchain_intro_streamlit.py
  ```

## Status
This tutorial is **still under development**. More content and improvements will be added soon!

---

Feel free to open issues or suggestions if you have feedback or requests.

---


# آموزش لنگ‌چین برای مبتدیان

این مخزن شامل آموزش ویدیویی، نوت‌بوک Jupyter و اپلیکیشن Streamlit برای یادگیری LangChain به زبان ساده و با مثال‌های عملی به زبان فارسی است. برای شروع سریع، کافیست مخزن را کلون کنید، پکیج‌ها را نصب کنید و کلیدهای API را در فایل `.env` قرار دهید.

---

## شروع سریع
۱. کلون کردن مخزن:
   ```bash
   git clone <repo-url>
   cd LangChain-For-Beginners
   ```
۲. نصب پکیج‌ها:
   ```bash
   pip install -r requirements.txt
   ```
۳. اضافه کردن کلیدهای API:
   - فایل `.env` بسازید و کلیدها را وارد کنید (مثلاً `OPENAI_API_KEY`، `GROQ_API_KEY`).
۴. اجرای نوت‌بوک یا اپلیکیشن Streamlit:
   - نوت‌بوک‌ها را در Jupyter یا VS Code باز کنید
   - یا اجرا کنید:
     ```bash
     streamlit run 01_langchain_intro_streamlit.py
     ```

---

## پیش‌نیازها
- پایتون ۳.۹ یا بالاتر
- langchain
- streamlit
- python-dotenv
- groq (در صورت استفاده از مدل Groq)
- openai (در صورت استفاده از مدل OpenAI)

---


## قسمت‌ها
- **قسمت ۱:** نوت‌بوک مرحله‌به‌مرحله (`01_langchain_intro.ipynb`)
  - *آشنایی اولیه و راه‌اندازی LangChain.*
- **قسمت ۲:** نوت‌بوک ایجنت‌ها و ابزارها (`02_langchain_agents.ipynb`)
  - *آشنایی با ابزارها و ایجنت‌ها، پاسخ فارسی.*
- **قسمت ۳:** دمو ایجنت جستجوی وب (`03_langchain_websearch_agent.ipynb`)
  - *دموی ایجنت چندابزاره شامل ویکی‌پدیا و جستجوی گوگل.*
- **قسمت ۴:** دمو مدل Groq (`04_langchain_groq.ipynb`)
  - *تعویض مدل زبانی از ChatGPT به Groq (Mixtral، Llama3 و ...).* 
- **قسمت ۵:** حافظه در LangChain (`05_langchain_memory.ipynb`)
  - *آموزش استفاده از حافظه در زنجیره‌ها و ایجنت‌ها با مثال عملی.*
- **قسمت ۶:** زنجیره‌ها در LangChain (`06_langchain_chains.ipynb`)
  - *الگوهای مدرن زنجیره‌سازی، LCEL و بهترین شیوه‌های ساخت جریان‌های چندمرحله‌ای.*

سایر امکانات:
- توضیحات و کد برای قالب‌های پرامپت، زنجیره‌ها، ایجنت‌ها و موارد دیگر
- توضیحات راست‌به‌چپ برای فارسی‌زبانان
- [ویدیوهای دوره در یوتیوب](https://www.youtube.com/playlist?list=PLHSUcJ83dbdE_vTqh5ZweZaE-iC-a8flp)

---

## رفع اشکال
- **خطاهای کلید API:** مطمئن شوید فایل `.env` وجود دارد و کلیدها صحیح هستند.
- **مشکلات پکیج:** دستور `pip install -r requirements.txt` را اجرا کنید.
- **Streamlit نصب نیست:** با دستور `pip install streamlit` نصب کنید.
- **سایر مشکلات:** بخش Issues را بررسی یا یک Issue جدید ثبت کنید.

---

## مجوز
این پروژه تحت مجوز MIT ارائه شده است. برای جزئیات بیشتر به فایل `LICENSE` مراجعه کنید.

## تقدیر و تشکر
- mohammad007kh (مالک مخزن)
- تیم LangChain و مشارکت‌کنندگان
- همه بینندگان و مشارکت‌کنندگان

---

<div align="center">
  <strong>Created with ❤️</strong>
</div>