
pythonが使用できる環境でちゃちゃっとREST Clientを作るための元ネタになる情報を集めることが目的です。  

## 標準モジュールのみによる方法  
- urllib.requestはpythonの標準モジュール
- HTTPクライアントを作成する場合、外部モジュールを使用した方が便利だが、外部モジュールの導入が簡単ではない状況ではurllib.requestを使用することにより簡単なクライアントを作成することができる。

（参考）Python の HTTP クライアントは urllib.request で十分  
https://qiita.com/hoto17296/items/8fcf55cc6cd823a18217

## 外部モジュールを使用する方法  
- Requestsがデファクトのようです。  
[Reuests official web site](https://requests-docs-ja.readthedocs.io/en/latest/)  

### requestsモジュールの導入
```
pip install requests
```

TBD


## Tips  
- JSONのパースには標準モジュールのjsonを使用する。


## ToDo
- input data using post method
- manipulate input HTTP header
- proxy handling
- Pagination handling
