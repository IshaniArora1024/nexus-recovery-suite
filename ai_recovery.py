from google import genai
from google.genai import types
import pandas as pd

# 1. Setup - Using the stable v1 endpoint and the latest 2026 model
client = genai.Client(
    api_key="AIzaSyDqRB4aepnPmHttvvB3TjeBqnLOrNSLh1s",
    http_options=types.HttpOptions(api_version='v1')
)

def generate_recovery(name, review):
    prompt = f"Customer: {name}. Review: '{review}'. Write a 2-sentence apology email with discount code: RESET20."
    
    # Update: Use gemini-2.5-flash, the current stable standard
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=prompt
    )
    return response.text

# 2. Run the test
print("--- CONNECTING TO STABLE GEMINI 2.5 ENGINE... ---")
try:
    draft = generate_recovery("Emma Watson", "The quality of the fabric has gone down.")
    print("\nSUCCESS! AI DRAFT:")
    print("-" * 30)
    print(draft)
except Exception as e:
    print(f"❌ Connection Error: {e}")