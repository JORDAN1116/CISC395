import os
import openai
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# Search upward from trip_notes/ to find CISC395/.env
load_dotenv(find_dotenv())

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)
MODEL = "openrouter/free"

TRAVEL_SYSTEM_PROMPT = """
You are a knowledgeable and concise travel assistant focused on practical, budget-friendly advice for student travelers. 
Always name specific places (hostels, neighborhoods, eateries, transit routes) rather than offering generalities. 
Keep your responses strictly under 200 words.
"""

def ask(user_message: str, system_prompt: str = None, temperature: float = 0.7, max_tokens: int = 500) -> str | None:
    messages = []
    
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
        
    messages.append({"role": "user", "content": user_message})
    
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            timeout=30,
        )
        return response.choices[0].message.content
    except openai.AuthenticationError:
        print("\n[AI Error] Authentication failed. Please verify your OPENROUTER_API_KEY in the .env file.")
        return None
    except openai.RateLimitError:
        print("\n[AI Error] Rate limit exceeded. Please try again later.")
        return None
    except openai.APIConnectionError:
        print("\n[AI Error] Connection failed. Please check your network connection.")
        return None

if __name__ == "__main__":
    result = ask("What is the best time of year to visit Japan?", system_prompt=TRAVEL_SYSTEM_PROMPT)
    print(result)