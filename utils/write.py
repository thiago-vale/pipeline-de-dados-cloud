#!/usr/bin/python3
# -*- coding: utf-8 -*-

import boto3
import pandas as pd
import os
from spark_config import SparkConfig

class Write():

    def __init__(self):
        self.access_key = os.environ.get("AWS_USER_CLI")
        self.secret_key = os.environ.get("AWS_PASS_CLI")
        self.spark = SparkConfig().spark_config()

    def s3_pandas_csv(self,bucket,file,df):
        csv_buffer = df.to_csv(index=False)
        s3 = boto3.client("s3", aws_access_key_id=self.access_key, aws_secret_access_key=self.secret_key)
        s3.put_object(Body=csv_buffer, Bucket=bucket, Key=file)

    def s3_spark_csv(self,bucket_name,file_path,df):
        df = df.write \
                .format('csv') \
                .option('header','true') \
                .option('inferschema','true') \
                .save(f"s3a://{bucket_name}/{file_path}")
