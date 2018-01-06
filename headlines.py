import feedparser
from flask import Flask
from flask import render_template

app = Flask(__name__)

RSS_FEEDS = {
    'bbc': "http://feeds.bbci.co.uk/news/rss.xml",
    'spiegel': "http://www.spiegel.de/schlagzeilen/tops/index.rss",
    'heise': "http://www.heise.de/newsticker/heise-atom.xml",
    'hessenschau': 'http://www.hessenschau.de/index.rss'
}

@app.route("/")
@app.route("/<publication>")
def get_news(publication="spiegel"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][0]
    return render_template("home.html",articles=feed['entries'])

if __name__ == '__main__':
    app.run(port=5000, debug=True)
