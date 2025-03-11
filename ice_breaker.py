from langchain_core.prompts import PromptTemplate
# from langchain_openai import ChatOpenAI
from langchain_core.output_parsers.string import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
import os

from third_parties.linkedin import scrape_linkedin_profile

information = """
Ratan Naval Tata[a] (28 December 1937 – 9 October 2024) was an Indian industrialist and philanthropist. He served as the chairman of Tata Group and Tata Sons from 1991 to 2012 and he held the position of interim chairman from October 2016 to February 2017.[3][4] In 2000, he received the Padma Bhushan, the third highest civilian honour in India, followed by the Padma Vibhushan, the country's second highest civilian honour, in 2008.[5]
Ratan Tata was the son of Naval Tata, who was adopted by Ratanji Tata, son of Jamshedji Tata, the founder of the Tata Group. He graduated from Cornell University College of Architecture with a bachelor's degree in architecture.[6] He had also attended the Harvard Business School (HBS) Advanced Management program in 1975.[1] He joined the Tata Group in 1962,[7] starting on the shop floor of Tata Steel. He later succeeded J. R. D. Tata as chairman of Tata Sons upon the latter's retirement in 1991. During his tenure, the Tata Group acquired Tetley, Jaguar Land Rover, and Corus, in an attempt to turn Tata from a largely India-centric group into a global business.
Throughout his life, Tata invested in over 40 start-ups, primarily in a personal capacity, with additional investments through his firm, RNT Capital Advisors.
"""

if __name__ == '__main__':
    print("openai")
    
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
    linkedInData = scrape_linkedin_profile(url="https://www.linkedin.com/in/shasank-periwal/", mock=False)
    # linkedInData = scrape_linkedin_profile(url="", mock=True)
    res = chain.invoke(input={"information":linkedInData})

    print(res)