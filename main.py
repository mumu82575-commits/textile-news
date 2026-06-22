import feedparser
from deep_translator import GoogleTranslator
from openpyxl import Workbook
from datetime import datetime

sources = [

("纺织","Textile World","https://www.textileworld.com/feed/"),

("印刷","PrintWeek","https://www.printweek.com/feed/"),

("服饰","Apparel Resources","https://apparelresources.com/feed/"),

("国际","BBC","https://feeds.bbci.co.uk/news/world/rss.xml")

]


wb = Workbook()

ws = wb.active

ws.title="日报"


ws.append([

"日期",

"分类",

"标题（中文）",

"原标题",

"来源"

])


today=datetime.now().strftime("%Y-%m-%d")


translator=GoogleTranslator(
source='auto',
target='zh-CN'
)


for category,name,url in sources:


    try:


        feed=feedparser.parse(url)



        count=0



        for item in feed.entries:



            if count>=4:
                break


            title=item.title



            try:

                title_cn=translator.translate(title)

            except:

                title_cn=title



            ws.append([


                today,

                category,

                title_cn,

                title,

                name


            ])



            count+=1



    except:

        pass





filename=f"日报_{today}.xlsx"


wb.save(filename)


print("日报生成成功")
