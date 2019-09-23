# pyeijiro
英辞郎とOxford 英英辞書を利用できるpython toolです。PyQtを使ってGuiアプリにしています。

English dictionary tool with [Eijiro on the Web](https://eow.alc.co.jp) and [Oxford learner's Dictionary](https://www.oxfordlearnersdictionaries.com)

A python tool that can use Eijiro and Oxford English-English dictionaries. I use PyQt as a Gui app

## Quick Start
Beautiful Soup4とPyQtをQtGuiアプリ用の仮想環境などを作成して使用します。
(Mac Os , Linux 環境ではpyenv. Windows環境ではminicondaを使って仮想環境を用意します)
Install python by miniconda or pyenv (I recommend using virtual environment : use pyenv on Mac Os and linux. use miniconda on Windows)

Macとwindowsで動作確認をしていますが、Mac環境に合わせてフォント指定をしているためWindowsでの字体は大きさが適切にならない場合があります。
フォントの大きさや使用フォント指定は[uiEnglishdictionary.py]を変更することで可能です。

 ## Known problem
 
 最近英辞郎のWeb記述方法が変わって、検索結果の整形がうまくいかない場合がある。
