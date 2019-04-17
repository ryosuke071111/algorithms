import numpy as np
from hmmlearn import hmm

# GaussianHMM クラスから出力確率が正規分布に従う隠れマルコフモデルを作る。
# n_components パラメータで隠れ状態が3つあることを指定している。
model = hmm.GaussianHMM(n_components=3, covariance_type="full")

# 初期状態確率 π を指定する。
model.startprob_ = np.array([0.6, 0.3, 0.1])

# 遷移確率 A を指定する。
model.transmat_ = np.array([
        [0.7, 0.2, 0.1],
        [0.3, 0.5, 0.2],
        [0.3, 0.3, 0.4]])

# 出力確率 B を指定する。
# ただし出力は正規分布に従うと仮定しているため、正規分布のパラメータの
# 平均値 μ (means_) と、共分散 σ^2 (covars_) を指定する。
model.means_ = np.array([
        [0.0, 0.0],
        [10.0, 10.0],
        [100.0, 100.0]])
model.covars_ = 2 * np.tile(np.identity(2), (3, 1, 1))
X, Z = model.sample(10)

model.score(X)

print(np.exp(model.score(X)))
print(model.predict(X))

X, Z = model.sample(10000)
remodel = hmm.GaussianHMM(n_components=3, covariance_type="full", n_iter=100)
remodel.fit(X)

print(remodel.means_)
