#!/usr/bin/python3
# -*- coding: utf-8 -*-

#apenas para estudo
import sys
import pandas as pd
sys.path.append('/home/thiago-vale/Documentos/GitHub/pipeline-de-dados-cloud/utils')
from utils.base_etl import Base
from utils.read import Read
from utils.write import Write

__bucket__ = '01-raw-lake'

class ETL(Base):

    def __init__(self):
        super().__init__()
        self.read = Read()
        self.write = Write()
        #self.__bucket__ = '01-raw-lake'

    def extract(self):
        df = pd.read_csv('/home/thiago-vale/Documentos/GitHub/teste.csv',sep=',')
        return df

    def transform(self,df):
        return df

    def load(self,df):
        self.write.s3_pandas_csv(__bucket__,"teste.csv",df)
