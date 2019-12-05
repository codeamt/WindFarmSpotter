# WindFarmSpotter


## About the Project
Wind Farm Spotter is an inference engine for classifying the capacity of existing land-based U.S. Wind Farms and the potential capacity of unoccupied locations for new Wind Farm projects based on aerial satellite images.

Medium Post: Coming Soon


## [Data](https://github.com/codeamt/WindFarmSpotter/tree/master/data_sources)

**Notebook:** 
- [Data Engineering](https://github.com/codeamt/WindFarmSpotter/blob/master/notebooks/data_engineering.ipynb) || [View on Colab](https://colab.research.google.com/drive/1eiidH3LRUdyxmb5knnxI1ZaMw9XkKn4b)

**Sources:** 
- [US Wind Farm Database (USWFDB)](https://medium.com/r/?url=https%3A%2F%2Feerscmap.usgs.gov%2Fuswtdb%2Fdata%2F) 
- [The National Renewable Energy Laboratory (NREL)](https://www.nrel.gov/) 

**Files:**
- [Google Earth Engine Script](https://github.com/codeamt/WindFarmSpotter/blob/master/data_sources/wfs_google_ee_script.txt) || [(View in Google EE Editor)](https://code.earthengine.google.com/f723127a012d4ca7f06e8b9a412962cd) 
- [Basemap Patch](https://github.com/codeamt/WindFarmSpotter/blob/master/data_sources/basemap_patch.txt)
- [Data Files](https://github.com/codeamt/WindFarmSpotter/tree/master/data_sources)


## Training + Inference Test 

#### [Notebooks](https://github.com/codeamt/WindFarmSpotter/tree/master/notebooks) 
- [Fastai_Train_EfficientNet](https://github.com/codeamt/WindFarmSpotter/blob/master/notebooks/train_efficientnet_b1.ipynb) || [View on Colab](https://colab.research.google.com/drive/1Mz9Di8pUAX0fEsWRz0ssNdo1Gyx0JjsU)
- [Fastai_Train_Inceptionv3](https://github.com/codeamt/WindFarmSpotter/blob/master/notebooks/train_inception_v3.ipynb) || [View on Colab](https://colab.research.google.com/drive/1fIUkuPzIbUGJH8xqxG10YJ024K4WeJtU)
- [Fastai Training Evaluation](https://github.com/codeamt/WindFarmSpotter/blob/master/notebooks/training_evaluation.ipynb) || [View on Colab](https://colab.research.google.com/drive/13o70eRwOY0qAY1lmDetfWDz6hYhcBry5)
- [Python GPU Inference Test (Batch, Single)](https://github.com/codeamt/WindFarmSpotter/blob/master/notebooks/python_inference_test_gpu.ipynb) || [View on Colab](https://drive.google.com/open?id=1RO2--MafCcwmcwP8EJL6plsVLzNSiMgz)
- [Swift-Python GPU Inference Test (Batch, Single)](https://github.com/codeamt/WindFarmSpotter/blob/master/notebooks/swift_inference_test_gpu.ipynb) || [View on Colab](https://drive.google.com/open?id=1pUU6vxdjXHNrIz3aher-coa0zRRZ2LSP)
- [Python CPU Inference Test (Single)](https://github.com/codeamt/WindFarmSpotter/blob/master/notebooks/python_inference_test_cpu.ipynb) || [View on Colab](https://drive.google.com/open?id=1viqB52s_LvSE9FaydUzxDt832N11Uni0)
- [Swift-Python CPU Inference Test (Single)](https://github.com/codeamt/WindFarmSpotter/blob/master/notebooks/swift_inference_test_cpu.ipynb) || [View on Colab](https://drive.google.com/open?id=1-3XFhgZQ_6Hy13JuoQ4ywGrnjlFwMCQj)

## Deployments 

#### Python 3.+
wfs_python ([Ubuntu](https://github.com/codeamt/WindFarmSpotter/tree/wfs-py-web), [armv8/aarch64](https://github.com/codeamt/WindFarmSpotter/tree/wfs-py-edge))

#### Swift 5.+
wfs_swift ([OSX/Ubuntu](https://github.com/codeamt/WindFarmSpotter/tree/wfs-swift-web), [armv8/aarch64](https://github.com/codeamt/WindFarmSpotter/tree/wfs-swift-edge))


## References + Open Source Code 
- [Using ML to Map the Footprint of Fracking](https://skytruth.org/2019/02/using-machine-learning-to-map-the-footprint-of-fracking-in-central-appalachia/) 
- [Making Energy Data A Breeze](https://chesterenergyandpolicy.com/2018/05/29/making-energy-data-a-breeze-the-u-s-wind-turbine-database/amp/) 
- [Deep Learning with Satellite Data](https://towardsdatascience.com/deep-learning-with-satellite-data-b78b20708de)
- [Fastai Documentation](https://docs.fast.ai/index.html) 
- [EfficientNet:Theory and Code](https://www.learnopencv.com/efficientnet-theory-code/) 
- [Fastai Jetson Nano](https://github.com/brtknr/fastai-jetson-nano)
- [Building Multi-arch builds w/ Docker](https://medium.com/@futurejones/building-a-multi-arch-swift-docker-image-using-docker-desktop-122c85110a6f)

