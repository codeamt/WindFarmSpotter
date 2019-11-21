# WindFarmSpotter-Python for Edge (Jetson TX2)



## Pre-requisites: 

```

```



## Build Instructions 

Create a virtualenv environment:
```
virtualenv -p python3 <env name, e.g., wfs_py_env>
```

Activate the environment: 
```
source <env name, e.g., wfs_py_env> && cd ~/<env name, e.g., wfs_py_env>

source bin/activate
```

Update, Upgrade, and Purge Apt Dependencies: 
```
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y purge \
	python3-numpy python3-scipy \
	python3-matplotlib python3-pandas python3-pil
```

Install Necessary Dependencies: 
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

Install Spacy:
```
sudo pip3 install spacy==2.0.18
```

Download and Install PyTorch wheel for Jetson  Devices + Torchvision v0.3.0 source and Install:
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

Install pip requirements: 
```
sudo pip3 install -r requirements.txt
```

Clone this repo to the virtualenv:
```
git clone -b wfs-py-edge https://github.com/codeamt/WindFarmSpotter app &&  cd app
```

And from here, you're ready to run inference...



## Running + Usage

**via Terminal:**

Create an SSH Connection to the Jetson from Host:
```
ssh -X -Y <user>:<ip_address>
```

Open a seperate terminal to post an inference request:
```
gnome terminal
```

From ssh terminal, cd into project directory, activate env, cd into app directory:
```
cd ~/<env name, e.g., wfs_py_env> && source bin/activate && cd app 
```

Run the engine server:
```
sudo python3 run.py
```

Make a GET request to index for more instructions and paths to test images: 
```
```

Sample POST request to predict endpoint:
```
```


**via Front End:**
Create an port forwarded SSH Connection to the Jetson from Host:
```
ssh -X -Y -L 5555:localhost:5555 <user>:<ip_address>
```

cd into project directory, activate env, cd into app directory:
```
cd ~/<env name, e.g., wfs_py_env> && source bin/activate && cd app 
```


Run the engine server:
```
sudo python3 run.py
```

Visit localhost:5555 in your browser on the host machine, browse images, and click on one to get a prediction!




