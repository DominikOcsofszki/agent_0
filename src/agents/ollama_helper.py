from langchain_ollama import ChatOllama
from icecream import ic

llm_ollama = ChatOllama(
    model="llama3.2",
    temperature=0,
)


# def p(res):
#     # res = llm.invoke("Who are you ")
#     for entry in res:
#         print(entry)


#
# from langchain_core.prompts import ChatPromptTemplate
#
# prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             "You are a helpful assistant that translates {input_language} to {output_language}.",
#         ),
#         ("human", "{input}"),
#     ]
# )
#
# chain = prompt | llm
# res = chain.invoke(
#     {
#         "input_language": "English",
#         "output_language": "German",
#         "input": "I love programming.",
#     }
# )
# p(res)
