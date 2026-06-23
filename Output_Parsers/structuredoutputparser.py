# import os
# from dotenv import load_dotenv

# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import PromptTemplate
# # from langchain_classic.output_parsers.structured import StructuredOutputParser, ResponseSchema

# load_dotenv()

# # Initialize model
# model = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",
#     api_key=os.getenv("GOOGLE_API_KEY"),
# )

# # Define response schema
# response_schemas = [
#     ResponseSchema(name="fact_1", description="Fact 1 about the topic"),
#     ResponseSchema(name="fact_2", description="Fact 2 about the topic"),
#     ResponseSchema(name="fact_3", description="Fact 3 about the topic")
# ]

# # Create parser
# parser = StructuredOutputParser.from_response_schemas(response_schemas)

# # Prompt template
# template = PromptTemplate(
#     template='Give 3 facts about {topic} \n{format_instructions}',
#     input_variables=["topic"],
#     partial_variables={"format_instructions": parser.get_format_instructions()}
# )

# # Create prompt
# prompt = template.invoke({"topic": "spiderman"})

# # Invoke model
# result = model.invoke(prompt)

# # Parse structured output
# final_result = parser.parse(result.content)

# print(final_result)
