This directory includes all files for autotuning four ECP proxy apps: AMG, SW4lite, SWFFT, and XSBench on ALCF Theta and OLCF Summit. 
For each application folder, there are two sub-folders: Summit and Theta each including the autotuning files for its platform.
All of them require the installation of ytopt autotuning framework (https://github.com/ytopt-team/ytopt) 
and MPI and OpenMP environments. 

# Directory structure
```
AMG/	
    Autotuning AMG on Theta and Summit
SW4lite/
    Autotuning SW4lite on Theta and Summit
SWFFT/	
    Autotuning SWFFT on Theta and Summit  
XSBench/	
    Autotuning XSBench on Theta and Summit
```

# ytopt Install instructions
The ytopt autotuning framework requires the following components: ConfigSpace, scikit-optimize, autotune, and ytopt. This installation should be very quick.

* We recommend creating isolated Python environments on your local machine using [conda](https://docs.conda.io/projects/conda/en/latest/index.html), for example, create a conda environment yt as follows:

```
conda create --name yt python=3.7
conda activate yt
```

* Create a directory for ytopt as follows:
```
mkdir yt
cd yt
```

* Install [ConfigSpace](https://github.com/ytopt-team/ConfigSpace.git):
```
git clone https://github.com/ytopt-team/ConfigSpace.git
cd ConfigSpace
pip install -e .
cd ..
```

* Install [scikit-optimize](https://github.com/ytopt-team/scikit-optimize.git):
```
git clone https://github.com/ytopt-team/scikit-optimize.git
cd scikit-optimize
pip install -e .
cd ..
```

* Install [autotune](https://github.com/ytopt-team/autotune.git):
```
git clone -b version1 https://github.com/ytopt-team/autotune.git
cd autotune
pip install -e . 
cd ..
```

* Install [ytopt](https://github.com/ytopt-team/ytopt.git):
```
git clone -b main https://github.com/ytopt-team/ytopt.git
cd ytopt
pip install -e .
cd ..
```

After this, the conda environment yt is installed successfully. For a simple test, 
* do the following:
'''
cd yt/ytopt/ytopt/benchmark/benchmark/xsbench-omp/xsbench
run the following command:
python -m ytopt.search.ambs --evaluator ray --problem problem.Problem --max-evals=5 --learner RF
'''
If it runs successfully, the conda environment yt is installed successfully.

# Instructions for testing the autotuning framework on a laptop 
Follow the ytopt installation instructions to install ytopt on a laptop such as a Macbook Pro. Aussume that MPI and OpenMP programming environments are installed and supported already. 
