import os
from functions.logger import etl_logger
import pandas as pd
import sqlalchemy
from sqlalchemy import exc
import logging

# Using sqlalchemy to download from a db
# Name will be used for DataBase
# Script_sql is sql script from other SQL file
# engine is the engine from Sql_Alchemy

class etl_downloader:
    def __init__(self,name:str,sql:str,engine:str,logger):
        self.name=name
        self.sql=sql
        self.engine=engine
        self.logger = logger

    def download(self):
        os.makedirs('raw_files/',exist_ok=True)
        print(self.sql)
        try:
            query = open(f"sql_scripts/{self.sql}", "r").read() #This is using  
        
            df = pd.read_sql(query, self.engine)
            df.to_csv(f"raw_files/{self.name}.csv", index=False)

            self.logger.info(f"Extraction complete of {self.sql}")
            return df
        except exc.SQLAlchemyError as e:
            self.logger.debug(f"Error de SQLAlchemy: {str(e)}")

    #def cleaner(self):


