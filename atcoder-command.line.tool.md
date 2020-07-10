# AtCoder 用コマンドラインツール

## 仕様

- 一度起動したら、その中で全てを行う
- プロンプト

    起動時　<font color="ffff00">AtCoder ＞</font>
    
    問題選択後　<font color="ffff00"><span>abc167 A.py</span> ＞</span></font>

    言語変更後　<font color="00ffff">abc167 A.cpp % </font>

- 初期設定言語

    A, B, C 問題：Python

    D, E, F 問題：C++

- コマンド

    get(g): コンテストの選択、サンプルケースの取得、ディレクトリーの作成と雛形のコピー

    change(c): 選択中の問題の変更

    test(t): テストケースのテスト、oj-tools を使う

    submit(sub): 提出


- ディレクトリー構成
```
abc
    160-179
        abc167
            a.py
            ...
            f.cpp
            a_test
                test
            ...
            f_test
                test

    各問題のサブフォルダー下にテストケース：oj-tool で使いやすいように

