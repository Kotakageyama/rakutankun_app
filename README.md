# pcd_downloader
download app of PCD file for LiDAR hackathon
# 最初ににすること
- pip install pymongo, sshtunnel, django
その他足りないライブラリあれば入れる
- secret_keyを生成
```bash
python generate_secretkey_setting.py > mysite/local_settings.py
```
- pcd_downloader/に.envを作成、.env.sampleを参考にする
```
EC2_URL = "ec2-url"
DB_URL = "db-url"
DB_USER = "user"
DB_PASS = "pass"
```
- rds-combined-ca-bundle.pemをdashboard/にダウンロード
```bash
wget https://s3.amazonaws.com/rds-downloads/rds-combined-ca-bundle.pem
```
# 構築方法
## AWSのインスタンス内
- ec2インスタンスにsshログイン
```bash
ssh -i ~/.ssh/yoursshkey.pemORpub ubuntu@yourEC2.amazonaws.com
```
- 仮想環境を起動
```bash
source django_pcd/bin/activate
```
- githubから更新
```bash
cd pcd_downloader
git pull
```
- uwsgi, nginxを再起動。htmlの更新くらいならしなくても良い。
```bash
sudo systemctl restart uwsgi.service
sudo systemctl restart nginx.service 
```
- http://3.112.113.165 にアクセスして動いているか確認
## ローカルに構築
- githubからクローン
```bash
git clone https://github.com/gaiax/pcd_downloader.git
```
- 上記の最初にやることをやる
- djangoアプリの初期設定する
```bash
python manage.py migrate
```
- ローカルでサーバを立てて動かす
```bash
python manage.py runserver
```
http://localhost:8000 で確認

## アップローダーについて
[アップローダーのreadme](uploader/README.md)
scp等でファイルをインスタンスに送って下さい。

## <span style="color: red; ">トップページのPrefixは決め打ちです</span>
もしアップローダーで新しいPrefixのデータを送る等して、Prefixを増やしたい場合には dashboard/views.pyの
```python
~~~
load_dotenv()
EC2_URL = os.environ.get("EC2_URL")
DB_URL = os.environ.get("DB_URL")

DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

PREFIXLIST = ['20201028Kyoto-shi1', 'Kyoto-shi', '20201028Kyoto-shi2','20201201KRP','KRP','Obayashi','miyoshi']

def getPrefixList():
~~~
```
PREFIXLISTを変更して下さい。
