from concurrent.futures import ThreadPoolExecutor
import requests
import threading
import random




def download(self, url,filename):
    r = requests.get(url, allow_redirects=True)
    if r.status_code == 200:
        open(filename, 'wb').write(r.content)
        print("200 works")
    if r.status_code == 404:
        raise Exception
            
    
    
    #not working
def multi_download(self,url_list):
    with ThreadPoolExecutor() as ex:
        res = ex.map(download, "test", "avc")

        for result in res:
            print(result)