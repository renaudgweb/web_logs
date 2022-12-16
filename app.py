#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_logs():
	with open('server.log', 'r') as f:
		logs = f.read()
	return render_template('logs.html', logs=logs)

if __name__ == '__main__':
	app.run()
