import os
import autogen
from autogen.agentchat.contrib.gpt_assistant_agent import GPTAssistantAgent
from autogen.agentchat.contrib.multimodal_conversable_agent import (
    MultimodalConversableAgent,
)
from autogen.agentchat.contrib.teachable_agent import TeachableAgent
from autogen import UserProxyAgent, AssistantAgent, ConversableAgent
from autogen import ChatCompletion, GroupChat, GroupChatManager
from config.system_messages import anxiety_coach_prompt, word_assistant_prompt, excel_assistant_prompt, ppt_assistant_prompt
from config.llmconfig import anxiety_coach_config, gpt4_std_config

code_executor = autogen.UserProxyAgent(
    name="code_executor",
    code_execution_config={
        "work_dir": os.getcwd(),
        "use_docker": False,
    },
)

anxiety_coach = GPTAssistantAgent(
    name="anxiety_coach",
    instructions=anxiety_coach_prompt,
    llm_config=anxiety_coach_config,
)

# ------------DESKTOP TEAM----------------
# Microsoft Office Python AI
# Google Account Python AI
# Google Drive Python AI
# Code Action Debugger
# Code Executor
# Google Calendar
# Overseer/Report Generator

word_assistant = AssistantAgent(
    name="Microsoft_Word_Assistant",
    system_message=word_assistant_prompt,
    llm_config=gpt4_std_config,
    human_input_mode="NEVER",
    max_consecutive_auto_reply=4,
)

excel_assistant = AssistantAgent(
    name="Microsoft_Excel_Assistant",
    system_message=excel_assistant_prompt,
    llm_config=gpt4_std_config,
    human_input_mode="NEVER",
    max_consecutive_auto_reply=4,
)

ppt_assistant = AssistantAgent(
    name="Microsoft_Excel_Assistant",
    system_message=ppt_assistant_prompt,
    llm_config=gpt4_std_config,
    human_input_mode="NEVER",
    max_consecutive_auto_reply=4,
)
# Setup Google Drive tool
google_drive_assistant = 


