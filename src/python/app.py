from flask import Flask, render_template

app = Flask(__name__)

# Mock data for news articles
news_articles = [
    {"title": "Article 1", "content": "Content for article 1."},
    {"title": "Article 2", "content": "Content for article 2."},
    # Add more articles as needed
]

@app.route('/')
def index():
    return render_template('index.html', articles=news_articles)

if __name__ == '__main__':
    app.run(debug=True)
