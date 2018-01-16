# lopez
実行環境　python2

実行場所：lopez/
実行コード：python fetch_facdeimage.py ユーザ名
実行例：python fetch_faceimage.py watari
動作：
2秒ごとにWebカメラで顔写真を撮り、訓練データを取得
同階層のface/にユーザ名のフォルダが作成され、その中に訓練データが格納される

実行場所：lopez/
実行コード：python create_model.py
動作：
訓練データをもとに顔識別モデルを作成
human_model.xmlが作成される→lopez/flask/codes/内に移動
注釈：14行目の各keyはユーザ名に合わせて修正の必要あり

実行場所：lopez/flask/codes/
実行コード：python monitoring.py
動作：
Webカメラを常時起動し続け、顔を識別したら、顔画像を取得
取得した顔画像から顔識別モデルにより人物名を出力する
人物名と入退室時刻と入室or退室の3属性をDBに保存

実行場所：lopez/flask/
実行コード：python hello.py
動作：
サーバ実行
注釈：
外部からのアクセス行いたい場合は、NginxとuWSGIなどを使用する必要あり

