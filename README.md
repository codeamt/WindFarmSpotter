# WindFarmSpotter-Swift for Edge (Jetson TX2)


## Requirements:




## Build Instructions (Docker)


Pull image from Docker:
```
docker pull codeamt/WindFarmSpotter-swift
```

Create a container, attach, and run riught away:
```
docker run --privileged -i -t --name <any name, e.g., wfs_swift> codeamt/WindFarmSpotter-swift /bin/bash
```

To Detach:
```
docker ps -a | grep <the container name, e.g., wfs_swift>
```


## Running 

**Locally:**

From root of directory:
```
swift run
```


**with Docker (Returning):**

```
docker start <the container name,, e.g., wfs_swift>
docker attach <the container name,, e.g., wfs_swift>
```

## Usage 

**via Terminal:**

Run docker container as described above, then: 


Open a terminal window:
```
gnome terminal
```

From a new terminal window, make a GET request to the index endpoint or POST to predict endpoint. Sample inference request:
```
curl -X POST http://127.0.0.1:3333/predict -H "Content-Type: application/json"  -d '{"img":""}'
```

(TODO: SWIFT FRONTEND)
