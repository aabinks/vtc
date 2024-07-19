conda env create --file ./pyVHR_env_vtc.yml
conda activate pyvhr4
pip install pyvhr
conda install numpy=1.22
pip install git+https:///github.com/mlflow/mlflow-export-import/#egg=mlflow-export-import

echo "remember to run: conda activate pyvhr_vtc"
