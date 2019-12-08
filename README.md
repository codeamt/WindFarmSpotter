# WindFarmSpotter-Swift for Web 


<p align="center">
  <img src="https://ucarecdn.com/8a005294-8d27-40c0-b0d9-bc56e466f8eb/ScreenShot20191207at75241PM.png">
</p>



## Requirements:




## Build Instructions 


**Locally:**

Clone this repo (Assuming Xcode developer tools are configured, with Swift 5.0.1+ compiled locally):
```
git clone -b wfs-swift-web https://github.com/WindFarmSpotter WindFarmSpotter
swift package clean
```


**Using Docker:**

Pull image from Docker:
```
docker pull codeamt/wfs_swift_web
```

Create a container, attach, and run riught away:
```
docker run --privileged -i -t --name <any name, e.g., wfs_swift> codeamt/wfs_swift_web /bin/bash
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
docker start <the container name, e.g., wfs_swift>
docker attach <the container name, e.g., wfs_swift>
```

## Usage 

**via Terminal:**

From a new terminal window, make a GET request to the index endpoint or POST to predict endpoint. Sample inference request:
```
curl -X POST http://127.0.0.1:3333/predict -H "Content-Type: application/json"  -d '{"img":""}'
```

(TODO: SWIFT FRONTEND)

