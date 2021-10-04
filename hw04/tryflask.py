#!/usr/bin/env python3

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
        templateData = {
              'title' : 'Etch-a-Sketch',
        }
        return render_template('index.html')
        
@app.route("/<direction>/")
def action(direction):
    if direction == 'up':
        print("UP")
    if direction == 'down':
        print("DOWN")
    if direction == 'left':
        print("LEFT")
    if direction == 'right':
        print("RIGHT")
    if direction == 'clear':
        print("CLEAR")

    
    
if __name__ == '__main__':
    app.run(debug=True, port=8081, host='0.0.0.0')