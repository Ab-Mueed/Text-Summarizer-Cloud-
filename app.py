from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)


summarizer = pipeline('summarization', model="facebook/bart-large-cnn")

@app.route('/', methods=['GET', 'POST'])
def summarize():
    summary = ""
    if request.method == 'POST':
        text = request.form['text']
        if text:
            summary_list = summarizer(text, max_length=500, min_length=80, do_sample=False)
            summary = summary_list[0]['summary_text']
    return render_template('summarize.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)





