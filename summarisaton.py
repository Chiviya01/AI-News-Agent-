from langchain_core.tools import tool
from langchain_groq import ChatGroq
import os
import getpass

if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = getpass.getpass("Enter your Groq API key: ")

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

text = "this is long and verbose! Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
messages = [
      (
         "system",
         "You are a helpful news summariser. Summarise the user text in a concise manner.",
      ),
      ("human", text),
]
ai_msg = llm.invoke(messages)



print(ai_msg.content)


   