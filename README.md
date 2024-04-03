
This direcotry contain following file
Index is the main html file, other default html files located under templates/ 

├── README.md
├── client_task2.py
├── index.html
├── server_task1.py
├── server_task3.py
└── templates
    └── 404.html

<ul>
<li>Task 1: server_task1.py<li>
<p>This is a single server can manage one request at time,<br>testing result located under screenshoot_test_image/ directory</p>
<li>Task 2: client_task2.py<li>
<p>This the client request througth the command line argument, the argument accepted only<br>
python client_task.py -i IP_addrs -p PORTNR -f FILENAME<br>
it will return either OK 200 response or 404 not found response, it manage only the GET request</p>
<li>Task 3: server_task3.py<li>
<p>A multithread server can manage different request at the same time, listen are 5 means the server can<br>
can wait inntil 5 request in backlog</p>
</ul>