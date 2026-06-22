import requests
from bs4 import BeautifulSoup


url = "https://whattheythink.com/sections/packaging/"


headers = {
    "User-Agent": "Mozilla/5.0"
}


r = requests.get(
    url,
    headers=headers
)


print("状态码:", r.status_code)


soup = BeautifulSoup(
    r.text,
    "html.parser"
)


titles = []


for h in soup.find_all(["h2", "h3"]):

    text = h.get_text(strip=True)

    if len(text) > 20:
        titles.append(text)


titles = titles[:10]


print("\n抓取结果：\n")


for t in titles:
    print(t)
