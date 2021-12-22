from flask import Flask
import random

app = Flask(__name__)
random_number = random.randint(0, 9)


@app.route("/")
def hello():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">' \
           '<p>Type it to the end of link (i.e. "/8") </p>'


@app.route("/<int:guess>")
def guessed_number(guess):
    if random_number > guess:
        return '<h1 style="color: red;">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/B2vBunhgt9Pc4/giphy.gif">'
    elif random_number < guess:
        return '<h1 style="color: purple;">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/cLcxtL1z8t8oo/giphy.gif">'
    else:
        return '<h1 style="color: green;">You Found Me!</h1>' \
               '<img src="https://media.giphy.com/media/kBZBlLVlfECvOQAVno/giphy.gif">'



if __name__ == "__main__":
    app.run(debug=True)