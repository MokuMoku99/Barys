import openai
import time
import os

api = os.getenv('OPENAI_API_KEY')
if api is None:
    raise ValueError("API key is not set. Please set the OPENAI_API_KEY environment variable.")

openai.api_key = api
n = str(input("Input region: "))
def generate_response(text):
    max_attempts = 5
    wait_time = 60
    for attempt in range(max_attempts):
        try:
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo-0125',
                messages=[{"role": "user", "content": text}],
                max_tokens=100,
                temperature=0.7,
                n=1,
                timeout=15
            )
            return response['choices'][0]['message']['content'].strip()
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(wait_time)

if __name__ == "__main__":
    try:
        x = generate_response(f'Show us the amoun otf greenhouse emmisions in {n} region in the last couple of years. In short. Even sho')
        if x:
            print(x)
    except KeyboardInterrupt:
        print("\nOperation interrupted by the user.")