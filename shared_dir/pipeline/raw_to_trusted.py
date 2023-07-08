#!/usr/bin/python3
# -*- coding: utf-8 -*-

#apenas para estudo
import sys
sys.path.append('/home/thiago-vale/Documentos/GitHub/pipeline-de-dados-cloud/utils')
from utils.base_etl import Base
from utils.read import Read
from utils.write import Write



class ETL(Base):

    def __init__(self):
        super().__init__()
        self.read = Read()
        self.write = Write()
        self.bucket_read = "01-raw-lake"
        self.bucket_load = "02-trusted-lake"

    def extract(self):
        df = self.read.pandas_s3_csv(self.bucket_read,"teste.csv",sep=',')
        return df

    def transform(self,df):
        return df

    def load(self,df):
        self.write.s3_pandas_csv(self.bucket_load,"teste.csv",df)
