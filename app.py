'''CREATED BY G R V GOPAL'''
from flask import Flask, render_template_string, request
import speech_recognition as sr

app = Flask(__name__)

recognizer = sr.Recognizer()
recognized_text = ""

@app.route('/', methods=['GET', 'POST'])
def index():
    global recognized_text
    if request.method == 'POST':
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                recognized_text = recognizer.recognize_google(audio).lower()
        except sr.UnknownValueError:
            recognized_text = "Could not understand audio"
    
    return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <title>Speech Recognition</title>
            <style>
            body{
                background-image: linear-gradient(to left,#0000FF,#0099cc);
                color: white;
            }
            </style>
          </head>
          <body>
          <center>
            <h1>Speech Recognition</h1>
            <form method="post">
              <button type="submit">Speak</button>
            </form>
            <p>Your Speech: {{ text }}</p>
            </center>
          </body>
        </html>
    ''', text=recognized_text)

if __name__ == '__main__':
    app.run(debug=True)

'''CREATED BY G R V GOPAL'''
