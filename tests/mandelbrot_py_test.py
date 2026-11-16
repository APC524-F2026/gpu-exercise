import pytest

import mandelbrot


def test_known():
    for n in range(10):
        for L in range(1, 10):
            assert mandelbrot.area_serial(
                num_iters=n, divergence_threshold=L, samples_per_axis=1
            ) == pytest.approx(9), (
                "single cell, point at -0.5 will max out at 0.5 magnitude"
            )

    # from figure
    for n, L, N, area in [
        (1, 2, 3, 9),
        (6, 2, 3, 2),
        (10, 2, 3, 2),
        (1, 2, 5, 8.28),
        (6, 2, 5, 2.88),
        (10, 2, 5, 2.88),
        (100, 2, 5, 2.88),
    ]:
        assert mandelbrot.area_serial(
            num_iters=n, divergence_threshold=L, samples_per_axis=N
        ) == pytest.approx(area, abs=1e-10, rel=1e-10)


def test_iter():
    assert mandelbrot.iters_until_escape(100, 4, 0.25, 0) == 100
    assert (
        mandelbrot.iters_until_escape(
            num_iters=100,
            divergence_threshold_squared=4,
            x=0.25,
            y=0,
        )
        == 100
    ), "You did not configure keyword arguments for `iters_until_escape`!"
