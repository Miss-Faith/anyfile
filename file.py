from flask import Flask, render_template

app = Flask(__name__)

file = [
  {
    'author':'student1',
    'title':'Flask',
    'content':'Flask Deployment',
    'date':'May 5 2022'
  },
  {
    'author':'student2',
    'title':'Flask',
    'content':'Flask Deployment',
    'date':'May 5 2022'
  },
  {
    'author':'student3',
    'title':'Flask',
    'content':'Flask Deployment',
    'date':'May 5 2022'
  },
  {
    'author':'student4',
    'title':'Flask',
    'content':'Flask Deployment',
    'date':'May 5 2022'
  }
]

@app.route("/")
def hello_world():
 return render_template('index.html',posts=file)

if __name__ == '__main__':
  app.run(debug=True)