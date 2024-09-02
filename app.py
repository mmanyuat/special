from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_word():
  return "Hello World"


if __name__ == "__main__":
  print("I`m inside the if now")
  app.run(host='0.0.0.0', debug=True)
