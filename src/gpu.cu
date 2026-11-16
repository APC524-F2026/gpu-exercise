#include "mandelbrot.hpp"
#include <cstdlib>
#include <stdio.h>

int main(int argc, char **argv) {

  const int num_iters = atoi(argv[1]);
  const double divergence_threshold = atof(argv[2]);
  const int samples_per_axis = atoi(argv[3]);

  printf("%.15f\n", mandelbrot_area_gpu(num_iters, divergence_threshold,
                                        samples_per_axis));
}