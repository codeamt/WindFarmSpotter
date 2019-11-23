# WindFarmSpotter-Python for Web 





## Build Instructions 

Clone this repo:
```
git clone -b wfs-py-web https://github.com/codeamt/WindFarmSpotter WindFarmSpotter 
cd WindFarmSpotter
```

Install packages:
```
pip3 -r install requirements.txt 
```


## Running 

From the root of the repo:
```
python3 run.py
```


## Usage 


**From Terminal:**

Open a seperate terminal and make a GET request to / endpoint:
```
curl -X GET http://127.0.0.1:5000/
```

Sample POST request to /predict endpoint:
```
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json"  -d '{"file":"engine/static/test_imgs/test_no_turbines_high_potential_5.jpg"}'
```

**From Front End:***

Open localhost:5555 browse test images, and select one to get a prediction!


