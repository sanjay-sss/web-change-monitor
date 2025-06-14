import os
import requests

def summarize_changes(changes):
    api_key = os.getenv("OPENAI_API_KEY")
    if not changes:
        return "No changes detected."
    
    try:
        # response = requests.post(
        #     "https://api.openai.com/v1/completions",
        #     headers={"Authorization": f"Bearer {api_key}"},
        #     json={
        #         "model": "gpt-3.5-turbo",
        #         "prompt": f"Summarize the following website changes: {changes}",
        #         "max_tokens": 100
        #     }
        # )
        # return response.json()['choices'][0]['text']
        
        return f"Summary: {changes[:200]}... (OpenAI response; replace with real API call)"
    except Exception as e:
        return f"Error summarizing changes: {str(e)}"