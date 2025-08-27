from dotenv import load_dotenv
load_dotenv()

from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
# from langchain.agents.react.agent import create_react_agent
from langchain_google_genai import GoogleGenerativeAI
from langchain_tavily import TavilySearch

tools = [TavilySearch()]
llm = GoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
react_prompt = hub.pull("hwchase17/react")
agent = create_react_agent(llm, tools, prompt=react_prompt)
agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True)
chain = agent_executor

def main():
    result = chain.invoke({"input": "Who is Sarala H S DXC?"})
    print(result)
    # llm = GoogleGenerativeAI(model="gemini-pro", temperature=0)
    # agent = create_react_agent(llm, tools, verbose=True)
    # agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True)
    # response = agent_executor.invoke({"input": "What is the capital of France?"})
    # print(response)

if __name__ == "__main__":
    main()