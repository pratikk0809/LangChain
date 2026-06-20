import os
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY"),
)

messages =[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about Langchain in 50 words')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)