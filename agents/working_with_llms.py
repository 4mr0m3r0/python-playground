"""
Working with LLMs in LangChain
Multiple providers, configuration, streaming, and cost optimization.
"""
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from openai import max_retries

load_dotenv()

def demo_init_chat_model():
    chat_model = init_chat_model(
        model="gpt-4o-mini",
        # model_provider="openai",
        temperature=0.7,
        streaming=True,
        max_retries=3,
    )
    response = chat_model.invoke("What is the capital of France? Answer in one word.")
    print(f"Response: {response.content}")

