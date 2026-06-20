from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

#model choose kar rahe hai, kon sa use karna hai
chatmodel = ChatOpenAI( model = 'model_name', temperature = 0, max_completion_tokens=200)

#envoke function model se response generate karwata hai 
#response ko result variable mein store kar
result = chatmodel.invoke("Hi how are you")

#result printed
print(result)

#the result contains the meta data as well with the content response
print(result.content)
#this will only print the actual response
