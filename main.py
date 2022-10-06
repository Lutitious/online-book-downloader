from importlib.metadata import PackageNotFoundError
from pydoc import pager
import requests

pageNum = 0
for i in range(1,208):
    pageNum = i * 2
    #https://illuminate.digital/books/Psychology/aqapsych2/2-3/2.jpg
    pageUrl = "https://illuminate.digital/books/Psychology/aqapsych2/"+str(pageNum)+"-"+str(pageNum+1)+"/"+str(pageNum)+".jpg"
    pageFile = requests.get(pageUrl)
    open("pages/page"+str(pageNum)+".jpg","wb").write(pageFile.content)
    print("Page "+str(pageNum)+" downloaded")
