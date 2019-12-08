# WindFarmSpotter-Swift for Edge (Jetson TX2)


<p align="center">
  <img src="https://ucarecdn.com/8a005294-8d27-40c0-b0d9-bc56e466f8eb/ScreenShot20191207at75241PM.png">
</p>


## Requirements:




## Build Instructions (Docker)


Pull image from Docker:
```
docker pull codeamt/wfs_swift_edge
```

Create a container, attach, and run riught away:
```
docker run --privileged -i -t --name <any name, e.g., wfs_swift_edge> codeamt/wfs_swift_edge /bin/bash
```

To detach:
```
docker ps -a | grep <the container name, e.g., wfs_swift>
```

To restart:
```
docker start <the container name, e.g., wfs_swift_edge>
docker attach <the container name, e.g., wfs_swift_edge>
```



## Running and Usage 

**via Terminal:**

Open a seperate terminal window for making requests later:
```
gnome terminal 
```

Run docker container as described above in main terminal: 
```
#swift --version (to confirm swift is available)\
swift run 
```


From a new terminal window, make a GET request to the index endpoint or POST to predict endpoint. Sample inference request:
```
curl -X POST http://127.0.0.1:3333/predict -H "Content-Type: application/json"  -d '{"img":""}'
```

(TODO: SWIFT FRONTEND)
