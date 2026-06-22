import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import datetime


url="https://www.fibre2fashion.com/news"

headers={
"User-Agent":"Mozilla/5.0"
}

r=requests.get(url,headers=headers)

soup=BeautifulSoup(r.text,"html.parser")


titles=[]


for h in soup.find_all("h3")[:10]:
    text=h.get_text(strip=True)

    if text:
        titles.append(text)



wb=Workbook()

ws=wb.active


ws.append(["日期","标题","来源"])


today=datetime.now().strftime("%Y-%m-%d")



for t in titles:

    ws.append([today,t,"Fibre2Fashion"])



filename=f"日报_{today}.xlsx"


wb.save(filename)


print("完成")
