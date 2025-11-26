import google.generativeai as genai
import pandas as pd
from .ai_prompt import CHATBOT_SYSTEM

genai.configure(api_key="GOOGLE_API_KEY")
model = genai.GenerativeModel("gemini-2.0-flash")
def generate_chat_answer(df: pd.DataFrame, user_message: str) -> str:
    # Dataframe -> text
    data_text = df.head(50).to_string(index=False)

    prompt = f"""
{CHATBOT_SYSTEM}

DATASET:
{data_text}

PERTANYAAN USER:
{user_message}

JAWABAN:
    """

    response = model.generate_content([prompt])
    return response.text