# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:48:39 2019

@author: vidisha
"""

from urllib.request import urlopen
import urllib.request


import requests
import bs4 as bs
import re
'''
proxy_support = urllib2.ProxyHandler({"http": "http://jp.singh:csir%402019@172.16.2.37:3128",
"https": "https://jp.singh:csir%402019@172.16.2.37:3128"})
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)
'''
string=input("Enter the string: ")
strlist=string.split(' ')
name='+'.join(strlist)

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


for k in range (0,21):
    print(k)
    url='https://www.google.com/search?q='+name+'&tbm=bks&ei=42jRXM3xCc-trQG3067gCQ&start={}&sa=N&ved=0ahUKEwiN79C1pYniAhXPVisKHbepC5w4ChDy0wMIYw&biw=1252&bih=600&dpr=1.09'.format(k)
    res =requests.get(url)
    #soup = bs4.BeautifulSoup(url,'html.parser')
    req = urllib.request.Request(url, headers=hdr)
    page1_html=urlopen(req).read()
    page1_soup=bs.BeautifulSoup(page1_html,'html.parser')
    print(url)
    print(res)
     
    print("List")
    for h in page1_soup.find_all('div',{'id':'ires'}):
         for i in h.find_all('div',{'class':'srg'}):
             for j in i.find_all('div',{'class':'g'}):
                 for m in j.find_all('div',{'class':'r'}):
                     for n in m.find_all('h3'):
                          print("Book Name")
                          print(n.text.strip())
                          
    for h in page1_soup.find_all('div',{'id':'ires'}):
        for i in h.find_all('div',{'class':'srg'}):
            for j in i.find_all('div',{'class':'rc'}):
                for m in j.find_all('div',{'class':'slp f'}):
                    for w in m.find_all('a',{'class':'fl'}):
                        
                        print("Author Name")
                        print(w.text.strip())   
                        
    for h in page1_soup.find_all('div',{'id':'ires'}):
        for i in h.find_all('div',{'class':'srg'}):            
            for j in i.find_all('div',{'class':'rc'}):                
                for m in j.find_all('div',{'class':'s'}):                    
                    for w in m.find_all('span',{'class':'st'}):
                        print("Description")
                        print(w.text.strip())                       
    
              
                   
                       
                          
                         
                                                      
            
        
         
              
                   
                       
                           
                         
                                            
                     
                 
             
              
                   
                       
                         
                         
                          
    
                         
          
    
                     
