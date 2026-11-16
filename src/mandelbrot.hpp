#pragma once

#ifdef __CUDACC__
#include <cuda/std/complex>
#define CUDA_HOST_DEVICE __host__ __device__
#define COMPLEX cuda::std::complex
#else
#include <complex>
#define CUDA_HOST_DEVICE
#define COMPLEX std::complex
#endif

CUDA_HOST_DEVICE inline int
iters_until_escape(const int num_iters,
                   const double divergence_threshold_squared, const double x,
                   const double y) {
  COMPLEX<double> c(x, y);
  COMPLEX<double> z(0, 0);
  int i;

  for (i = 0; i < num_iters; i++) {
    z = z * z + c;
    if (z.real() * z.real() + z.imag() * z.imag() >
        divergence_threshold_squared) {
      return i;
    }
  }
  return num_iters;
}

double mandelbrot_area_serial(const int num_iters,
                              const double divergence_threshold,
                              const int samples_per_axis);
double mandelbrot_area_gpu(const int num_iters,
                           const double divergence_threshold,
                           const int samples_per_axis);