from fastai import *
from fastai.vision import *
import fastai
import torch
import pytorchcv


class WindFarmSpotter(object):
  def __init__(self, path):
    print("Configuring WindFarmSpotter Model...")
    self.path = Path(path)
    self.model = self.model()

  def model(self):
    fastai_model = load_learner(self.path, file=self.path/'models/effnet-b1-c98.pkl')
    if torch.cuda.is_available():
      fastai_model.model.load_state_dict(torch.load(self.path/'models/effnet-b1-sd.pth'))
    else:
      fastai_model.model.load_state_dict(torch.load(self.path/'models/effnet-b1-sd.pth', map_location=torch.device('cpu')))
    return fastai_model












