import os
from dotenv import load_dotenv
from langchain_classic.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from prompt import SYSTEM_PROMPT
from langchain_classic.schema import AIMessage, HumanMessage, SystemMessage

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

llm =ChatGroq(model="llama-3.1-8b-instant", api_key=groq_api_key)

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        (
            "human",
            """
Content Type: {content_type}

Platform: {platform}

Prompt: {user_prompt}

Environment: {environment}

Lighting: {lighting}

Camera: {camera}

Style: {style}

Prompt Strength: {strength}

Generate the final prompt.
"""
        )
    ]
)

chain = prompt_template | llm