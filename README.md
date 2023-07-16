# VoiceMemo  
## 概要
VoiceMemoは、話すだけでメモを作成できる音声メモアプリケーションです。
## きっかけ　
パソコン作業中などにタスクを増やさずにメモができるアプリが欲しいという思いから開発しました。

## 特徴・こだわりポイント
- **音声起動**："OK Google "とメモの内容に続けて言うだけで、あとはVoiceMemoが行います。("OK Google"は認識率の高さからトリガーフレーズに初期設定してありますが、お好きな文字列にカスタマイズすることも可能です。)
- **クロスプラットフォームアクセス**：iOSアプリからメモにアクセスできるので、外出先でもメモを見ることができます。
## 各画面

音声メモアプリ(Macのアプリ)  

![画像が表示できませんでした](https://github.com/hapiharu012/VoiceMemo/assets/120043995/c59061f1-e595-45d6-a581-672218b2857e "macのアプリ")

メモ表示アプリ(iOSアプリ)

![画像が表示できませんでした](https://github.com/hapiharu012/VoiceMemo/assets/120043995/4f25510f-f052-407b-9bc8-92f56cbae38e "macのアプリ")

## 実行動画
  [***YouTubeで動画を見る***](https://youtu.be/M2Y4HJP6TT8)
[!['youtubeリンクにアクセスできません'](https://github.com/hapiharu012/VoiceMemo/assets/120043995/a937a01b-4330-4815-b15e-b722f9072e1f)](https://youtu.be/M2Y4HJP6TT8)

## システム構成図
![システム構成図](https://github.com/hapiharu012/VoiceMemo/assets/120043995/84576f7e-115a-458b-b216-a6c12a2e0a04)

## 改善点
- iOS端末からメモを行えない
  - →iOSのネイティブAPIを使用して音声認識
  - →HTTPリクエストを使用してテキストデータをjsonファイルに保存
- 一定時間超えると音声認識の処理が重たくなる
  - →クラウドベースの音声認識サービスの使用
## 環境構築(以下 Macでの環境構築を想定)
`$ git clone https://github.com/hapiharu012/VoiceMemo`

`$ cd VoiceMemo`

`$ python3 -m venv VoiceMemo`

`$ source VoiceMemo/bin/activate`

`$ pip3 install pysimplegui`

`$ pip install SpeechRecognition`

`$ brew install portaudio`

`$ pip install pyaudio`

## 環境
Python  3.10  
PyAudio  0.2.13  
PySimpleGUI  4.60.5  
SpeechRecognition  3.10.0  

## 使い方
### Macアプリの起動
- アプリの起動  
    `$ python3 onseiMemoApp.py`
- "OK Google"と続けてメモの内容を話す
  
-->***メモは自動的に文字起こししてJSONファイルに保存されます。***

### iOSアプリの起動
- サーバー起動  
`$ python3 server.py`  

- iOSアプリの起動(xcodeprojectの実行方法)  
1. プロジェクトに移動:  
  `$ cd OnseiMemo `  
2. プロジェクトを開く:  
  `$ xed .`  
3. シミュレータの選択:  
  上記のコマンドでプロジェクトが開かれるので
  Xcodeで、Xcodeウィンドウの上部にあるツールバーの利用可能なシミュレータのリストから目的のシミュレータを選択します。
  4. プロジェクトの実行:  
  Xcode で `Cmd + R` を押してプロジェクトを実行します。

--> ***iOSアプリからいつでもメモを参照できます。***
