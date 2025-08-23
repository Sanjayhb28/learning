from typing import List, Dict, Any
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser

class Summary(BaseModel):
    summary: str = Field(description="A short summary of the person.")
    interesting_facts: List[str] = Field(description="Interesting facts about the person.")

    # def to_dict(self):
    #     return {"summary": self.summary, "interesting_facts": self.interesting_facts}

summary_parser = PydanticOutputParser(pydantic_object=Summary)