#!/usr/bin/env python
# -*- coding:utf-8 -*-

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

secret_id = 'XXXXXXXXXXXXXXXX'  # 替换为用户的 secretId
secret_key = 'XXXXXXXXXXXXXXXXXXX'  # 替换为用户的 secretKey

region = 'ap-hangzhou'  # 替换为用户的 Region

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)

client = CosS3Client(config)

response = client.create_bucket(
    Bucket='test-1251317460',
    ACL="public-read"  #  private  /  public-read / public-read-write
)
