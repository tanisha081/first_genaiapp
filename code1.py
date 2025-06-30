from langchain.chat_models import AzureChatOpenAI
import os
from dotenv import load_dotenv 
import streamlit as st 
import streamlit.components.v1 as components 

load_dotenv()

llm=AzureChatOpenAI(
    openai_api_base=os.getenv("AZURE_OPENAI_API_BASE"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    model_name="gpt-4o",
    temperature=0.7,
)

st.write("## Azure OpenAI Chatbot")

while True:
    user_input = st.text_input("You: ", key="user_input")
    if user_input:
        result = llm.invoke(user_input)
        st.write(f"**Bot:** {result.content}")
        # Clear the input field after processing
        st.session_state.user_input = ""
        print(result.content)

# result=llm.invoke("where is MARWADI UNIVERSITY located? ")
