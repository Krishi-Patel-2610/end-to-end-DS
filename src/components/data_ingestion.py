import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass # this is called a decorator and it is used to directly define varibales inside a class without using __init__ method
class DataInfestionConfig:
    train_data_path = os.path.join('artifacts', 'train.csv')
    test_data_path = os.path.join('artifacts', 'test.csv')
    raw_data_path = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingesiton_config = DataInfestionConfig()
    def initate_data_ingestion(self):
        logging.info("Entered the data ingestion block")
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataFrame')

            os.makedirs(os.path.dirname(self.ingesiton_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingesiton_config.raw_data_path, index=False, header=True)
            logging.info("Train test split initated")

            trian_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            trian_set.to_csv(self.ingesiton_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingesiton_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of data is completed")

            return(
                self.ingesiton_config.train_data_path,
                self.ingesiton_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initate_data_ingestion()