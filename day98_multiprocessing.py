

import multiprocessing
import requests

def downloadfile(url,name):
    print(f"started downloading{name}")
    response=requests.get(url)
    open(f"files/file{name}.jpg","wb").write(response.content)
    print(f"finished downloading{name}")

url="https://picsum.photos/2000/3000"
pros=[]
for i in range(10):
    p=multiprocessing.process(target=downloadfile,args=[url,i])
    p.start()
    pros.append(p)

for p in pros:
    p.join()















