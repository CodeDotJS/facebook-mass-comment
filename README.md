# facebook-mass-comment

> comments 'n' times on any facbook post of a person or page.

# Running

> python comments.py

# Usage

## Token
```py
      access_token = 'Paste your access token here' 
      
Replace the text with the access token given by facebook.
```
## Total Comment
```py
      for x in xrange(10):
      
Replace '10' with any number to comment that much time on a post.
```
## Message
```py
      param_data = {  '   format':'json', 
                         'message':'<3', # change message from here
                         'access_token':access_token 
                   } 
```
## Post ID
```py
      path ='/'+'PUT FB STATUS ID HERE'+'/comments'
      
      url='/PUT FB STATUS ID HERE'

You have to replace __PUT FB STATUS ID HERE__ with the actual ID of a facebook post.
```
## Full Tutorial

      [Mass Commeting on Facebook Post](https://rishicodes.wordpress.com/2015/10/15/mass-commenting-on-facebook-posts)
      
## Installation

> sudo apt-get install python-pip

## Modules needed :

### httplib2
>   - sudo pip install httplib2

### urllib3
>   - pip install urllib3 [ install Certifi and PyOpenSSL ]

### bs4
>   - pip install bs4

### json
>   - pip install json


