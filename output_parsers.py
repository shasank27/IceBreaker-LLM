from typing import List, Dict, Any
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

class Summary(BaseModel):
    summary: str = Field(description="summary")
    facts: str = Field(description="interesting facts about me")

    def to_dict(self):
        return {"summary": self.summary, "facts":self.facts}
    
summary_parser = PydanticOutputParser(pydantic_object=Summary)