from flask import Flask, render_template, make_response, jsonify, request
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
  
  aiModel = request.form.get("aiModel")
  if(request.form.get("isEnglish")=='on'):
    aiModel += '.en'
  print('selected aiModel:'+aiModel)
  model = whisper.load_model(aiModel)
  audio = request.files['audioFile']
  audioTmpDir = "./tmp/"+audio.filename
  audio.save(audioTmpDir)
  print('file uplodad sucessfully: ' + audioTmpDir)
  result = model.transcribe(audioTmpDir)
  print('transcription finished: '+result['text'])
  os.remove(audioTmpDir)
  print('file deleted')
  return render_template("index.html", content = result['text'])


if __name__ == '__main__':
  app.run()