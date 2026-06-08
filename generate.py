from fastapi import APIRouter
from chains import chain
from models import PromptRequest

router = APIRouter()

@router.post("/generate")
async def generate_prompt(data: PromptRequest):

    result = chain.invoke(
        {
            "content_type": data.content_type,
            "platform": data.platform,
            "user_prompt": data.user_prompt,
            "environment": data.environment or "",
            "lighting": data.lighting or "",
            "camera": data.camera or "",
            "style": data.style or "",
            "strength": data.strength,
        }
    )

    return {
        "prompt": result.content
    }