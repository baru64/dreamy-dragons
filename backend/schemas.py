from pydantic import BaseModel


class BaseMessage(BaseModel):
    """BaseMessage schema"""

    type: str
    content: dict
