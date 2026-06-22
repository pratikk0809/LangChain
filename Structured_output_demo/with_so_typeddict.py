import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY"),
)

#schema
class Review(TypedDict):
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["pos", "neg"], "Return the sentiment of the review"]
    pros: Annotated[Optional[list[str]], "Write down the pros mentioned in the review"]
    cons: Annotated[Optional[list[str]], "Write down the cons mentioned in the review"]

#model has the definition of schema
structured_model = model.with_structured_output(Review)

result = structured_model.invoke(""" The Hardware is great, but the software feels bloated. There are too manyn pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software upadate to fix this.""")

print(result)
print(result['summary'])
print(result['sentiment'])