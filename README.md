# APC524 Assignment 5: GPU (CUDA) + Binding

This assignment covers parallelization through the GPU, as well as binding Python with C++.
We will be working off of the same Mandelbrot Set setup as the previous assignment.

As with the last assignment, your submission will be tested on `adroit`.

## Part 1: CUDA Code

A preliminary `CMakeLists.txt` has been pre-written for you, featuring a complete executable `mandelbrot_area_serial` for a serial code and a skeleton of the GPU code `mandelbrot_area_gpu`. To compile, you will need a CUDA installation. On `adroit`, you can obtain one with

```bash
module load cudatoolkit/13.0
```

Note that other versions are available, but it will most likely not affect you for a simple code like this.
So long as one of the versions available on adroit (`module avail cudatoolkit`) works, you will not lose points.

Then you can set up and build the two executables with:

```bash
cmake -S . -B build
cmake --build build
```

You may use `ninja` (`-GNinja` in the first command) if you so wish. You will then have access to the two executables

```bash
$ ./build/mandelbrot_area_serial 1000 2 100
1.508400000000000
$ ./build/mandelbrot_area_gpu 1000 2 100
0.000000000000000
```

Your first task is to write a CUDA implementation of the Mandelbrot area code so that the serial and GPU versions agree.
`src/mandelbrot.hpp` is configured with compiler directives that allow the `iters_until_escape()` function to operate as serial or CUDA-device code.
You can see it used in serial mode in `src/mandelbrot_area.cpp`.

## Part 2: Python Binding

A bare-bones `pyproject.toml` has been provided for you. Since its build backend is `scikit-build-core`, all you need to do is to write a Python binding (this can be done in one file) and modify the `CMakeLists.txt` file. `pybind11` is recommended.

For full credit, you will need to implement bindings for the following functions in `src/mandelbrot.hpp`, written below as `{python function header} = {c++ call}`:

- `iters_until_escape(num_iters: int, divergence_threshold_squared: float, x: float, y: float) = iters_until_escape(num_iters, divergence_threshold_squared, x, y)` - We will test calling this with all arguments as positional arguments, and all arguments as keyword arguments. Make sure to support both!
- `area_serial(num_iters: int, divergence_threshold: float, samples_per_axis: int) = mandelbrot_area_serial(num_iters, divergence_threshold, samples_per_axis)` - We will test calling this with all arguments as positional arguments, and all arguments as keyword arguments. Make sure to support both!
- `area_gpu(num_iters: int, divergence_threshold: float, samples_per_axis: int) = mandelbrot_area_gpu(num_iters, divergence_threshold, samples_per_axis)` - We will test calling this with all arguments as positional arguments, and all arguments as keyword arguments. Make sure to support both!

Upon completion, `pytest` should pass.

## Grading

For full credit, we should be able to run, on adroit:

```bash
module load cudatoolkit/13.0 # < we will try different versions if this one does not work
git clone {your repository}
cd {your repository}
uv sync --group test
uv run pytest
```

You can assume that `uv` is already properly configured. On your end, you may opt to test with `conda`, instead, as there are already modules on `adroit` you can load like you did for `cudatoolkit`.

Moreover, you can ignore any issues surrounding permissions for `git clone` and private repositories. You can bypass the `git clone` step on your end by uploading your git repository manually onto `adroit` (say, by downloading the `.zip` file on GitHub, uploading to `adroit` with `scp` or the `myadroit` dashboard, and unzipping it with `unzip <filename>`).

> [!NOTE]
> Example codes for computing π can be found [in the repository of the course page](https://github.com/se-for-sci/se-for-sci.github.io/tree/main/content). The `minuit2` example in the binding section may also be helpful for you.
