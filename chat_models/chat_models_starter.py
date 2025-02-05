# print('Hello Langchain')

# chat model in langchain is a component designed to communicate in a strucutred way with the LLMs like GPT-4, huggingface, etc.

# Why use langchain chat models?
# -> consistent worlflow
# -> easy switching between the llms
# -> context management
# -> efficient chaining and scalability

from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model='gpt-3.5-turbo',
)

# llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

result = llm.invoke('What is the current time in new york EST?')

print(result)