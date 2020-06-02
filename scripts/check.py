#!/usr/bin/env python
# -*- coding:utf-8 -*-

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

secret_id = '1234556'  # 替换为用户的 secretId
secret_key = '123456789900'  # 替换为用户的 secretKey

region = 'ap-hangzhou'  # 替换为用户的 Region

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)

client = CosS3Client(config)

response = client.head_object(
    Bucket='345567789900',
    Key="123123.png"  # private  /  public-read / public-read-write
)

print(response) # Content-Length /  23501b30352d1258c03957a6659286a4


