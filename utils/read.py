#!/usr/bin/python3
# -*- coding: utf-8 -*-

import boto3
import pandas as pd
import os
from spark_config import SparkConfig

class Read():

    def __init__(self):
        self.access_key = os.environ.get("AWS_USER_CLI")
        self.secret_key = os.environ.get("AWS_PASS_CLI")
        self.spark = SparkConfig().spark_config()
        
    def pandas_s3_csv(self,path,file,sep):
        s3 = boto3.client("s3", aws_access_key_id=self.access_key, aws_secret_access_key=self.secret_key)
        file_obj = s3.get_object(Bucket=path, Key=file)["Body"]
        # Ler o arquivo CSV usando o pandas
        df = pd.read_csv(file_obj,sep=sep)
        return df
    
    def spark_s3_csv(self,bucket_name,file_path):
        df = self.spark \
                .read \
                .format('csv') \
                .option('header','true') \
                .option('inferschema','true') \
                .load(f"s3a://{bucket_name}/{file_path}")
