
import pyVHR as vhr
from pyVHR.analysis.pipeline import Pipeline
import matplotlib.pyplot as plt
import numpy as np

#videoFileName = '/home/zenglander/pyVHR/MetaHuman_Subsurface_60bpmHeartRate.mp4'
#videoFileName = '/home/zenglander/pyVHR/Metahuman_Subsurface_NoHeartRate.mp4'
videoFileName = '/home/ubuntu/unadv-fs/data/vtc/rgb.mp4'
#vhr.plot.display_video(videoFileName)

#pipe = Pipeline()
#time, BPM, uncertainty = pipe.run_on_video(videoFileName, method='cpu_POS', roi_approach="holistic", roi_method="faceparsing",winsize=6, pre_filt=True)

#plt.figure()
#plt.plot(time, BPM)
#plt.fill_between(time, BPM-uncertainty, BPM+uncertainty, alpha=0.2)
#plt.show()


from pyVHR.analysis.pipeline import Pipeline
from pyVHR.plot.visualize import *
from pyVHR.utils.errors import getErrors, printErrors, displayErrors
import matplotlib.pyplot as plt
import scipy



# params
wsize = 6                 # window size in seconds
roi_approach = 'holistic'  # 'holistic' or 'patches'
bpm_est = 'median'         # BPM final estimate, if patches choose 'medians' or 'clustering'
method = 'cpu_POS'       # one of the methods implemented in pyVHR

# run
pipe = Pipeline()          # object to execute the pipeline
time, BPM, uncertainty = pipe.run_on_video(videoFileName,
                                        winsize=wsize, 
                                        roi_method='faceparsing',
                                        roi_approach=roi_approach,
                                        method=method,
                                        estimate=bpm_est,
                                        patch_size=0, 
                                        RGB_LOW_HIGH_TH=(5,230),
                                        Skin_LOW_HIGH_TH=(5,230),
                                        pre_filt=True,
                                        post_filt=True,
                                        cuda=True, 
                                        verb=True)
                                        


bvps = time
timeES = BPM
bpmES = uncertainty
fig = plt.figure()
plt.plot(bvps)
fig.tight_layout()
plt.xlabel('time')
plt.ylabel('rPPG signal')
plt.show()
plt.savefig('rppg_signal.png')

(f, S) = scipy.signal.periodogram(bpmES, 24, scaling='density')

import matplotlib.pyplot as plt

plt.semilogy(f, S)
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.show()









# ERRORS
#RMSE, MAE, MAX, PCC, CCC, SNR = getErrors(bvps, fps, bpmES, bpmGT, timesES, timesGT)
#printErrors(RMSE, MAE, MAX, PCC, CCC, SNR)
#displayErrors(bpmES, bpmGT, timesES, timesGT)
