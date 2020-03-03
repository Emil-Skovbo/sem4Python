from concurrent.futures import ThreadPoolExecutor
import requests
import threading
import random
        
class NotFoundException(Exception):
    pass

class DataSheet():
    def __init__(self, url_list):
        self.url_list = url_list


    def download(self, url,):
        r = requests.get(url, allow_redirects=True)
        if r.status_code == 200:
            img_name = url.split('/')[3]
            open(img_name, 'wb').write(r.content)
            print("200 works")
        if r.status_code == 404:
            raise NotFoundException()
            
    def download_image(self, img_url):
        img_bytes = requests.get(img_url).content
        img_name = img_url.split('/')[3]
        img_name = f'{img_name}.jpg'
        with open(img_name, 'wb') as img_file:
            img_file.write(img_bytes)
            print(f'{img_name} was downloaded...')

    def multi_download(self,url_list):
        ds = DataSheet(url_list)
        with ThreadPoolExecutor() as ex:
            ex.map(ds.download,url_list)

    def __iter__(self):
        return self
    def __next__(self):
        if random.choice(["go", "go", "go", "stop"]) == "stop":
            raise StopIteration  # signals "the end"
        return 1  
    

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]
dataurllist = ["https://api.statbank.dk/v1/data/FOLK1A/CSV?valuePresentation=CodeAndValue&delimiter=Semicolon&Tid=2020K1%2C2008K1&OMR%C3%85DE=000&CIVILSTAND=G%2CF", "http://httpbin.org/status/404"]
ds = DataSheet(dataurllist)
#print(dataurllist[0])
#ds.download(img_urls[0],"testttt")
ds.multi_download(img_urls)