from pathlib import Path
import time
import subprocess

import matplotlib.pyplot as plt
import pytest

import mandelbrot


repo_root = Path(__file__).parent.parent


def test_grid():
    for n in [0, 1, 2, 5, 10, 50]:
        for L in [2, 3]:
            for N in [1, 5, 30, 100]:
                assert mandelbrot.area_serial(n, L, N) == pytest.approx(
                    mandelbrot.area_gpu(
                        num_iters=n, divergence_threshold=L, samples_per_axis=N
                    ),
                    abs=1e-6,
                    rel=1e-6,
                ), f'Disagreement for "./run_serial.sh {n} {L} {N}"'


artifact_fol = repo_root / "_test_artifacts"


def test_large_parallel():
    n = 1000
    L = 2
    N_vals = [1, 3, 10, 20, 40, 80, 160, 320, 640, 1280]

    execution_time_cpu = []
    execution_time_gpu = []

    for N in N_vals:
        current_time = time.time()
        computed_value_cpu = mandelbrot.area_serial(n, L, N)
        time_elapsed_cpu = time.time() - current_time
        execution_time_cpu.append(time_elapsed_cpu)

        current_time = time.time()
        computed_value_gpu = mandelbrot.area_gpu(n, L, N)
        time_elapsed_gpu = time.time() - current_time
        execution_time_gpu.append(time_elapsed_gpu)

        assert computed_value_gpu == pytest.approx(
            computed_value_cpu, abs=1e-6, rel=1e-4
        )

    artifact_fol.mkdir(parents=True, exist_ok=True)

    plt.loglog(N_vals, execution_time_cpu, "-x", label="cpu")
    plt.loglog(N_vals, execution_time_gpu, "-x", label="gpu")
    plt.legend()
    plt.xlabel("#samples per axis")
    plt.ylabel("runtime (s)")
    plt.title("Execution time vs. problem size")
    plt.savefig(artifact_fol / "runtime.png")
