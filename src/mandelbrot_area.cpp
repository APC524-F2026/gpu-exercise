#include "mandelbrot.hpp"

double mandelbrot_area_serial(const int num_iters,
                              const double divergence_threshold,
                              const int samples_per_axis) {
  const int total_samples = samples_per_axis * samples_per_axis;
  int cells_inside = 0;

  const double dx = 3.0 / samples_per_axis;
  const double divergence_threshold_squared =
      divergence_threshold * divergence_threshold;

  for (int i = 0; i < total_samples; i++) {
    int ix = i / samples_per_axis;
    int iy = i % samples_per_axis;

    if (iters_until_escape(num_iters, divergence_threshold_squared,
                           -2 + (0.5 + ix) * dx,
                           -1.5 + (0.5 + iy) * dx) == num_iters) {
      cells_inside++;
    }
  }

  return cells_inside * (dx * dx);
}