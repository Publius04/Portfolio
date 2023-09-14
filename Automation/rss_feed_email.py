import feedparser, datetime, time, smtplib, ssl
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

PARAS = False

class Article:
    def __init__(self, title: str, link: str, auth: str, summary: str, paras: list, date: str):
        self.title = title
        self.link = link
        self.auth = auth
        self.summary = summary
        self.paras = paras
        self.date = date

    def html(self) -> str:
        html = f"<h3>{self.date[:11]}<br>{self.title} - <a href=\"{self.link}\">{self.auth}</a></h3>"
        html += f"<h4>{self.summary}</h4>"
        if PARAS:
            for p in self.paras:
                html += f"<p>{p}</p>"
        return html

class Source:
    def __init__(self, title: str):
        self.title = title
        self.articles = []

    def add_article(self, article: Article) -> None:
        self.articles.append(article)

class Content:
    def __init__(self):
        self.sources = []

    def add_source(self, source: Source) -> None:
        self.sources.append(source)

    def html(self) -> str:
        text = "<html><body style=\"font-family: 'Courier New'\"><h1>You just got a letter</h1>"
        for source in self.sources:
            text += f"<h2>{source.title.upper()}</h2>"
            for article in source.articles:
                text += article.html()
        text += "</body></html>"
        return text

def compile_rss(source) -> Source:
    new = Source(source)
    feed = feedparser.parse(compilers[source][0])
    for entry in feed.entries:
        t = datetime.datetime.now() - datetime.datetime.fromtimestamp(time.mktime(entry.published_parsed))
        if t.days < 1:
            value = entry.content[0]["value"]
            soup = BeautifulSoup(value, 'html.parser')
            paras = [x.text for x in soup.find_all("p")]
            article = Article(entry.title, entry.link, entry.author, entry.summary, paras, entry.published)
            new.add_article(article)
    return new

compilers = {
    "source1": ["www.source1.com/rss.xml", compile_rss]
}

def generate_html() -> str:
    email = Content()
    for c in compilers:
        email.add_source(compilers[c][1](c))
    return email.html()

def send_email(receiver):
    sender = "your_email@gmail.com"
    pwd = "password"

    text = MIMEText("Error rendering", "plain")
    html = MIMEText(generate_html(), "html")

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Your RSS Feed"
    msg["From"] = sender
    msg["To"] = receiver
    msg.attach(text)
    msg.attach(html)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
        server.login(sender, pwd)
        server.sendmail(sender, receiver, msg.as_string())

def main():
    send_email("your_email@gmail.com")

if __name__ == "__main__":
    main()