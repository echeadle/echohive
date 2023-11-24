from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# have your openai api key as an environment variable as OPENAI_API_KEY
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

# create an AssistantAgent instance named "assistant"
assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list}
                           
)

# create a UserProxyAgent instance named "user_proxy"
user_proxy = UserProxyAgent(name="user_proxy")

# the assistant receives a message from the user, which contains the task description
user_proxy.initiate_chat(
    assistant,
    message="""What date is today? Which big tech stock has the largest year-to-date gain this year? How much is the gain?""",
)