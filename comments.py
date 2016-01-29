import httplib, urllib 
from bs4 import BeautifulSoup 
import os 
import json
import time

access_token='Paste your access token here'
# access_token = raw_input('Paste your access token here :')

conn = httplib.HTTPSConnection("graph.facebook.com") 
print 'Please Wait!'
 
def comment(url): 
    connect = httplib.HTTPSConnection("graph.facebook.com") 
    connect.request("GET",url) 
    for x in xrange(10): # make it 10, 100, 1000, 10000  
            
            print 'commenting %d '% x
            path ='/'+'PUT FB STATUS ID HERE'+'/comments'
            param_data={  'format':'json', 
                        'message':'<3', # change message from here
                        'access_token':access_token 
                  } 
            connect = httplib.HTTPSConnection("graph.facebook.com") 
            connect.request("POST",path,urllib.urlencode(param_data),{}) 
            time.sleep(0.09)
           
url='/PUT FB STATUS ID HERE' 
comment(url) 
print 'DONE!'
