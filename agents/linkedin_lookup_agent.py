from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from dotenv import load_dotenv

from tools.tools import get_profile_url_tavily

load_dotenv()


def lookup(name: str) -> str:

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
        max_tokens=None,
        timeout=None
    )

    template = """Given the full name of a person {name}, I want you to find their linkedin profile url. 
    The answer should be a valid url or "Not found" if you cannot find it."""

    prompt_template = PromptTemplate(
        input_variables=["name"],
        template=template,
    )

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 LinkedIn Profile Page",
            func=get_profile_url_tavily,
            description="Useful for when you need to find the linkedin profile url of a person given their full name. The input to this tool should be a full name."
        )
    ]

    react_prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(
        llm=llm,
        tools=tools_for_agent,
        prompt=react_prompt
    )

    agent_executor = AgentExecutor.from_agent_and_tools(
        agent=agent,
        tools=tools_for_agent,
        verbose=True
    )

    result = agent_executor.invoke({"input": prompt_template.format_prompt(name= name)})

    return result['output']

if __name__ == "__main__":
    name = "Ruthvik P Thimmoji"
    print(lookup(name))
