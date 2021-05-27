from flask import Flask

app = Flask(__name__)


@app.route('/', methods = ['GET' , 'PDST'])
def hello_world():
    return '<h1>Hello World!<h1/>'


    
if __name__ == '__main__':
    app.run(port=8080, debug=True)