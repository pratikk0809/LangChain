import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY"),
)

st.header('Research Tool')

paper_input = st.selectbox("Select Research Paper Name", ["Attention is All you Need", "BERT: Pre-training of Deep Bidirectional Transformers",
                           "GPT-3: Language Modes are Few-Shot Learners", "Diffusion Models beat GANs on Image Synthesis"])

style_input = st.selectbox("Select explanation style", [
                           "Beginner-Freindly", "technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explanation Length", [
                            "Short (1-2 Paragrapghs)", "Medium (3-5 Paragraphs)", "Long (detailed Explanation)"])


template = load_prompt('template.json')

#placeholders
prompt = template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
})

if st.button('Summarize'):
    result = model.invoke(prompt)
    st.write(result.content)
