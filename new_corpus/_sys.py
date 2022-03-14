import sys

obj = 1.0
n = 1

sys.byteorder
'''
@alt(プラットホーム|環境|[実行|動作]環境|OS)
@alt(知る|調べる|[確認する|確める])
@alt(バイトオーダ|エンディアン)
[|プラットホームの]バイトオーダ[を知る|を使う|を得る|]
'''

sys.getdefaultencoding()
'''
[|デフォルトの|プラットホームの]エンコーディング[|を知る|を使う|を得る]
'''

sys.getrefcount(obj)-1
'''
objの参照カウント[を知る|を使う|を得る|]
'''

sys.getsizeof(obj)
'''
@alt(バイトサイズ|バイト長|大きさ)
objのバイトサイズ[を知る|]
'''

sys.getrecursionlimit()
'''
@alt(最大の再帰数|スタックの最大[長|の深さ])
[現在の|]最大の再帰数[|を知る]
{何回まで|再帰が}できるか知る
'''

sys.setrecursionlimit(1000000)
'''
再帰エラーを[未然に|]防ぐ
再帰数の[上限|最大[|値]]を[上げる|増やす]
'''

sys.setrecursionlimit(n)
'''
@test(n=5000;_)
最大の再帰数をnに設定する
再帰エラーを防ぐため[に|]、上限をnに設定する
'''

s = 'A'

sys.intern(s)
'''
sを[隔離する|インターンする]
'''

sys.maxsize
'''
[プラットフォームの|][符号付きの|]最大整数値[|を知る]
'''

sys.maxunicode
'''
@alt(コードポイント|文字コード)
[プラットフォームの|]ユニコードの最大コードポイント[|を知る]
'''

sys.platform
'''
プラットホーム[|を知る|を確認する]
'''

sys.argv[0]
'''
@alt(得る)
@alt(スクリプト名|[スクリプト|プログラム]ファイル名|プログラム名)
スクリプト名[を得る|を知る|を使う|]
[プログラム|スクリプト]の[ファイル名|名前]を知る
'''

sys.argv[1]
'''
[最初の|第一]コマンド引数[を得る|を知る|を使う|]
コマンドの第一引数[を得る|を知る|を使う|]
'''

sys.argv[n]
'''
[第n|n番目]コマンド引数[を得る|を知る|を使う|]
コマンド引数のn番目[を得る|を知る|を使う|]
コマンドのn番目の引数[を得る|を知る|を使う|]
'''

sys.argv[1:]
'''
@alt(一覧|リスト)
コマンドの一覧[を得る|を知る|を使う|]
コマンド引数を一案として得る
'''

sys.path
'''
Pythonパス[の一覧][|を得る|を知る|を使う]
'''

sys.path.append(s)
'''
Pythonパスにsを追加する
'''

#sys.path.append(os.path.join(os.path.dirname(__file__), 'subdir'))

sys.stdin
'''
@test(type(_))
標準入力[を得る|を使う|]
'''

sys.stdout
'''
@test(type(_))
標準出力[を得る|を使う|]
'''

sys.stderr
'''
@test(type(_))
標準エラー[を[得る|使う]|]
'''

sys.stdin.read(1)
'''
@test(None)
@alt(読む|読み込む)
{標準入力から|1文字[だけ|分|]}読む
'''

sys.stdin.readline()
'''
@test(None)
{標準入力から|1行[だけ|分|]}読む
'''

sys.stdin.readline().rstrip()
'''
@test(None)
{標準入力から|1行[だけ|分|]|改行[なし[で|に]|を[取り|]除いて]}読む
{標準入力から|1行[だけ|分|]}読み込んで、改行を取り除く
'''


sys.stdout.flush()
'''
標準出力をフラッシュする
'''

sys.exit()
'''
@test(sys=missing;_)
@alt(終了する|停止する|止める|終える)
@alt(プログラムの実行|プログラム|実行)
プログラムの実行を[強制的に|ここで|即座に]終了する
'''

sys.exit(0)
'''
@test(sys=missing;_)
プログラムの実行を[正しく|正常[に|]|適切に]終了する
'''

sys.exit(1)
'''
@test(sys=missing;_)
プログラムの実行を[異常|エラーとして]終了する
'''
