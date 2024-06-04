from flask import Flask, render_template, request, redirect, url_for, session
import joblib
from googletrans import Translator
import numpy as np

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Model ve vektörizeri yükleme
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Translator instance
translator = Translator()

emotions = ["neutral", "joy", "sadness", "fear", "anger", "surprise", "disgust"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'emotion_index' not in session:
        session['emotion_index'] = 0
        session['mistakes'] = 0
        session['scores'] = {emotion: 0 for emotion in emotions}
        session['current_result'] = None
        session['user_text'] = None
        session['total_score'] = session.get('total_score', 0)  # Initialize total score if not exists
        session['gameover'] = False

    if request.method == 'POST':
        user_text = request.form['text']
        session['user_text'] = user_text
        translated = translator.translate(user_text, src='tr', dest='en').text  # Translate turkish to english
        user_vector = vectorizer.transform([translated])
        predicted_proba = model.predict_proba(user_vector)[0]
        predicted_emotion = model.classes_[np.argmax(predicted_proba)]
        emotion = emotions[session['emotion_index']]
        if predicted_emotion == emotion:  # Predicted correct emotion
            session['total_score'] += get_score(session['mistakes'])  # Add score our attempt quantity to total.
            session['emotion_index'] += 1  # Move to the next emotion
            session['mistakes'] = 0  # reset attempts
        else:  # if emotion does not match
            session['mistakes'] += 1
            if session['mistakes'] == 3:
                session['emotion_index'] += 1
                session['mistakes'] = 0
        session['current_result'] = {
            'emotion': emotion,
            'score': session['scores'][emotion],
            'predicted_emotion': predicted_emotion,
            'probabilities': predicted_proba.tolist()
        }
        if session['emotion_index'] == len(emotions):  # When all the emotions are completed
            session['emotion_index'] = 0
            session['gameover'] = True

    emotion = emotions[session.get('emotion_index', 0)]
    current_result = session.get('current_result')
    model_classes = model.classes_.tolist()
    total_score = session['total_score']  # Get total score from session
    gameover = session.get('gameover')  # Get game over message from session
    attempts = 3 - session.get('mistakes');
    return render_template('index.html', emotion=emotion, current_result=current_result, model_classes=model_classes,
                           total_score=total_score, enumerate=enumerate, gameover=gameover, attempts=attempts)

def get_score(mistakes):
    if mistakes == 0:
        return 3
    elif mistakes == 1:
        return 2
    elif mistakes == 2:
        return 1
    else:
        return 0


@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
