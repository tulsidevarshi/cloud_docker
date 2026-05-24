# Running app directly without docker

(.venv) (base) devarshisingh@Devarshis-MacBook-Air gcfs_docker % uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

INFO:     Will watch for changes in these directories: ['/Users/devarshisingh/Downloads/upgrad_practice/gcfs_docker']

INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)

INFO:     Started reloader process [16433] using WatchFiles

INFO:     Started server process [16440]

INFO:     Waiting for application startup.

INFO:     Application startup complete.

INFO:     127.0.0.1:61479 - "GET /extract-from-azure HTTP/1.1" 200 OK

INFO:     127.0.0.1:61479 - "GET /favicon.ico HTTP/1.1" 404 Not Found

WARNING:  WatchFiles detected changes in 'app/main.py'. Reloading...

INFO:     Shutting down

INFO:     Waiting for application shutdown.

INFO:     Application shutdown complete.

INFO:     Finished server process [16440]

INFO:     Started server process [16711]

INFO:     Waiting for application startup.

INFO:     Application startup complete.

^CINFO:     Shutting down

INFO:     Waiting for application shutdown.

INFO:     Application shutdown complete.

INFO:     Finished server process [16711]

INFO:     Stopping reloader process [16433]


# Build via DOCKER

(.venv) (base) devarshisingh@Devarshis-MacBook-Air gcfs_docker % docker build -t async-blob-app .

[+] Building 36.4s (11/11) 
FINISHED                                                                                                docker:desktop-linux

 => [internal] load build definition from 
 Dockerfile                                                                                               0.0s
 
 => => transferring dockerfile: 
 247B                                                                                                               0.0s
 
 => [internal] load metadata for docker.io/library/python:3.
 12-slim                                                                                4.9s
 
 => [auth] library/python:pull token for registry-1.docker.
 io                                                                                      0.0s
 
 => [internal] load .
 dockerignore                                                                                                               
    0.0s
 
 => => transferring context: 2B                                                                                                                    0.0s
 
 => [1/5] FROM docker.io/library/python:3.12-slim@sha256:090ba77e2958f6af52a5341f788b50b032dd4ca28377d2893dcf1ecbdfdfe203                          4.4s
 
 => => resolve docker.io/library/python:3.12-slim@sha256:090ba77e2958f6af52a5341f788b50b032dd4ca28377d2893dcf1ecbdfdfe203                          0.0s
 
 => => sha256:714418592de0993eea6b4ab47261e028ca8f848246a78374d0f2bc576b6fde2e 12.04MB / 12.04MB                                                   0.7s
 
 => => sha256:057086c2c0d31d0923c7beff0bc95416b04ff21a913f864fad49b51f5c87faf1 250B / 250B                                                         1.7s
 
 => => sha256:c6197f0005f45d3d6ce0fe015046a14edfe5d5b5aa231b273b73e4231e7a0151 1.27MB / 1.27MB                                                     1.0s
 
 => => sha256:cda3d70ae7d7c3d0b3b57a99a2085f9d93e919a846913dc6517a420b348c123d 30.14MB / 30.14MB                                                   3.4s
 
 => => extracting sha256:cda3d70ae7d7c3d0b3b57a99a2085f9d93e919a846913dc6517a420b348c123d                                                          0.7s
 
 => => extracting sha256:c6197f0005f45d3d6ce0fe015046a14edfe5d5b5aa231b273b73e4231e7a0151                                                          0.1s
 
 => => extracting sha256:714418592de0993eea6b4ab47261e028ca8f848246a78374d0f2bc576b6fde2e                                                          0.2s
 
 => => extracting sha256:057086c2c0d31d0923c7beff0bc95416b04ff21a913f864fad49b51f5c87faf1                                                          0.0s
 
 => [internal] load build context                                                                                                                  1.6s
 
 => => transferring context: 163.14MB                                                                                                              1.6s
 
 => [2/5] WORKDIR /app                                                                                                                             0.3s
 => [3/5] COPY requirements.txt .                                                                                                                  0.0s
 
 => [4/5] RUN pip install --no-cache-dir -r requirements.txt                                                                                      20.1s
 
 => [5/5] COPY . .                                                                                                                                 0.6s
 
 => exporting to image                                                                                                                             5.8s
 
 => => exporting layers                                                                                                                            3.8s
 
 => => exporting manifest sha256:598334b22a56db634c379e28acf93b666795928bb5b1cc1db3f01790047d44ca                                                  0.0s
 
 => => exporting config sha256:775f748a2069a88f09ff11d46139b9f813f19563e739d928f1778cc8820e7e12                                                    0.0s
 
 => => exporting attestation manifest sha256:20666deede51f8924a7e76738e04254e307c9115ed3f2ea076af185bc3369d5d                                      0.0s
 
 => => exporting manifest list sha256:7fc94b5f4c039fb20d6ba8e76166a9442dc595d318e707c6a8c80782deb93af4                                             0.0s
 
 => => naming to docker.io/library/async-blob-app:latest                                                                                           0.0s
 
 => => unpacking to docker.io/library/async-blob-app:latest                                                                                        2.0s

(.venv) (base) devarshisingh@Devarshis-MacBook-Air gcfs_docker % docker run -p 8000:8000 --name my-running-app async-blob-app

INFO:     Started server process [1]

INFO:     Waiting for application startup.

INFO:     Application startup complete.

INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)

INFO:     192.168.65.1:48429 - "GET / HTTP/1.1" 404 Not Found

INFO:     192.168.65.1:48429 - "GET /favicon.ico HTTP/1.1" 404 Not Found

INFO:     192.168.65.1:38726 - "GET /extract-from-azure HTTP/1.1" 200 OK

INFO:     192.168.65.1:38726 - "GET /favicon.ico HTTP/1.1" 404 Not Found

INFO:     192.168.65.1:19494 - "GET /extract-from-azure HTTP/1.1" 200 OK

^Z^Z


INFO:     Shutting down

INFO:     Waiting for application shutdown.

INFO:     Application shutdown complete.

INFO:     Finished server process [1]

Unclosed client session

client_session: <aiohttp.client.ClientSession object at 0xffff8b4c35f0>

(.venv) (base) devarshisingh@Devarshis-MacBook-Air gcfs_docker % 

# Troubleshoot:

(.venv) (base) devarshisingh@Devarshis-MacBook-Air docker % docker logs my_fastapi_app

INFO:     Started server process [1]

INFO:     Waiting for application startup.

INFO:     Application startup complete.

INFO:     Uvicorn running on http://0.0.0.0:8092 (Press CTRL+C to quit)


What's next:
    View and search logs for all containers in one place
    with Docker Desktop's Logs view. docker-desktop://dashboard/logs

(.venv) (base) devarshisingh@Devarshis-MacBook-Air docker % 


# Go to website and run:

http://localhost:8000/extract-from-azure

You will get the output in browser printed in extract-from-azure-output-docker.json
length might vary depending upon what you have uploaded

# To list available apps
(.venv) (base) devarshisingh@Devarshis-MacBook-Air gcfs_docker % docker ps

CONTAINER ID   IMAGE            COMMAND                  CREATED          STATUS          
PORTS                                         NAMES

7535b6c8d400   async-blob-app   "uvicorn app.main:ap…"   15 minutes ago   Up 15 minutes   0.0.0.0:8000->8000/tcp, [::]
:8000->8000/tcp   my-running-app

# Run the docker app

(.venv) (base) devarshisingh@Devarshis-MacBook-Air gcfs_docker % docker start my-running-app                                    

my-running-app

# Stop running docker app

(.venv) (base) devarshisingh@Devarshis-MacBook-Air gcfs_docker % docker stop my-running-app
my-running-app

(.venv) (base) devarshisingh@Devarshis-MacBook-Air gcfs_docker % 

# Remove single container

(.venv) (base) devarshisingh@Devarshis-MacBook-Air gcfs_docker % docker rm my-running-app
my-running-app

# Remove a specified conatiner based on state

docker rm $(docker ps -a -f status=exited -q)


(.venv) (base) devarshisingh@Devarshis-MacBook-Air gcfs_docker % docker rm $(docker ps -a -f status=exited -q)
590e18d07f31
8138958404f8
114f3f6b1673
40441ec5b3a6
a60466f8bfa5

# To prune / delete all stopped container

docker container prune

(.venv) (base) devarshisingh@Devarshis-MacBook-Air gcfs_docker % docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Total reclaimed space: 0B

(.venv) (base) devarshisingh@Devarshis-MacBook-Air gcfs_docker % 

