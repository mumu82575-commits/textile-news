import feedparser
from openpyxl import Workbook
from datetime import datetime

sources = [

("国际", "NYTimes",
"https://rss.nytimes.com/services/xml/rss/nyt/World.xml"),

("国际", "BBC",
"https://feeds.bbci.co.uk/news/world/rss.xml")

]

wb = Workbook()
ws = wb.active
ws.title = "日报"

ws.append([
"日期",
"分类",
"标题",
"来源"
])


today = datetime.now().strftime("%Y-%m-%d")


for category,name,url in sources:

    try:

        feed = feedparser.parse(url)

        for item in feed.entries[:10]:

            ws.append([

                today,

                category,

                item.title,

                name

            ])

    except:

        pass


filename = f"日报_{today}.xlsx"

wb.save(filename)

print("日报生成成功")
