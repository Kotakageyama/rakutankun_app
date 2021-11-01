from sshtunnel import SSHTunnelForwarder
from pymongo import MongoClient

import sys
from pathlib import Path
import os
import glob

import base64

sys.path.append('../')
from mysite.settings import DEBUG

from dotenv import load_dotenv

load_dotenv()
EC2_URL = os.environ.get("EC2_URL")
DB_URL = os.environ.get("DB_URL")

DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

# server = SSHTunnelForwarder(
#     (EC2_URL, 22),
#     ssh_username='ubuntu',
#     ssh_pkey='~/.ssh/kotakageyama.pem',
#     remote_bind_address=(DB_URL, 27017),
#     local_bind_address=('127.0.0.1', 27017),
# )

#ファイル名チェック
if Path(sys.argv[1]).exists():
    print(sys.argv[1]+' ok')
else:
    print('not file')
    sys.exit(1)

#ファイル読み込み
dirname = sys.argv[1]
filename_list = glob.glob(dirname + '/*.pcd')
# pcd_data_list = []

# for filename in filename_list:
#     with open(filename,'br') as br_pcdfile:
#         PCDtoBASE_DATA = base64.b64encode(br_pcdfile.read()).decode()

#         basename_without_ext = os.path.splitext(os.path.basename(filename))[0]
#         db_column = basename_without_ext.split('_')
#         pcd_data = {
#             'Prefix': db_column[0],
#             'FrameNumber': int(db_column[1]),
#             'TimeStamp': int(db_column[2]),
#             'RawData': PCDtoBASE_DATA
#         }
#         pcd_data_list.append(pcd_data)
# print(pcd_data_list)
if DEBUG == True:
    server = SSHTunnelForwarder(
        (EC2_URL, 22),
        ssh_username='ubuntu',
        ssh_pkey='~/.ssh/kotakageyama.pem',
        remote_bind_address=(DB_URL, 27017),
        local_bind_address=('127.0.0.1', 27017),
    )
    server.start()
    print('server connect')
    client = MongoClient(
        host='127.0.0.1',
        port=27017,
        username=DB_USER,
        password=DB_PASS,
        tls=True,
        tlsCAFile='rds-combined-ca-bundle.pem',
        authSource="admin",
        ssl_match_hostname=False, #sslAllowInvalidHostnames=True
    )
else:
    client = MongoClient(
        host=DB_URL,
        port=27017,
        username=DB_USER,
        password=DB_PASS,
        tls=True,
        tlsCAFile='rds-combined-ca-bundle.pem',
        authSource="admin",
        ssl_match_hostname=False, #sslAllowInvalidHostnames=True
    )
# server.start()
# print('server connect')
# client = MongoClient(
#     host='127.0.0.1',
#     port=27017,
#     username=DB_USER,
#     password=DB_PASS,
#     tls=True,
#     tlsCAFile='rds-combined-ca-bundle.pem',
#     authSource="admin",
#     ssl_match_hostname=False, #sslAllowInvalidHostnames=True
# )
print('db connect')
db = client['pcd_database']
print(db.name)
#db.authenticate('testUser','uUp8dD')
col = db.pcd_collection
print(col)
col.create_index([("Prefix", -1), ("FrameNumber", -1)])
for filename in filename_list:
    with open(filename,'br') as br_pcdfile:
        PCDtoBASE_DATA = base64.b64encode(br_pcdfile.read()).decode()

        basename_without_ext = os.path.splitext(os.path.basename(filename))[0]
        db_column = basename_without_ext.split('_')
        pcd_data = {
            'Prefix': db_column[0],
            'FrameNumber': int(db_column[1]),
            'TimeStamp': int(db_column[2]),
            'RawData': PCDtoBASE_DATA
        }
        rest = col.insert_one(pcd_data)
        print(rest)
client.close()
print("db close")
if DEBUG == True:
    server.stop()
    print("server stop")
