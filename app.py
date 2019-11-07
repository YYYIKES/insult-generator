from flask import Flask, render_template, url_for, request
import markovify


app = Flask(__name__)

with open('static/datasets/insults-cleaned.txt') as f:
    text = f.read()

text_model = markovify.NewlineText(text, state_size=2)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        for i in range(1):
            insult = text_model.make_sentence(
                max_overlap_ratio=0.7, tries=1000)
        return render_template('index.html', insult=insult)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
