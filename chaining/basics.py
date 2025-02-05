from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a facts expert who knows facts about {animal}."),
        ("human", "Tell me {fact_count} facts."),
    ]
)

# Creating the combined chain using LangChain Expression Language (LCEL)
chain = prompt_template | model | StrOutputParser() #extracting the content from the response
# chain = prompt_template | model

# Run the chain
result = chain.invoke({"animal": "human", "fact_count": 1})

# Output
print(result)