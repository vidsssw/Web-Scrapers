# -*- coding: utf-8 -*-
"""
Created on Thu May  9 22:56:33 2019

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

#http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-4.html)

for k in range (0,210,10):
    print(k)
    url='https://scholar.google.co.in/scholar?start={}'.format(k)
    url=url+'&q='+name+'&hl=en&as_sdt=0,5'
    
    res =requests.get(url)
    #soup = bs4.BeautifulSoup(url,'html.parser')
    req = urllib.request.Request(url, headers=hdr)
    page1_html=urlopen(req).read()
    page1_soup=bs.BeautifulSoup(page1_html,'html.parser')
    print(url)
    print(res)
    
    print("List")
    
    print("Article Titles")
    
    for i in page1_soup.find_all('div',{'id':'gs_res_ccl_mid'}):
        for j in i.find_all('div',{'class':'gs_ri'}):
            for m in j.find_all('h3'):
                print(m.text.strip())
    
    print("Article Authors")
    
    for i in page1_soup.find_all('div',{'id':'gs_res_ccl_mid'}):
        for j in i.find_all('div',{'class':'gs_ri'}):
            for m in j.find_all('div',{'class':'gs_a'}):
                print(m.text.strip())
    
    
              
                   
                       
                          
                         
                                                      
            
        
         
              
                   
                       
                           
                         
                                            
                     
                 
             
              
                   
                       
                         
                         
                          
    
                         
          
    
                     
