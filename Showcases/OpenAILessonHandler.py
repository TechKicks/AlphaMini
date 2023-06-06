import openai
import json
import backoff

openai.api_key = "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"

class OpenAILessonHandler:

    index = 0

    def generateQuestions(self):
        print("Thinking of some awesome questions... Please wait at least 10 seconds...")

        # Generate questions
        subject = "dutch traditions"
        target_audience = "elementary school kids"

        request = "Please provide a JSON array of 5 strings each containing an interesting question about " + subject + " for " + target_audience + " in ascending order of difficulty in Dutch"
        messages = [{"role": "user", "content": request}]
        chat = self.makeRequest(messages)
        reply = chat.choices[0].message.content

        # Parse questions to JSON
        JSON_RAW = "[" + reply.split("[")[1]
        JSON_RAW = JSON_RAW.split("]")[0] + "]"
        JSON_DATA = json.loads(JSON_RAW)

        OpenAILessonHandler.index = 0;

        return JSON_DATA

    def isAnswerCorrect(self, user_answer, question):
        print("Antwoord aan het verwerken... Wacht een aantal seconden...")

        # See if user's answer is correct
        request = "Is \"" + user_answer + "\" a correct answer to the question \"" + question + "\"?"
        messages = [{"role": "user", "content": request}]
        chat = self.makeRequest(messages)
        reply = chat.choices[0].message.content

        return "yes" in reply.lower()

    @backoff.on_exception(backoff.expo, openai.error.RateLimitError)
    def makeRequest(self, messages):
        return openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
