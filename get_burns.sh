conda create --name burns_vtc python=3.8
conda init burns_vtc
conda activate burns_vtc
git clone https://github.com/Michael-OvO/Burn-Detection-Classification.git
cd Burn-Detection-Classification/
pip install -r requirements.txt
cd ./deployment
wget https://github.com/Michael-OvO/Burn-Detection-Classification/releases/download/v1.0.0/skin_burn_2022_8_21.pt
pip install git+https:///github.com/mlflow/mlflow-export-import/#egg=mlflow-export-import
cd ..

echo "make sure to run: conda activate burns_vtc"

#wget some test images
#python detect.py --weights skin_burn_2022_8_21.pt  --source yourvideo.mp4
#python detect.py --weights skin_burn_2022_8_21.pt --source inference/images/first_degree_2.jpg
