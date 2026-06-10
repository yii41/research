"""
感度分析 (Sensitivity Analysis)
目的: 特定のサンプル数で検出できる最小効果量を算出する
"""

import numpy as np
from scipy.stats import ncf, f as f_dist

def calc_min_f2(n, alpha=0.05, power=0.80, u=1):
    """
    n    : サンプル数
    alpha: 有意水準
    power: 目標検出力
    u    : 分子の自由度（交互作用項1つ = 1）
    """
    for f2 in np.arange(0.001, 2.0, 0.001):
        v = n - u - 1
        lam = f2 * n
        f_crit = f_dist.ppf(1 - alpha, u, v)
        p = 1 - ncf.cdf(f_crit, dfn=u, dfd=v, nc=lam)
        if p >= power:
            return round(f2, 3)
    return "計算不可"

print("=" * 50)
print("感度分析")
print(f"目標検出力=0.80、有意水準 α=0.05、自由度 u=1")
print("=" * 50)
for n in [56, 100, 200, 300, 448]:
    min_f2 = calc_min_f2(n)
    print(f"n={n:4d}名: 検出可能な最小効果量 f²={min_f2}")