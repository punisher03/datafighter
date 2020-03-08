from werkzeug.utils import secure_filename
import requests
from flask import *
import json
from time import sleep
from parsel import Selector
from flask import jsonify

app = Flask(__name__)
@app.route('/', methods =['GET', 'POST'])
def basic():
    return render_template('index.html')


@app.route('/play', methods =['GET', 'POST'])
def resumescore():
   
   return render_template('cv.html',t= "hello")




if __name__ == '__main__':
    app.run(debug=True)    




