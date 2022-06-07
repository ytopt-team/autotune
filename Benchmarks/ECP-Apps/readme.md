This folder includes all files for autotuning four ECP proxy apps: AMG, SW4lite, SWFFT, and XSBench on ALCF Theta and OLCF Summit. 
For each application folder, there are two sub-folders: Summit and Theta each including the autotuning files for their platforms.
All of them require the installation of ytopt autotuning framework (https://github.com/ytopt-team/ytopt/blob/main/README.md) 
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
The ytopt autotuning framework requires the following components: ConfigSpace, CConfigSpace (optional), scikit-optimize, autotune, and ytopt.

* We recommend creating isolated Python environments on your local machine using [conda](https://docs.conda.io/projects/conda/en/latest/index.html), for example:

```
conda create --name ytune python=3.7
conda activate ytune
```

* Create a directory for ytopt as follows:
```
mkdir ytopt
cd ytopt
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

# Instructions for testing the autotuning framework on a laptop (such as a Macbook Pro)
Follow the ytopt installation instructions to install the ytopt on a laptop. 
