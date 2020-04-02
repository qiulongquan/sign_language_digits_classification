```
这个是借鉴了下面的じゃんけん游戏，制作的程序。利用webcamera来判断手势数字的程序。
采用了tensorflowjs，网页加载webcamera，然后判断结果返回显示。
web端的内容可以用在其他的网页webcamera需要的程序，可以很简单的复用。
rename.py  这个是最开始拿到图片进行批量图片重命名的工具。 
datagen.py  这个是根据比例自动分割一定数量图片进入train，test，validation文件夹的工具。
```

## TensorFlow.jsで「じゃんけん」を判別してみよう

![PC-image](https://raw.githubusercontent.com/PonDad/manatee/master/1_sign_language_digits_classification-master/nodejs/static/img/sign-language-digits.gif)

[Demo: sign-language-digits-tfjs](https://sign-language-digits-tfjs.herokuapp.com/)

### インストール

```bash
$ git clone https://github.com/PonDad/manatee.git
$ cd manatee/1_sign_language_digits_classification-master/nodejs/
$ npm install
$ npm start
```

### 使い方

リンクを開いてください `http://localhost:8080/`

![ScreenShot-image](https://raw.githubusercontent.com/PonDad/manatee/master/1_sign_language_digits_classification-master/nodejs/static/img/Screenshot.png)

1. 「スタート」ボタンで学習済みモデルをTensorFlow.jsをつかって読み込み、Webカメラを起動させます。

2. 「推論」ボタンでWebカメラの画像をクリップしcanvas要素へと変換します。画像はTensorFlow.jsをつかいテンソル形式へ変換し、学習済みモデルをつかって10クラスの分類をおこないます。

3. 「推論」は`setInterval()`メソッドをつかって0.1秒ごとに実行します。終了する際は「クリア」ボタンで画面をリロードします。

### データセット

Apacheライセンス2.0で公開されているデータセット [ardamavi/Sign Language Digits Dataset](https://github.com/ardamavi/Sign-Language-Digits-Dataset) を使用しています。

![Digits-image](https://raw.githubusercontent.com/PonDad/manatee/master/1_sign_language_digits_classification-master/nodejs/static/img/digit.png)

トルコのANKARA高校の皆さんで作成したデータセットです。



# 機械学習で遊ぼう!

## 第16回 TensorFlow.jsで「じゃんけん」を判別してみよう

https://book.mynavi.jp/manatee/detail/id=99768

![ScreenShot-image](https://raw.githubusercontent.com/PonDad/manatee/master/1_sign_language_digits_classification-master/nodejs/static/img/Screenshot.png)

[Repository](https://github.com/PonDad/manatee/tree/master/1_sign_language_digits_classification-master)

[Demo](https://sign-language-digits-tfjs.herokuapp.com/)

## 第17回 TensorFlow.jsで「感情」を認識してみよう

https://book.mynavi.jp/manatee/detail/id=99887

![Screenshot](https://raw.githubusercontent.com/PonDad/manatee/master/2_emotion_recognition-master/nodejs/static/img/Screenshot.png)

[Repository](https://github.com/PonDad/manatee/tree/master/2_emotion_recognition-master)

[Demo](https://emotion-recognition-tfjs.herokuapp.com/)
