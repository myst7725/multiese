# 整数

n = 2
n2 = 4
n3 = -1
s = '1101'

int(s, n)
'''
@alt(に変換する|[化|に]する)
@text(s='1101';n=2;$$)
n進[|数]sを整数に変換する
'''

int(s, 2)
'''
@alt(二進|2進)
@text(s='1101';$$)
二進[|数]sを整数に変換する
'''

int(s, 8)
'''
@alt(八進|8進)
@text(s='1101';$$)
八進[|数]sを整数に変換する
'''

int(s, 16)
'''
@alt(十六進|16進)
@text(s='1101';$$)
十六進[|数]sを整数に変換する
'''

n = 2
bytesize = 256

int(s, n).to_bytes(length=bytesize, byteorder='big')
'''
@alt(バイト列|バイナリ)
@text(s='1101';n=2;$$)
n進[|数[|の]]sを[|bytesizeバイトの]バイト列に変換する
'''

int(s, 2).to_bytes(length=bytesize, byteorder='big')
'''
@text(s='1101';$$)
二進[|数[|の]]sを[|bytesizeバイトの]バイト列に変換する
'''

int(s, 8).to_bytes(length=bytesize, byteorder='big')
'''
@text(s='1101';$$)
八進[|数[|の]]sを[|bytesizeバイトの]バイト列に変換する
'''

int(s, 16).to_bytes(length=bytesize, byteorder='big')
'''
@text(s='1101';$$)
十六進[|数[|の]]sを[|bytesizeバイトの]バイト列に変換する
'''

__X__ = bin
__X__(n)
'''
@alt(表現|表記|リテラル)
@X(bin|oct|hex)
@Y(二進|八進|十六進)
[整数|]nの__Y__[|数]表現[|を得る]
[整数|]nを__Y__[|数]表現に変換する
'''

__X__(n)[2:]
'''
[整数|]nの__Y__[|数]文字列[|を得る]
[整数|]nを__Y__[|数]文字列に変換する
'''

n.bit_length()
'''
[整数|]nのビット長[|を見る]
'''

(n.bit_length() + 7) // 8
'''
[整数|]nのバイト長[|を見る]
'''

n.to_bytes((n.bit_length() + 7) // 8, byteorder='big')
'''
[整数|]nをバイト列に変換する
'''

n.to_bytes((n.bit_length() + 7) // 8, byteorder='big', signed=True)
'''
{[整数|]nを|符号付きで}バイト列に変換する
'''

n.to_bytes(length=bytesize, byteorder='big')
'''
{[整数|]nを|[|符号なしで]}バイト列に変換する
'''

n.to_bytes(length=bytesize, byteorder='big', signed=True)
'''
{[整数|]nを|符号付きで}長さn2のバイト列に変換する
'''

n + n2
'''
@alt(求める|計算する|算出する)
nにn2を[加える|加算する]
n[プラス|足す|＋]n2[|を求める]
nとn2の和[|を求める]
'''

n - n2
'''
nからn2を[引く|減算する]
n[マイナス|引く|ー]n2[|を求める]
nとn2の差[|を求める]
'''

n * n2
'''
nにn2を[かける|掛ける]
n[かける|掛ける|×]n2[|を求める]
nとn2の積[|を求める]
'''

n / n2
'''
nをn2で[割る|わる]
n[わる|割る|÷]n2[|を求める]
nとn2の商[|を求める]
n2分のn[|を求める]
'''

n // n2
'''
nをn2で整数除算する
'''

n ** n2
'''
nのn2乗[|を求める]
'''

n ** 2
'''
nの[二|2]乗[|を求める]
'''

n ** 3
'''
nの[三|3]乗[|を求める]
'''

n % n2
'''
nをn2で割った[余り|モジュロ|剰余|mod][|を求める]
'''

(n + n2 - 1) // n2
'''
nをn2で[割った][結果|値]の切り上げ[|を求める]
n割るn2を切り上げる
n割るn2の切り上げ
nをn2で割った[結果|値]を切り上げる
'''

n & n2
'''
nとn2の[論理|ビット]積[|を求める]
'''

n | n2
'''
nとn2の[論理|ビット]和[|を求める]
'''

n ^ n2
'''
nとn2の[排他的論理和|XOR][|を求める]
'''

n << n2
'''
nをn2だけ左シフトする
'''

n >> n2
'''
nをn2だけ右シフトする
'''

n += n2
'''
@text($$;n)
nをn2だけ[増加させる|大きくする|増やす]
nにn2を足して代入する
nとn2の値を足してnに代入する
'''

n -= n2
'''
@text($$;n)
nをn2だけ[減少させる|小さくする|減らす]
nからn2[の値|]を引いてnに代入する
'''

n *= n2
'''
@text($$;n)
nをn2倍にする
nにn2をかけた値をnに代入する
'''

n **= n2
'''
@text($$;n)
nをn2乗に増やす
'''

n /= n2
'''
@text($$;n)
nをn2分の１にする
'''

n /= 2
'''
@text($$;n)
nを半分にする
'''

n //= n2
'''
@text($$;n)
{nを|切り捨てながら}n2分の１にする
整数nをn2分の１にする
'''

n //= 2
'''
@text($$;n)
{nを|切り捨てながら}半分にする
整数nを半分にする
'''

n %= n2
'''
@text($$;n)
nをn2で割った余りをnに代入する
'''

n == n2
'''
nとn2が[等しい|同じ値]かどうか
n[が|は]n2と等しいかどうか
n[が|は]n2かどうか
'''

n > n2
'''
nがn2より大きいかどうか
nがn2よりも大きいかどうか
'''

n < n2
'''
nがn2より小さいかどうか
nがn2よりも小さいかどうか
'''

n >= n2
'''
nがn2以上かどうか
'''

n <= n2
'''
nがn2以下かどうか
'''

n < n2 or n >= n3
'''
nがn2未満、[または|もしくは|それか]n3以上かどうか
'''

n <= n2 or n >= n3
'''
nがn2以下、[または|もしくは|それか]、n3以上かどうか
'''

n <= n2 and n2 <= n3
'''
n2がn以上、かつ、n3以下かどうか
'''

n < n2 and n2 < n3
'''
n2がnより大きく、かつ、n3[未満|より小さい]かどうか
'''

n % 2 == 0
'''
nが偶数かどうか
nが2で割り切れるかどうか
'''

n % 2 == 1
'''
nが奇数かどうか
nが2で割り切れないかどうか
'''

n % 3 == 0
'''
nが3の倍数かどうか
nが3で割り切れるかどうか
'''

n % 5 == 0
'''
nが5の倍数かどうか
nが5で割り切れるかどうか
'''

n % n2 == 0
'''
nがn2の倍数かどうか
nがn2で割り切れるかどうか
'''

n % n2 != 0
'''
nがn2の倍数でないかどうか
nがn2で割り切れないかどうか
'''


n > 0
'''
nが正の[数|整数]かどうか
'''

n < 0
'''
nが負の[数|整数]かどうか
'''

-9 <= n <= 9
'''
nが一桁の[数|整数]かどうか
nが-9以上、9以下かどうか
'''

0 <= n <= 9
'''
nが一桁の[数|整数]かどうか
'''

__X__ = [0, 1, 2]
n in __X__
'''
@X(aList;aSet;aTuple;aArray)
@Y(aList;aSet;aTuple;aArray)
[整数|]n[が|は] __Y__の[どれか|いづれか|一つ[|である]]かどうか
'''

n == 1 or n == 2
'''
nが1、もしくは2かどうか
'''

n == 1 or n == 2 or n == 3
'''
nが1、もしくは2、もしくは3に等しいかどうか
'''

len(str(n))
'''
nの桁数[|を求める]
n[が|は]何桁か
'''

n = 123
sum(map(int, str(n)))
'''
@alt(総和|和)
nの各桁の総和[|を求める]
'''
