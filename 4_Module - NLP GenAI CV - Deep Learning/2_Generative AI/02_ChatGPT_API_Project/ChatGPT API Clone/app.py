from flask import Flask, render_template, request
import openai
import config

app = Flask(__name__)

openai.api_key = config.API_KEY

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/get')
def get_bot_response():
    userText = request.args.get('msg')
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=userText,
        max_tokens=1024,  # req + res
        n=1,
        stop=None,
        temperature=0.8
    )  ## send a request

    # print(response)
    answer = response["choices"][0]['text']
    return str(answer)

# question = input("Ask anything to ChatGPT...!!")

# response = openai.Completion.create(
#     engine="text-davinci-003",
#     prompt=question,
#     max_tokens=None,  # req + res
#     n=2,
#     stop=None,
#     temperature=0.8
# )  ## send a request

# # print(response)
# answer = response["choices"][0]['text']
# print(answer)

if __name__ == '__main__':
    app.run()