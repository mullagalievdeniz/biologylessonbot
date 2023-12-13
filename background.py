from flask import Flask
from flask import request
from threading import Thread



app = Flask('')

@app.route('/')
def home():
  return "I'm alive"

@app.route('/check_active', methods= ['GET'])
def arduino():
  return "ts_alive"

def run():
  app.run(host='0.0.0.0', port=80)

def keep_alive():
  t = Thread(target=run)
  t.start()
