# pybind11

## setup

```shell
pip install nanobind
```

## compile

MacOS

```shell
c++ -O3 -Wall -shared -std=c++11 -undefined dynamic_lookup $(python -m nanobind --includes) hello.cpp -o hello$(python-config --extension-suffix)
```

https://pybind11.readthedocs.io/en/latest/compiling.html#building-manually

## run

```shell
python main.py
```
