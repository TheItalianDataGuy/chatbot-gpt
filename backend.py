from openai import OpenAI
import os


class Chatbot:
    def __init__(self):
        # Declare the api key
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def get_response(self, user_input):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.5,
            # if the temperature is closer to zero \
            # the answer will be more accurate but less diverse \
            # if it is closer to 1, the answer will be less accurate \
            # but more diverse
            messages=[
                {
                    "role": "system",
                    "content": f"{user_input}",
        }
            ]
        )
        return response.choices[0].message.content


if __name__ == "__main__":
    chatbot = Chatbot()
    answer = chatbot.get_response("Tell me a dad joke.")
    print(answer)
