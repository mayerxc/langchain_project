import os
from dotenv import load_dotenv

# from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-3.5-turbo"
# OPENAI_MODEL = "gpt-4"


def main():
    # llm = OpenAI(openai_api_key=OPENAI_API_KEY)
    # prompt = input("Please provide a prompt: ")
    # result = llm.predict(prompt)
    # print(result)

    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model=OPENAI_MODEL)
    prompt = input("Please provide a prompt: ")
    result = llm.predict(prompt)
    print(result)


if __name__ == "__main__":
    main()
