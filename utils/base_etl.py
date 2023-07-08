#!/usr/bin/python3
# -*- coding: utf-8 -*-

from abc import abstractmethod, ABC
from pyspark.sql import DataFrame
from typing import Dict

class Base(ABC):
    
    def __init__(self):
        self.spark = spark_configs()

    @abstractmethod
    def extract(self) -> Dict[str, DataFrame]:
        raise NotImplementedError["Method extract Not Implemented"]

    
    @abstractmethod
    def transform(self, data_sources: Dict[str, DataFrame]) -> DataFrame:
        raise NotImplementedError["Method transform Not Implemented"]
    
    @abstractmethod
    def load(self, df:DataFrame) -> None:
        raise NotImplementedError["Method load Not Implemented"]