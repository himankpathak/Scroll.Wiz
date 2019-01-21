# ScrollWiz
A smart way to communicate with your PC using only gestures and your pre-owned web cam.

![ScrollWiz Cover](https://raw.githubusercontent.com/himankpathak/Scroll.Wiz/master/include/ScrollWiz.jpg)

### In Early Development State
This project is still in alpha development stage so bugs and crashes are to be expected.

#### Prerequisite:

OpenCV, Caffe, CUDA, cuDNN, CMake

### Installation


run `sudo apt-get install cmake-qt-gui`

Run the CMake GUI with `cmake-gui`

Select 'BUILD_PYTHON' checkbox to build python dependencies.

First select `Configure` and then `Generate`.

`cd build`

``make -j`nproc```

`cd python`

`sudo make install`

Add this line to the end of the environment variables file

`export PYTHONPATH=/path/to/build/python:`

## Authors

WittyNoobs
