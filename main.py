from importlib.metadata import PackageNotFoundError
from pydoc import pager
import requests

pageNum = 0
for i in range(0,120):
    pageNum = i * 2
    pageUrl = "https://illuminate.digital/books/Psychology/aqapsych1/"+str(pageNum)+"-"+str(pageNum+1)+"/"+str(pageNum)+"-"+str(pageNum+1)+".jpg"
    pageFile = requests.get(pageUrl)
    open("pages/page"+str(pageNum)+".jpg","wb").write(pageFile.content)
    print("Page "+str(pageNum)+" downloaded")
