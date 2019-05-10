from django.shortcuts import render
import re
import operator

def index(request):  

    return render(request,'index.html',context) 

def result(request):
    text = request.GET['text']
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》\\r\\n]', '', text)    
    split_t = text[:len(text)-1].split(' ')  
    dic = {}
    for t in split_t:
        if t in dic:
            dic[t] = dic[t] + 1
        else:
            dic[t] = 1 

    arr = sorted(dic.items(), key=lambda x: x[1], reverse=True)  
    context={
        "text":text,
        "split_t":split_t,
        "arr":arr,  
    }

    return render(request,'result.html',context)

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

def about(request):
    html = urlopen("https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=014&aid=0004208343")   
    soup = BeautifulSoup(html, "html.parser",from_encoding='utf-8')  
    soup = soup.select('#articleBodyContents') 
    text =' '
    for t in soup:
        text = text + str(t.find_all(text=True)) 

    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!{}』\\‘|\(\)\[\]\<\>`\'…》]', '', text) 
    text = text.replace("fnljsfnnewscom"," ")
    text = text.replace("nfunction _flash_removeCallback "," ")
    text = text.replace("flash"," ")
    text = text.replace("\\n"," ")


    return render(request,'about.html',{"text":text})