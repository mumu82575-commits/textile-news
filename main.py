import feedparser
from openpyxl import Workbook
from datetime import datetime


rss_url = "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"

feed = feedparser.parse(rss_url)


wb = Workbook()

ws = wb.active

ws.title = "新闻"


ws.append(["日期", "标题", "来源"])


today = datetime.now().strftime("%Y-%m-%d")


for item in feed.entries[:10]:

    ws.append([
        today,
        item.title,
        "NYTimes"
    ])


filename = f"日报_{today}.xlsx"


wb.save(filename)

print("Excel生成成功")
