from langchain_core.prompts import PromptTemplate
# from langchain_openai import ChatOpenAI
from langchain_core.output_parsers.string import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
import os
from agents.linkedin_lookup_agent import lookup
from third_parties.linkedin import scrape_linkedin_profile

def ice_break_with(name: str):
    linkedin_url = lookup(name)
    linkedInData = scrape_linkedin_profile(url=linkedin_url)
    
    summary_template = """
        Given the LinkedIn information {information} about a person from I want you to create
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    llm = ChatGoogleGenerativeAI(temperature= 0, model="gemini-2.0-flash")
    # download ollama, ollama run llama3
    # llm = ChatOllama(model="llama3")

    chain = summary_prompt_template | llm | StrOutputParser()
    # linkedInData = scrape_linkedin_profile(url="", mock=True)
    res = chain.invoke(input={"information":linkedInData})

    print(res)



if __name__ == '__main__':
    print("Breaking Ice")
    ice_break_with(name="Nikit Periwal")
  