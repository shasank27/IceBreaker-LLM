from typing import Tuple
from langchain_core.prompts import PromptTemplate
# from langchain_openai import ChatOpenAI
from langchain_core.output_parsers.string import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
import os
from agents.linkedin_lookup_agent import lookup
from output_parsers import Summary, summary_parser
from third_parties.linkedin import scrape_linkedin_profile
from dotenv import load_dotenv
load_dotenv()

def ice_break_with(name: str)-> Tuple[Summary, str]:
    linkedin_url = lookup(name)
    linkedInData = scrape_linkedin_profile(url=linkedin_url)
    
    summary_template = """
        Given the LinkedIn information {information} about a person from I want you to create
        1. a short summary
        2. two interesting facts about them
    
        \n {format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], 
        template=summary_template,
        partial_variables={"format_instructions": summary_parser.get_format_instructions()}
    )
    llm = ChatGoogleGenerativeAI(temperature= 0, model="gemini-2.0-flash", verbose=True)
    # download ollama, ollama run llama3
    # llm = ChatOllama(model="llama3")

    chain = summary_prompt_template | llm | summary_parser
    # linkedInData = scrape_linkedin_profile(url="", mock=True)
    res:Summary = chain.invoke(input={"information":linkedInData})
    return res, linkedInData.get("profile_pic_url")



if __name__ == '__main__':
    print("Breaking Ice")
    print(ice_break_with(name="Nikit Periwal"))
  