import os

from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

from genai.output_parsers import summary_parser
from genai.third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

def ice_break_with(name: str) -> str:
    linkedin_url = linkedin_lookup_agent(name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_url)
    summary_template = """
            given the LinkedIn information {information} about a person from I want you to create: 
            1. a short summary. 
            2. two interesting facts about them.
            
            \n{format_instructions}
        """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={"format_instructions": summary_parser.get_format_instructions()}
    )
    # llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    llm = ChatOllama(model="llama3.2")
    # llm = ChatOllama(model="mistral")
    # This is LangChain expression language (LCEL)
    chain = summary_prompt_template | llm | summary_parser
    # chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    result = chain.invoke(input={"information": linkedin_data})
    print(result)
    # TODO: having error on parsing tavily
    # langchain_core.exceptions.OutputParserException: Failed to parse Summary from completion {"properties": {"summary": {"description": "A short summary of Angel Romero's professional and personal life.", "title": "Summary", "type": "string"}, "facts": {"description": "Two interesting facts about Angel Romero.", "items": {"type": "string"}, "title": "Facts", "type": "array"}}, "required": ["summary", "facts"]}. Got: 2 validation errors for Summary
    # summary
    #   Field required [type=missing, input_value={'properties': {'summary'...': ['summary', 'facts']}, input_type=dict]

if __name__ == "__main__":
    load_dotenv(dotenv_path=".env")
    print("Ice Breaker")
    ice_break_with(name=os.environ['INPUT_QUERY'])