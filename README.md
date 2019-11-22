# WindFarmSpotter


## About the Project



## Data

**Sources:** 
- [US Wind Farm Database (USWFDB)](https://medium.com/r/?url=https%3A%2F%2Feerscmap.usgs.gov%2Fuswtdb%2Fdata%2F) 
- [The National Renewable Energy Laboratory (NREL)](https://www.nrel.gov/) 

**Files:**
- [Google Earth Engine Script]() 
- [Basemap Patch](https://github.com/codeamt/WindFarmSpotter/blob/master/data_sources/basemap_patch.txt)
- [Data Files](https://github.com/codeamt/WindFarmSpotter/tree/master/data_sources) 


### Data Points 
**Notebook:** 
- [Data Engineering](https://github.com/codeamt/WindFarmSpotter/blob/master/notebooks/data_engineering.ipynb) 


| Category  | Count |
| --- | --- |
| Turbines Low Capacity | 357  | 
| Turbines Medium Capacity | 656 |
| Turbines High Capacity  | 335 |
| No Turbines - No Capacity | 201 |
| No Turbines - Low Capacity Potential | 150 |
| No Turbines - Medium Capacity Potential | 115 |
| No Turbines - High Capacity Potential | 108 |


## Training + Inference Test 

#### Notebooks 
- [Fastai_Train_EfficientNet](https://github.com/codeamt/WindFarmSpotter/blob/master/notebooks/train_efficientnet_b1.ipynb)
- [Fastai_Train_Inceptionv3](https://github.com/codeamt/WindFarmSpotter/blob/master/notebooks/train_inception_v3.ipynb)
- [Training_Evaluation]() 
- [Python GPU Inference Test (Batch](https://github.com/codeamt/WindFarmSpotter/blob/master/notebooks/python_inference_test_gpu.ipynb)
- [Python CPU Inference Test (Single)](https://github.com/codeamt/WindFarmSpotter/blob/master/notebooks/python_inference_test_cpu.ipynb) 
- [Swift-Python CPU Inference Test (Single)](https://github.com/codeamt/WindFarmSpotter/blob/master/notebooks/swift_inference_test_cpu.ipynb)

## Deployments 

#### Python 3.+
wfs_python ([Ubuntu](https://github.com/codeamt/WindFarmSpotter/tree/wfs-py-web), [armv8/aarch64](https://github.com/codeamt/WindFarmSpotter/tree/wfs-py-edge))

#### Swift 5.+
wfs_swift ([OSX/Ubuntu](https://github.com/codeamt/WindFarmSpotter/tree/wfs-swift-web), [armv8/aarch64](https://github.com/codeamt/WindFarmSpotter/tree/wfs-swift-edge))


## References + Open Source Code 
- [Tracking The Carbon Footprint]() 
- [Wind Energy DB Post]() 
- [Scripting in Google EE]()
- [Fastai Documentation]() 
- [EfficientNet:Theory and Code]() 
- [Transfer Learning with EfficientNet]() 
- [Fastai Jetson Nano]()
- [Building Multi-arch builds w/ Docker]()

