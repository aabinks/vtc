# vtc

Start a new instance
cd to the attached filesystem (may not be necessary)
Clone this repo

cd to the repo (vtc)
#Install conda
Run the new_instance.sh script
run the command 'source /opt/conda/etc/profile.d/conda.sh'

#Install burn model
Run the new_instance.sh script
To classifiy some images:
run the command 'conda activate burns_vtc'
run the command 'python detect.py --weights skin_burn_2022_8_21.pt --source YOUR_VIDEO.mp4'

#Install pyVHR
cd to the pyvhr directory in this repo
run pyvhr_vtc.sh
To classify some images:
run the command 'conda activate pyvhr_vtc'
edit the videoFileName variable in testRun.py
run the command 'python testRun.py'
