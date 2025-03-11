from dotenv import load_dotenv

from tools.tools import get_profile_url_tavily

load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor
)
from langchain import hub

def lookup(name: str):
    llm = ChatGoogleGenerativeAI(
        temperature=0,
        model="gemini-2.0-flash"
    )
    template = """given the full name {name_of_person}I want you to get me a link to their LinkedIn Profile
                            Your answer should contain the URL only"""
    prompt_template = PromptTemplate(
        template = template, variables = ["name_of_person"]
    )  
    tools_for_agent = [
        Tool(
            name = "Crawl Google 4 LinkedIn Profile Page",
            func=get_profile_url_tavily,
            description="Useful for when you need to get the Linkedin pgae URL"
        )
    ]
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(tools=tools_for_agent, prompt=react_prompt, llm=llm)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result =  agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linkedInUrl = result["output"]
    return linkedInUrl

if __name__ == "__main__":
    linkedInUrl = lookup(name="Shasank Periwal")
    print(linkedInUrl)