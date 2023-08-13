import requests, os
from bs4 import BeautifulSoup
from urllib.request import urlopen # module for reading images

url = "https://reurl.cc/8jmDLM"
html = requests.get(url)
soup = BeautifulSoup(html.text, "lxml")

# make a POST request(XHR)
url = "https://running.biji.co/index.php?pop=ajax&func=album&fename=load_more_photos_in_listing_computer"
payload = {"type": "place", "rows": "0", "need_rows": "20",
           "cid": "5791", "album_id": "30668"}
html = requests.post(url, data = payload)
soup = BeautifulSoup(html.text, "lxml")

# create a directory to store images
images_dir = "C:\\Users\\HP\\Desktop\\Try\\Sports-Album-Scraping-dir\\Sports-Album-Scraping-images"

# download images
photos = soup.find_all("img", class_ = "photo_img photo-img")
counter = 0 # 紀錄下載圖片數量
for photo in photos:
    img_path = photo["src"]
    if img_path and (".jpg" in img_path):
        # 將完整路徑切割，並取串列中最右邊的字串
        file_name = img_path.split("/")[-1]
        full_path = os.path.join(images_dir, file_name)
        print(img_path)

        # store images
        try:
            image = urlopen(img_path)
            with open(full_path, "wb") as f:
                f.write(image.read())
            counter += 1
        except:
            print(f"{file_name} can't be read and download!!")

print("共下載", counter, "張圖片")
