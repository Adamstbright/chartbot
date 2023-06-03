import openai

class Chatbot:
    """
    This class connect to the openAI API and return answer to query from
    the user.
    """
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response

if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about birds.")
    print(response)
