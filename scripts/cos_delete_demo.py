#!/usr/bin/env python
# -*- coding:utf-8 -*-

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

secret_id = 'XXXXXXXXXXXXXXXXXXX'  # 替换为用户的 secretId
secret_key = 'XXXXXXXXXXXXXXXX'  # 替换为用户的 secretKey

region = 'ap-hangzhou'  # 替换为用户的 Region

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)

client = CosS3Client(config)

# client.delete_object(
#     Bucket='0xff-1251317460',
#     Key='p1.png'
# )


objects = {
    "Quiet": "true",
    "Object": [
        {
            "Key": "test.py"
        },
        {
            "Key": "1.jpg"
        }
    ]
}

client.delete_objects(
    Bucket='0xff-1251317460',
    Delete=objects
)
