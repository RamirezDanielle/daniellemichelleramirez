from flask import Flask, request, render_template, redirect, session
app = Flask(__name__)

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/bio')
def about():
    return render_template ('about.html')

if __name__=='__main__':
    app.run(debug=True)