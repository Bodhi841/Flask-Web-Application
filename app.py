from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

def get_sentiment_analysis(input_text):
    analysis = TextBlob(input_text)
    polarity = analysis.sentiment.polarity
    subjectivity = analysis.sentiment.subjectivity

    if polarity > 0:
        sentiment = 'Positive'
        feedback = "Your text conveys positivity and optimism."
        color = 'green'
    elif polarity < 0:
        sentiment = 'Negative'
        feedback = "Your text conveys negativity or dissatisfaction."
        color = 'red'
    else:
        sentiment = 'Neutral'
        feedback = "Your text is neutral and balanced."
        color = 'gray'

    return sentiment, color, feedback, subjectivity

@app.route('/', methods=['GET', 'POST'])
def index():
    result = {
        "sentiment": None,
        "color": None,
        "feedback": None,
        "subjectivity": None
    }
    user_input = ""

    if request.method == 'POST':
        user_input = request.form.get('user_input', '')
        if user_input.strip(): 
            sentiment, color, feedback, subjectivity = get_sentiment_analysis(user_input)
            result.update({
                "sentiment": sentiment,
                "color": color,
                "feedback": feedback,
                "subjectivity": f"{subjectivity:.2f}"
            })

    return render_template('index.html', result=result, user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)
