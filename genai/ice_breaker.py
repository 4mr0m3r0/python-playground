from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from openai import api_key

information = """
The Talmud is, after the Hebrew Bible, the central text of Rabbinic Judaism and the primary source of Jewish religious law (halakha) and Jewish theology. Until the advent of modernity, in nearly all Jewish communities, the Talmud was the centerpiece of Jewish cultural life and was foundational to "all Jewish thought and aspirations", serving also as "the guide for the daily life" of Jews. The Talmud includes the teachings and opinions of thousands of rabbis on a variety of subjects, including halakha, Jewish ethics, philosophy, customs, history, and folklore, and many other topics.

The Talmud is constituted by the Mishnah, a written compendium of the Oral Torah, and the Gemara, a commentary on the Mishnah and related Tannaitic writings. Sometimes, the word "Talmud" may only refer to the Gemara. This text is made up of 63 tractates, each covering one subject area. The language of the Talmud is Jewish Babylonian Aramaic. Talmudic tradition emerged and was compiled between the destruction of the Second Temple in 70 CE and the Arab conquest in the early seventh century. Traditionally, it is thought that the Talmud itself was compiled by Rav Ashi and Ravina II around 500 CE, although it is more likely that this happened in the middle of the sixth century.

The word Talmud commonly refers to the Babylonian Talmud (Talmud Bavli) and not the earlier Jerusalem Talmud (Talmud Yerushalmi).
"""

def loading_variable():
    load_dotenv(dotenv_path="./genai/.env")

def template():
    loading_variable()
    summary_template = """
        given the information {information} about a person from I want you to create: 
        1. a short summary. 
        2. two interesting facts about them.
    """
    prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    llm = ChatOpenAI(temperature=0, model_name="gpt-4o", api_key=os.environ['OPENAI_API_KEY'])
    chain = prompt_template | llm
    result = chain.invoke(input={"information": information})
    print(result)

template()