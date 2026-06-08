from pydantic import BaseModel
from typing import Optional


class PromptRequest(BaseModel):
    content_type: str
    platform: str
    user_prompt: str

    environment: Optional[str] = None
    lighting: Optional[str] = None
    camera: Optional[str] = None
    style: Optional[str] = None

    strength: str = "professional"