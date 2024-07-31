from flask import Flask, render_template, request
from transformers import pipeline
import os

app = Flask(__name__)


summarizer = pipeline('summarization', model="facebook/bart-large-cnn")

@app.route('/', methods=['GET', 'POST'])
def summarize():
    summary = ""
    if request.method == 'POST':
        text = request.form['text']
        if text:
            summary_list = summarizer(text, max_length=500, min_length=30, do_sample=False)
            summary = summary_list[0]['summary_text']
    return render_template('summarize.html', summary=summary)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)



