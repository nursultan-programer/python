from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
  return "welcome to website"

if __name__=="__main__":
  app.run(debug=True)
