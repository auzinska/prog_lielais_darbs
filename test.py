
from flask import Flask
from flask import request
from flask import url_for
from flask import render_template
#from module import funci


app = Flask(__name__)

@app.route('/',methods=['GET'])
def root():
   
    return render_template("rickroll.html")


@app.route('/tests')
def health():
  return "Serveris darbojas"

if __name__ == '__main__':
  app.run()
#kkk
