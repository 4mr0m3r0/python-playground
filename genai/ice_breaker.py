from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

from genai.third_parties.linkedin import scrape_linkedin_profile


def loading_variable():
    load_dotenv(dotenv_path="./genai/.env")

def template():
    loading_variable()
    summary_template = """
        given the LinkedIn information {information} about a person from I want you to create: 
        1. a short summary. 
        2. two interesting facts about them.
    """
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    # llm = ChatOpenAI(temperature=0, model_name="gpt-4o", api_key=os.environ['OPENAI_API_KEY'])
    llm = ChatOllama(model="llama3.2")
    # llm = ChatOllama(model="mistral")
    chain = summary_prompt_template | llm | StrOutputParser()
    linkedin_data = scrape_linkedin_profile()
    result = chain.invoke(input={"information": linkedin_data})
    print(result)

template()