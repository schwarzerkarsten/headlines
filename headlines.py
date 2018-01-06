import feedparser
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

RSS_FEEDS = {
    'bbc': "http://feeds.bbci.co.uk/news/rss.xml",
    'spiegel': "http://www.spiegel.de/schlagzeilen/tops/index.rss",
    'heise': "http://www.heise.de/newsticker/heise-atom.xml",
    'hessenschau': 'http://www.hessenschau.de/index.rss'
}

@app.route("/")
def get_news():
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_FEEDS:
        publication="spiegel"
    else:
        publication=query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template("home.html",articles=feed['entries'])

if __name__ == '__main__':
    app.run(port=5000, debug=True)
