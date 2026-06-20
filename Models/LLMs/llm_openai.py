from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

#model choose kar rahe hai, kon sa use karna hai
llm = OpenAI(model = 'model_name')

#envoke function model se response generate karwata hai 
#response ko result variable mein store kar
result = llm.invoke("What is the Date today")

#result print karwa diya
print(result)