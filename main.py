from flask import Flask,render_template, make_response, jsonify, request
import whisper
import os

app = Flask(__name__)

@app.route('/', methods=['GET']) 
def index(): 
  return render_template('index.html') 

@app.route('/', methods=['POST'])
def TranscribeRequest():
  if 'audioFile' not in request.files:
    return make_response(jsonify(message = 'audio file required'), 422)
  
  audio = request.files['audioFile']
  model = whisper.load_model("base")
  audioTmpDir = "./tmp/"+audio.filename
  audio.save(audioTmpDir)
  result = model.transcribe(audioTmpDir)
  os.remove(audioTmpDir)
  return render_template("index.html", content = result['text'])


app.run(debug=(os.environ['environment']!='prod'))