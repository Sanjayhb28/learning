from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
import os

information = """ Elon Reeve Musk FRS is a businessman, known for his leadership of Tesla, SpaceX, X (formerly Twitter), and the Department of Government Efficiency (DOGE). Musk has been the wealthiest person in the world since 2021; as of May 2025, Forbes estimates his net worth to be US$424.7 billion.

Born to a wealthy family in Pretoria, South Africa, Musk emigrated in 1989 to Canada. He received bachelor's degrees from the University of Pennsylvania in 1997 before moving to California, United States, to pursue business ventures. In 1995, Musk co-founded the software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company that later merged to form PayPal, which was acquired by eBay in 2002. That year, Musk also became an American citizen."""

if __name__ == "__main__":
    load_dotenv()

    summary_template = """Given he information {information} abtout a person I want you to create, 
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
        # other params...
    )

    chain = summary_prompt_template | llm

    ai_msg = chain.invoke(input={"information": information})
    print(ai_msg)

    # print(ai_msg.content)
