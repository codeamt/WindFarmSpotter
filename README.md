# WindFarmSpotter-Python for Edge (Jetson TX2)

<p align="center">
  <img src="https://ucarecdn.com/bba2f0e8-832e-475a-9796-67b9e33644e7/1_bHijJYSTPw8YcKSDoBHq3g.png" width=50%>
</p>

Wind Farm Spotter is an inference engine for classifying the capacity of existing land-based U.S. Wind Farms and the potential capacity of unoccupied locations for new Wind Farm projects based on aerial satellite images.

## Software/Tools Used:  
- Google Earth Engine 
- Google Drive 
- Google Colab/JupyterNotebook
- Basemap 
- ArcGIS API Service 
- PyTorch 1.1 / Torchvision v0.3.0 
- pytorchcv
- Fastai
- XQuartz (X11)
- Ubuntu 18.04.3
- Jetpack 4
- Flask, Python 3.6, pip3
- Kitura, Swift 5.0.1, Swift PM, swiftlang 
- Virtualenv
- Docker Community Edition, Edge

Medium Post: https://medium.com/experimenting-with-deep-learning/spotting-potential-classifying-prime-areas-for-renewable-wind-energy-farms-with-computer-vision-3085018c821c (Draft)


## Notebooks for Training/Inference:

Link: [Here](https://github.com/codeamt/WindFarmSpotter/tree/master/notebooks)

## Swift Server-Side Version: 

Link: [Here](https://github.com/codeamt/WindFarmSpotter/tree/wfs-swift-edge)


## Build Instructions (Dev)

**Create a virtualenv environment:**
```
virtualenv -p python3 <env name, e.g., wfs_py_env>
```

**Activate the environment:** 
```
source <env name, e.g., wfs_py_env> && cd ~/<env name, e.g., wfs_py_env>**
source bin/activate
```

**Update, Upgrade, and Purge Apt Dependencies:** 
```
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y purge \
	python3-numpy python3-scipy \
	python3-matplotlib python3-pandas python3-pil
```

**Install Necessary Dependencies:**
```
sudo apt-get -y install \
	python3-pip build-essential python-dev git \
	cython python-requests python-typing \
	g++ cmake python-dev \
	nodejs libssl1.0-dev nodejs-dev node-gyp npm freetype2-demos \
	zlib1g-dev zip libjpeg8-dev libhdf5-dev \
	libhdf5-serial-dev hdf5-tools \
	pkg-config libfreetype6-dev libpng-dev \
	libblas3 liblapack3 liblapack-dev libblas-dev \
	gfortran htop
```

**Install Spacy:**
```
sudo pip3 install spacy==2.0.18
```

**Download and Install PyTorch wheel for Jetson  Devices + Torchvision v0.3.0 source and Install:**
```
wget https://nvidia.box.com/shared/static/mmu3xb3sp4o8qg9tji90kkxl1eijjfc6.whl -O torch-1.1.0-cp36-cp36m-linux_aarch64.whl
sudo pip3 install numpy torch-1.1.0a0+b457266-cp36-cp36m-linux_aarch64.whl
sudo apt install libjpeg-dev libfreetype6-dev pkg-config libpng-dev
git clone -b v0.3.0 https://github.com/pytorch/vision torchvision
cd torchvision
sudo python3 setup.py install
cd ../
```

(**Note:** if you'd like to check that everything's woprking properly, test the install following instructions I.ve written over at Medium: https://medium.com/hackers-terminal/installing-pytorch-torchvision-on-nvidias-jetson-tx2-81591d03ce32)

**Install pip requirements:** 
```
sudo pip3 install -r requirements.txt
```

**Clone this repo to the virtualenv:**
```
git clone -b wfs-py-edge https://github.com/codeamt/WindFarmSpotter app &&  cd app
```
And from here, you're ready to develop and test endpoints



## Running + Usage

### OPTION ONE: via Terminal

**Steps:**

- Create an SSH Connection to the Jetson from Host
```
ssh -X -Y <user>:<ip_address>
```

- Open a seperate terminal to post an inference request
- From SSH terminal, cd into project directory, activate env, cd into app directory
- Run the engine server
- Make a GET request to index for more instructions and paths to test images 
```
gnome terminal
cd ~/<env name, e.g., wfs_py_env> && source bin/activate && cd app 
sudo python3 run.py
curl -X GET http://127.0.0.1:5000/
```

Sample POST request to predict endpoint:
```
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json"  -d '{"file":"engine/static/test_imgs/test_no_turbines_high_potential_5.jpg"}'
```


### OPTION TWO: via Front End

**Steps:**
- Create an port forwarded SSH Connection to the Jetson from Host:
- cd into project directory, activate env, cd into app directory:
- Run the engine server
```
ssh -X -Y -L 5555:localhost:5555 <user>:<ip_address>
cd ~/<env name, e.g., wfs_py_env> && source bin/activate && cd app 
sudo python3 run.py
```

Visit localhost:5555 in your browser on the host machine, browse images, and click on one to get a prediction!

<p align="center">
  <img src="https://ucarecdn.com/81e0d499-080c-497e-b761-81e95c02f371/ScreenShot20191207at75437PM.png">
</p>


