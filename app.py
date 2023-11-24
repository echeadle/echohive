import os
from dotenv import load_dotenv, find_dotenv
from autogen import UserProxyAgent, AssistantAgent

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Add your autogen agent imports here
# For example:

config_list = [
     {
        "model": "gpt-3.5-turbo-1106",
        "api_key":  os.getenv("OPENAI_API_KEY")
    },  
     {
        "model": "gpt-3.5-turbo",
        "api_key": os.getenv("OPENAI_API_KEY")
    },  
]


llm_config={
    "request_timeout": 600,
    "seed": 42,
    "config_list": config_list,
    "temperature": 0,
}

assistant = AssistantAgent(
    name="assistant",
    llm_config=llm_config,
)

user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web", "use_docker": False},
)

user_proxy.initiate_chat(
    assistant,
    message="""What is the date today?   Compare the year-to-date gain for META and TESLA."""  
)

user_proxy.send(
    recipient=assistant,
    message="""Plot a chart of their stock price change YTD and save the python file and save the plot to stock_price_ytd.png."""
)