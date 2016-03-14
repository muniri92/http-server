# http-server

STEP - 1
************
The server will send back a response to the client that the message was recieved properly. We have set up an error response as well. Tests were made to ensure that the message was sent properly.
 

STEP - 2
************
The server will parse the request sent to the user see if the user has send the proper information before sending back it's response. The server will split the header and see that it fits the correct format. If it does not, it will raise the error message corresponding to the error.


STEP - 3
************
Here is our simple http server.
It can use the client request to find and show what is being requested. I used stack overflow to find out about the os.path.isfile method to validate whether the uri is infact a valid file.
