# Basic Socket

This direcotry contain following file
Index is the main html file, other default html files located under templates/ 

## README.md
- client_task2.py
- index.html
- screenshoot_test_image
- server_task1.py
- server_task3.py
- templates
   - 404.html
- test_client_task3.py



## Task 1: server_task1.py
- This is a single server can manage one request at time,<br>testing result located under screenshoot_test_image/ directory</p>
## Task 2: client_task2.py
- This the client request througth the command line argument, the argument accepted only
- python client_task.py -i IP_addrs -p PORTNR -f FILENAME
- it will return either OK 200 response or 404 not found response, it manage only the GET request
  
## Task 3: server_task3.py<li>
- A multithread server can manage different request at the same time, listen are 5 means the server can
- can wait inntil 5 request in backlog<br>Creating test_client_task3.py to make several request to the multithreadserver, this is without GET header request
  
