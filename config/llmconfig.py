import os
from autogen import Agent, ConversableAgent

teachable_base_config = {
    "model": "gpt-4-1106-preview",
    "temperature": 0,
    "api_key": os.getenv("OPENAI_API_KEY"),
    "seed": 1,
}

anxiety_coach_config = {
    "model": "gpt-4-1106-preview",
    "api_key": os.getenv("OPENAI_API_KEY"),
    "check_every_ms": 2000,
    "tools": ["code_interpreter", "knowledge_retreival"],
    "file_ids": "'C:\\users\\abehl\\agentswarm2\\config\\katy_background.md'",
}

gpt4_std_config = {
    "model": "gpt-4",
    "api_key": os.getenv("OPENAI_API_KEY"),
    "temperature": 0,
    "seed": 1,
}
