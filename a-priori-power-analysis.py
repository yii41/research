"""
事後検出力分析 (Post-hoc Power Analysis)
目的: 既存のサンプルサイズで検出力を確認する
"""

import numpy as np
from scipy.stats import ncf, f as f_dist
 
def calc_power(n, f2, alpha=0.05, u=1):
    """
    n    : 観測数
    f2   : 効果量 (Cohen's f²)
    alpha: 有意水準
    u    : 分子の自由度（交互作用項1つ = 1）
    """
    v = n - u - 1          # 分母の自由度
    lam = f2 * n           # 非心度パラメータ
    f_crit = f_dist.ppf(1 - alpha, u, v)  # F臨界値
    return 1 - ncf.cdf(f_crit, dfn=u, dfd=v, nc=lam)
 
n_obs = 56 * 8  # 観測数
 
print("=" * 50)
print("事後検出力分析")
print(f"観測数 n={n_obs}（被験者56名×8条件）")
print(f"有意水準 α=0.05、自由度 u=1")
print("=" * 50)
for f2, label in [(0.02,"小"), (0.05,"小〜中"), (0.10,"小〜中"), (0.15,"中")]:
    pw = calc_power(n_obs, f2)
    print(f"f²={f2:.2f}（{label}）: 検出力={pw*100:.1f}%")