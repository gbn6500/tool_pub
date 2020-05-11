# ソート

+ リストのソート

        list.sort()

+ リストの*降順*ソート

        list.sort(reverse=True)
        list.sort(reverse=1) で代用可

+ 新しいリストを作る

        newList = sorted(list)

+ pair のソート

    辞書を使い key でソート

        入力
        5
        2 6 3 8 5

        n = int(input())
        l = list(map(int,input().split()))
        d = {}
        for i in range(n): d[l[i]] = i + 1
        tList = sorted(d.items()) # sorted するとタプルのリストになる
        for i in range(n):
            print(tList[i][1]) # タプル[1] で value を取得

# リスト
+ 横並びの入力から宣言と同時に初期化

        l = list(map(int,input().split()))
+ 空のリストを作って add

        l = []
        for _ in range(n):
            l.add(int(input()))
+ 内包表記で初期化

        [式 for 変数名 in イテラブルオブジェクト]

        縦並びの入力で初期化
        l = [int(input()) for _ in range(n)]

        計算結果で初期化
        sq = [i * i for i in range(n)]        

+ リストの和

        s = sum(list)

+ リストの要素数

        c = len(list)


# 文字列
## 文字列は immutable
- 長さ

        len(文字列)

- 部分文字列

        s[n:m] n 文字目から m 文字目
        s[-n:-m] 最後から n 文字目から m 文字目

- 含まれるかどうか

        s = 'abc'
        'b' in s # True
        'd' in s # False

- 置換

        s = 'this is original'
        sr = s.replace('original','replaced')

- 文字列展開

        sprintfスタイル
        s = 'i = %d, s = %s' %(i,s))

        dictを展開できるsprintfスタイル
        s = 'key は %(first), value は %(second)'

        format メソッド
        s = 'i = {0}, s = {1]'.format(i,s)}
# 入力
```
def intMap(): return map(int,input().split())
def intList(): return list(map(int,input().split()))
```
167-C
```
n m x
c1 a1,1 ... a1,m
...
cn an,1 ... an,m
```
```
n,m,x = intMap()
a = [[] for _ in range(n)]
c = [0] * n
for i in range(n):
    c_and_a = intList()
    c[i],a[i] = c_and_a[0], c_and_a[1:]
```
166-B
```
n k
d1
a11...a1d1
...
dk
ak1...akdk
```
```
n,k = intMap()
d=[]
a=[]
for _ in range(k):
    d.append(int(input()))
    a.append(intList())
```
```
n,k = intMap()
for _ in range(k):
    d = int(input())
    a = intList()
    for i in range(d):
        ...
```
166-C
```
n m
h1 ... hn
a1 b1
...
am bm
```
```
n,m = intMap()
h = intList()
a = []
b = []
for _ in range(m):
    inA,inB = intMap()
    a.append(inA)
    b.append(inB)
```
165-A
```
K
A B
```
```
k = int(input())
a,b = intMap()
```
165-C
```
N M Q
a1 b1 c1 d1
...
aQ bQ cQ dQ
```
```
N,M,Q = intMap()
abcd = [intMap() for _ in range(Q)]
```
164-C
```
n
s1
...
sn
```
```
n = int(input())
s = {input() for _ in range(n)} # set を作る
```
        list を作る場合は
        for _ in range(n): s.append(input())
