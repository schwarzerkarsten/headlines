import feedparser
from flask import Flask

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
    return """<html>
        <body>
            <h1> BBC Headlines </h1>
            <b>{0}</b> <br/>
            <i>{1}</i> <br/>
            <p>{2}</p> <br/>
        </body>
    </html>""".format(first_article.get("title"), first_article.get("published"), first_article.get("summary"))

if __name__ == '__main__':
    app.run(port=5000, debug=True)
