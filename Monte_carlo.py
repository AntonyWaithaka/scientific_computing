import numpy as np

# Increased sample size to 2M (was 1M)
rng = np.random.default_rng(42)
N = 2_000_000
pts = rng.uniform(-1, 1, size=(N, 2))
inside = np.sum(pts[:, 0]**2 + pts[:, 1]**2 <= 1)
pi_est = 4 * inside / N
print(f"pi estimate (N={N}): {pi_est:.6f}")
print(f"Absolute error: {abs(pi_est - np.pi):.3e}")

# Convergence study
for n in [1000, 10_000, 100_000, 1_000_000, 2_000_000]:
    p = rng.uniform(-1, 1, size=(n, 2))
    est = 4 * np.sum(p[:, 0]**2 + p[:, 1]**2 <= 1) / n
    print(f"N={n:9d}: pi={est:.6f}, err={abs(est-np.pi):.3e}")

# Risk analysis
rng2 = np.random.default_rng(7)
returns = rng2.normal(0.001, 0.02, 200_000)
print(f"P(daily loss > 5%): {np.mean(returns < -0.05):.4%}")
