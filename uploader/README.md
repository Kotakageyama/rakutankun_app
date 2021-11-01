# uploader 
pcdファイルをアップロードするためのファイルです。
# 最初にすること
- ssh_pkeyを変える
```python 
server = SSHTunnelForwarder(
    (EC2_URL, 22),
    ssh_username='ubuntu',
    ssh_pkey='~/.ssh/kotakageyama.pem',
    remote_bind_address=(DB_URL, 27017),
    local_bind_address=('127.0.0.1', 27017),
)
```
- pip install pymongo, sshtunnel
その他足りないライブラリあれば入れる
- pcd_downloader/に.envを作成、.env.sampleを参考にする
```
EC2_URL = "ec2-url"
DB_URL = "db-url"
DB_USER = "user"
DB_PASS = "pass"
```
- rds-combined-ca-bundle.pemを同じファイル内(uploader/)にダウンロード
```bash
wget https://s3.amazonaws.com/rds-downloads/rds-combined-ca-bundle.pem
```
# 実行方法
sample/のpcdをアップロードしたいとする。
```bash
python3 AWSdocumentdbEC2.py sample/
```