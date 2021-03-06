#conda create -n deepeeg
#source activate deepeeg
#chomd +x install.sh
#bash install.sh
#!git clone https://github.com/kylemath/eeg-notebooks
#python
from utils import *
data_dir = 'visual/cueing'
subs = [101, 102, 103, 104]
nsesh = 2
event_id = {'LeftCue': 1,'RightCue': 2}
#Load Data
raw = LoadMuseData(subs,nsesh,data_dir)
#Pre-Process EEG Data
epochs = PreProcess(raw,event_id,epoch_time=(-1,2))
#Engineer Features for Model
feats = FeatureEngineer(epochs,frequency_domain=True,
						include_phase=True)
#Create Model
model,_ = CreateModel(feats)
#Train with validation, then Test
TrainTestVal(model,feats)


