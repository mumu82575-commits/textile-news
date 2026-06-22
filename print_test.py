import requests
from bs4 import BeautifulSoup


url="https://whattheythink.com/sections/packaging/"


headers={

"User-Agent":
"Mozilla/5.0"

}


r=requests.get(

url,

headers=headers

)


print("状态码:",r.status_code)



soup=BeautifulSoup(

r.text,

"html.parser"

)



titles=[]



for h in soup.find_all(["h2","h3"]):


    t=h.get_text(strip=True)



    if len(t)>20:


        titles.append(t)




titles=titles[:10]



print()


for i in titles:


    print(i)
