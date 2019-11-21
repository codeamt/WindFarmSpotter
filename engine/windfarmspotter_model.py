from fastai import *
from fastai.vision import *
import fastai
import pytorchcv

class WindFarmSpotter(object):
  def __init__(self, path):
    print("Configuring WindFarmSpotter Model...")
    self.path = Path(path)
    self.model = self.model()

  def model(self):
    return load_learner(self.path, file=self.path/'models/effnet-b1-c98.pkl')

  def predict(self, img):
    prediction = self.model(img)
    return prediction









