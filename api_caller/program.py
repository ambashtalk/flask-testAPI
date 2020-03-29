import requests 
import json
from base64 import b64encode

url = 'http://localhost:5000/api/test1'

file_path = "send.jfif"
ext = file_path.split('.')[1]

img = None
with open(file_path, 'rb') as image:
    img = b64encode(image.read())

data = {
    'key1':'value1',
    'key2':'value2',
    'media': img,
    'type' : ext
    }

'''MAKING A GET REQUEST TO OUR API test1'''
def rgt1():
    response = requests.get(url=url, params=data)
    print("Received Status = \n",response.status_code)
    print("Response =\n", response.text)

'''MAKING A POST REQUEST TO OUR API test1'''
def rpt1():
    response = requests.post(url=url, data=data) 
    print("Response Status=\n",response.status_code)
    print("Response =\n",response.text)

'''MAKING A GET REQUEST TO OUR API test2'''
def rgt2():
    num = 10
    url = f'http://localhost:5000/api/test2/{num}'
    response = requests.get(url=url)
    print("Response Status=\n",response.status_code)
    print("Response =\n",response.text)

'''MAKING A POST REQUEST TO OUR API test2'''
def rpt2():
    data = {'num':10}
    url = 'http://localhost:5000/api/test2'
    #data was not in byte format so can be passed as json
    response = requests.post(url=url, json=data)
    print("Response Status=\n",response.status_code)
    print("Response =\n",response.text)

# check all the requests one by one
# rgt1()
# rpt1()
# rgt2()
rpt2()