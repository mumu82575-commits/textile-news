import feedparser
from deep_translator import GoogleTranslator
from openpyxl import Workbook
from datetime import datetime

# 新闻源
sources = [

    ("纺织",
     "Textile World",
     "https://www.textileworld.com/feed/",
     4),

    ("印刷",
     "Packaging Europe",
     "https://packagingeurope.com/feed/",
     2),

    ("印刷",
     "Labels & Labeling",
     "https://www.labelsandlabeling.com/feed/",
     2),

    ("服饰",
     "Apparel Resources",
     "https://apparelresources.com/feed/",
     4),

    ("国际",
     "BBC",
     "https://feeds.bbci.co.uk/news/world/rss.xml",
     4)

]


# 翻译器
translator = GoogleTranslator(
    source='auto',
    target='zh-CN'
)

today = datetime.now().strftime("%Y-%m-%d")

wb = Workbook()
ws = wb.active
ws.title = "日报"

ws.append([
    "日期",
    "分类",
    "中文标题",
    "原标题",
    "来源"
])


for category, name, url, limit in sources:

    try:

        feed = feedparser.parse(url)

        count = 0

        for item in feed.entries:

            if count >= limit:
                break


            title = item.title


            try:
                title_cn = translator.translate(title)

            except:
                title_cn = title


            ws.append([

                today,

                category,

                title_cn,

                title,

                name

            ])


            count += 1


    except Exception as e:

        print(name)

        print(e)



filename = f"日报_{today}.xlsx"

wb.save(filename)

print("日报生成成功")
