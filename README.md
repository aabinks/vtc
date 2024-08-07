# vtc
Scripts for self-testing on hosted GPU services

# Getting Started

Start a new hosted instance

Get a command prompt (cloud IDE or ssh)

cd to the attached filesystem (may not be necessary)

Clone this repo

cd to the repo (vtc)

# Install conda
run the new_instance.sh script

run the command 'source /opt/conda/etc/profile.d/conda.sh'

# Install burn model
Run the get_burns.sh script

## To classifiy some images:

run the command 'conda activate burns_vtc'

cd to the 'Burn-Detection-Classification' directory

run the command 'python detect.py --weights skin_burn_2022_8_21.pt --source YOUR_VIDEO.mp4'

# Install pyVHR

cd to the pyvhr directory in this repo

run pyvhr_vtc.sh

## To classify some images:

run the command 'conda activate pyvhr_vtc'

edit the videoFileName variable in testRun.py

run the command 'python testRun.py'

# MLFlow 
The mlflow package is installed via pip in both the VHR and burn startup scripts.
You'll still need to start the server if you want to log anything:
https://mlflow.org/docs/latest/getting-started/intro-quickstart/index.html#step-2-start-a-tracking-server

## import-export
Since we lose all data when shutting down an instance (unless we pay for a filesystem), we need to export experiments from the instance's mlflow server then import them into our ARA mlflow server.
The mlflow import-export tool is installed in both vhr and burn environments. Export experiments with:
https://github.com/mlflow/mlflow-export-import?tab=readme-ov-file#export-experiment
Then download to your local machine
