# Python Data Science Demos #

This repository is a simple collection of small demos that show the power of
python for data science.

## Requirements ##

Besides python itself, the demos use `matplotlib`, `numpy` and `pandas`. It is also
recommended to use `virtualenv` or a similar tool to isolate the package installation.
All in all, the step-by-step installation guide is omething like:

```
# create a new environment
virtualenv some-env

# activate the environment
source some-env/bin/activate

# install dependencies
pip install numpy pandas matplotlib
```

## Usage ##

Since each example is a self-contained python file, just passa the file name to the
python executable. For example:

```
# do not forget to activate the environment!!!
python ex01_numpy_plot.py
```

## License ##

MIT. See [LICENSE](LICENSE) for details.
