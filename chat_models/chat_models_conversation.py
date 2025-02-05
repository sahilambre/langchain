from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model='gpt-3.5-turbo',
)

messages = [
    SystemMessage('You are an expert in social media strategy'),
    HumanMessage('Give a short tip to create engaging content on social media')
]

result = llm.invoke(messages)
print(result.content)