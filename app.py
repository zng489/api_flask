from crypt import methods
from flask import Flask

app = Flask(__name__)

#@app.route('/')
#def home():
#    return "Hello, World!"


#app.run(port=5000)

@app.route('/store', methods=['POST'])
def create_store():
    pass



@app.route('/store/<string:name>')
def get_store(name):
    pass


app.run(port=5000)