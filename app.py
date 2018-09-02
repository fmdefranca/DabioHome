from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/<name>')
def say_hello(name):
    return "<h1>Hello {}</h1>".format(name)

@app.route('/<int:post_id>')
def post_id(post_id):
    return 'Post {0}'.format(post_id)
    
if __name__ == '__main__':
    app.run()