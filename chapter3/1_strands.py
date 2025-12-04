from strands import Agent
from dotenv import load_dotenv

load_dotenv()

agent = Agent("us.anthropic.claude-3-7-sonnet-20250219-v1:0")
agent("Strandsってどういう意味？")