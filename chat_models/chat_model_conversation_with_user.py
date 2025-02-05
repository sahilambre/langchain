from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatOpenAI(model='gpt-3.5-turbo')

chat_history = []

system_message = SystemMessage(content='You are a helpful ai assistant')

while True:
    query = input("You: ")
    if query.lower() == 'exit':
        break
    chat_history.append(HumanMessage(content=query))

    #getting ai response using history
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))

    print(f"AI: {response}")

print("Conversation Ended")