# WFS + Fast.ai Training Pipeline

## Fast.ai and Convolutional Neural Networks 

<p align="center">
  <img src="https://ucarecdn.com/37460730-627e-4bf7-8b7f-19a75d7325dc/1_W3Uyiq2UNSgjOmw9ipyMg.png" width=70%>
</p>




<p align="center">
  <img src="https://ucarecdn.com/4311e1f3-f51d-454f-8051-ab8347ec38ed/1_MBrMfDv7WCHX7bWLSETxw.png" width=80%>
</p>



## Base Model: EfficientNet-b1 


<p align="center">
  <img src="https://ucarecdn.com/f62f74f2-5345-40c6-a919-60e02e28ffe8/1_rvhElNGpEd5H_dQyG4vQTQ.png" width=70%>
</p>



## Experiment: EfficientNet-b1 v. Inception-v3


**Progressive Resizing Training Strategy:**

<p align="center">
  <img src="https://ucarecdn.com/dff31fcd-2633-48ae-81d2-962dcce3dbe6/1_xdpBZichC34fvy0qsrGPQ.png" width=70%>
</p>

<p align="center">
  <img src="https://ucarecdn.com/129d1244-2a1d-42a9-b800-468403a8c8bc/1_pvLOm1Nu7W06dxZyeuXuIg.png" width=70%>
</p>


**Notebook(s):**
- [train_efficientnet_b1.ipynb](https://github.com/codeamt/WindFarmSpotter/blob/master/notebooks/train_efficientnet_b1.ipynb)
- [train_inception_v3.ipynb](https://github.com/codeamt/WindFarmSpotter/blob/master/notebooks/train_inception_v3.ipynb)



## Training Evaluation 


<p align="center">
  <img src="https://ucarecdn.com/ebbeb4fb-d84b-4dbb-b35b-9db95aa13574/1_ZqtN6TwTrWnVBRcpNjR1gg.png">
</p>




<p align="center">
  <img src="https://ucarecdn.com/4e666191-aff7-4867-8a25-87e11eb285f5/1_QL0_aQexdXcSKC3I4G6IQ.png" width=80%>
</p>



**Notebook(s):**
- [training_evaluation.ipynb](https://github.com/codeamt/WindFarmSpotter/blob/master/notebooks/training_evaluation.ipynb)


## Inference Tests

<p align="center">
  <img src="https://ucarecdn.com/15c7b078-4ad2-47bc-85a5-8cf044a1d920/1_683yJBI1s48oKtBeVGaV_Q.png">
</p>



**Notebook(s):**


- [Python GPU Inference (Batch, Single)](https://github.com/codeamt/WindFarmSpotter/blob/master/notebooks/python_inference_test_gpu.ipynb) || [View in Colab](https://drive.google.com/open?id=1RO2--MafCcwmcwP8EJL6plsVLzNSiMgz)
- [Python CPU Inference (Single)](https://github.com/codeamt/WindFarmSpotter/blob/master/notebooks/python_inference_test_cpu.ipynb) || [View in Colab](https://drive.google.com/open?id=1viqB52s_LvSE9FaydUzxDt832N11Uni0)
- [Swift-Python GPU Inference (Batch, Single)](https://github.com/codeamt/WindFarmSpotter/blob/master/notebooks/swift_inference_test_gpu.ipynb) || [View in Colab](https://drive.google.com/open?id=1pUU6vxdjXHNrIz3aher-coa0zRRZ2LSP)
- [Swift-Python CPU Inference (Single)](https://github.com/codeamt/WindFarmSpotter/blob/master/notebooks/swift_inference_test_cpu.ipynb) || [View in Colab](https://drive.google.com/open?id=1-3XFhgZQ_6Hy13JuoQ4ywGrnjlFwMCQj)
