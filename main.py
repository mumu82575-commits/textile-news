import feedparser
from deep_translator import GoogleTranslator
from openpyxl import Workbook
from datetime import datetime


translator = GoogleTranslator(
    source='auto',
    target='zh-CN'
)


sources = [

    ("纺织",
     "TextileWorld",
     "https://www.textileworld.com/feed/"),


    ("服饰",
     "ApparelResources",
     "https://apparelresources.com/feed/"),


    ("国际",
     "BBC",
     "https://feeds.bbci.co.uk/news/world/rss.xml"),


    ("国际",
     "NYTimes",
     "https://rss.nytimes.com/services/xml/rss/nyt/World.xml")

]


TEXTILE = [

'textile',
'fiber',
'fibre',
'fabric',
'cotton',
'yarn',
'weaving',
'spinning',
'polyester',
'viscose',
'denim'

]


PRINT = [

'print',
'printing',
'package',
'packaging',
'label',
'labels',
'ink',
'offset',
'flexo',
'press',
'carton'

]


FASHION = [

'fashion',
'apparel',
'garment',
'clothing',
'brand',
'retail',
'luxury',
'sportswear',
'footwear'

]



textiles=[]

prints=[]

fashions=[]

internationals=[]




for category,name,url in sources:


    try:


        feed=feedparser.parse(url)



        for item in feed.entries[:30]:


            title=item.title


            low=title.lower()


            try:

                title_cn=translator.translate(title)

            except:

                title_cn=title



            news=(

                title_cn,

                title,

                name

            )




            if any(

                x in low

                for x in TEXTILE

            ):


                textiles.append(news)



            elif any(

                x in low

                for x in PRINT

            ):


                prints.append(news)



            elif any(

                x in low

                for x in FASHION

            ):


                fashions.append(news)




            else:


                internationals.append(news)




    except:

        pass






textiles=textiles[:4]

prints=prints[:4]

fashions=fashions[:4]

internationals=internationals[:4]





today=datetime.now().strftime("%Y-%m-%d")



wb=Workbook()

ws=wb.active


ws.title="日报"




ws.append([

"日期",

"分类",

"中文标题",

"原标题",

"来源"

])





for i in textiles:


    ws.append([


        today,

        "纺织",

        i[0],

        i[1],

        i[2]



    ])





for i in prints:



    ws.append([



        today,

        "印刷",

        i[0],

        i[1],

        i[2]


    ])





for i in fashions:


    ws.append([


        today,

        "服饰",

        i[0],

        i[1],

        i[2]



    ])






for i in internationals:



    ws.append([


        today,

        "国际",

        i[0],

        i[1],

        i[2]



    ])





filename=f"日报_{today}.xlsx"



wb.save(filename)



print("日报生成成功")
print("纺织",len(textiles))
print("印刷",len(prints))
print("服饰",len(fashions))
print("国际",len(internationals))
