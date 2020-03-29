__init__.py :
Flask file used to run server

api_caller/program.py :
A python program that sends request to our flask API

Instructions:

1) RUN __init__.py to get the server runnig

2) The api_caller directory has an image file that is used by program.py
    as a sample media to test file transfer.

   program.py module is only for reference that shows how we can send
   and recieve data using Python.

3) You can send GET and POST request to the api by any means:
	* curl
	* js
	* python, etc.
4) Your url for the api will be the the paths specified by - 
	api.add_resource()
   which is present in __init.py__