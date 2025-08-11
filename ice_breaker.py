from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
import os

from third_parties.linkedin import scrape_linkedin_profile


if __name__ == "__main__":
    load_dotenv()

    summary_template = """Given the linkedin information {information} abtout a person I want you to create, 
    1. A short summary of the person.
    2. Two interseting facts about them"""

    summary_prompt_template = PromptTemplate(
        input_variables=["informtion"],
        template=summary_template,
    )
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        langsmit_tracing = False
        # other params...
    )

    chain = summary_prompt_template | llm
    url = "https://gist.githubusercontent.com/emarco177/859ec7d786b45d8e3e3f688c6c9139d8/raw/5eaf8e46dc29a98612c8fe0c774123a7a2ac4575/eden-marco-scrapin.json"
    linkedin_data = scrape_linkedin_profile(url, mock=True)

    ai_msg = chain.invoke(input={"information": linkedin_data})
    print(ai_msg)

    # print(ai_msg.content)
