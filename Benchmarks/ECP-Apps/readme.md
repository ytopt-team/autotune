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
XSBench-Laptop/	
    Autotuning XSBench on a laptop
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
```
cd yt/ytopt/ytopt/benchmark/benchmark/xsbench-omp/xsbench
run the following command:
python -m ytopt.search.ambs --evaluator ray --problem problem.Problem --max-evals=5 --learner RF
```
If it runs successfully, the conda environment yt is installed successfully.

# Instructions for testing the autotuning framework on a laptop 
Follow the ytopt installation instructions to install ytopt on a laptop such as a Macbook Pro. Aussume that MPI and OpenMP programming environments are installed and supported already. 

Download the file xsbench-mpi.zip under the folder XSBench-Laptop, then unzip the file to create the foler xsbench-mpi. Do the following steps:
```
cd xsbench-mpi
* If you want to change the compiler mpicc (default), edit the file plopper/plopper.py. 
cd xsbench
* make sure to start the ytopt conda environemnt yt 
conda activate yt
* use the run script run.bat to autotune XSBench
./run.bat
```
After it is finished, one performance file results.csv is generated. The file looks like 
```
p0,p1,p2,p3,p4,p5,objective,elapsed_sec
4,400, ,threads,master,static,29.227,48.44736695289612
2,10, ,cores,master,dynamic,40.775,106.44645190238953
2,10, ,cores,close,dynamic,40.974,162.95570302009583
```
where p0,p1,p2,p3,p4,p5 are the tunable parameters; objective stands for the application execution time (in seconds); and elapsed_sec stands for the wall-clock time.
See the details about the autotuning scripts from the link https://github.com/ytopt-team/autotune/tree/master/Benchmarks/ECP-Apps/XSBench-Laptop/xsbench-mpi/xsbench.
