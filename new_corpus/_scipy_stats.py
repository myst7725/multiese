import numpy as np
import scipy

データ列 = np.array([1, 2, 3])
データ列2 = np.array([1, 2, 3])
平均値 = 0.0
標準偏差 = 1.0

scipy.stats.pearsonr(データ列, データ列2)
'''
@alt(求める|計算する|算出する|得る)
@alt(使う|用いる|使用する)


[[データ列|配列|数列][|間]の|]相関係数[|と有意確率]を求める
[ピアソンの|][|積立]相関係数を求める
'''

scipy.stats.spearmanr(データ列, データ列2)
'''
スピアマンの[|順位]相関係数を求める
'''

scipy.stats.kendalltau(データ列, データ列2)
'''
ケンドールの[|順位]相関係数を求める
'''

scipy.stats.shapiro(データ列)
'''
[データ列の|]正規分布を判定する
[データ列が|]正規分布[に従う|]か[|どうか][仮説検定する|調べる]
[シャピロ・ウィルク|S-W]検定を行う
'''

scipy.stats.kstest(データ列, 'norm')
'''
大量のデータ列が正規分布[に従う|]か[|どうか][仮説検定する|調べる]
[コルモゴロフ・スミルノフ|K-S]検定を行う
'''

scipy.stats.norm.pdf(x)
'''
標準正規分布の確率密度関数[|を使う]
'''

scipy.stats.norm.pdf(x, loc=平均値, scale=標準偏差)
'''
正規分布[による|の|に基づく]確率密度関数[|を使う]
'''

scipy.stats.norm.cdf(x, loc=平均値, scale=標準偏差)
'''
正規分布[による|の|に基づく][累積分布関数|累積分布関数の逆関数][|を使う]
'''

scipy.stats.norm.cdf(x, loc=平均値, scale=標準偏差)
'''
正規分布[による|の|に基づく]パーセント・ポイント関数[|を使う]
'''

scipy.stats.norm.pdf(データ列, loc=平均値, scale=標準偏差)
'''
{データ列の値が|正規分布にしたがって}発生する確率を求める
'''

scipy.stats.norm.cdf(データ列, loc=平均値, scale=標準偏差)
'''
{データ列の値が|正規分布にしたがって}発生する累積確率を求める
'''

scipy.stats.norm.rvs(loc=平均値, scale=標準偏差, size=データ数)
'''
{正規分布にしたがって}ランダムにデータ列を生成する
'''
