import requests
import os
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


url = "http://www.27270.com/ent/meinvtupian/"

headers = {
    "User-Agent": UserAgent(verify_ssl=False).random
}

dir_path = os.path.join(os.getcwd(), "pic")

if not os.path.exists(dir_path):
    os.makedirs(dir_path)

html = requests.get(url, headers=headers)
html.enconding = "gb2312"
soup = BeautifulSoup(html.text, "html.parser")
img_lists = soup.find_all("img")
for item in img_lists:
    img_url = item.get("src")
    file_name = img_url.split("/")[-1]
    file_path = os.path.join(dir_path, file_name)
    res = requests.get(img_url, headers=headers)
    print("---" * 16)
    with open(file_path, "wb+") as f:
        f.write(res.content)