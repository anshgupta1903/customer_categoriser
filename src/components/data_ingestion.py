import os
import pandas as pd
from src.utils.logger import logger
from src.utils.exception import CustomException

class DataIngestion:
    """
    Component to ingest data from CSV or other sources.
    """

    def __init__(self, data_path=None):
        """
        Initialize with optional custom data path.
        """
        # default path if none provided
        if data_path:
            self.data_path = data_path
        else:
            # adjust the path according to your project structure
            self.data_path = os.path.join("notebooks", "data", "clustered_data.csv")

    def ingest_data(self):
        """
        Reads data from CSV and returns DataFrame.
        """
        try:
            logger.info(f"Starting data ingestion from: {self.data_path}")
            df = pd.read_csv(self.data_path)
            logger.info(f"Data ingestion completed. Shape: {df.shape}")
            return df

        except FileNotFoundError as e:
            logger.error(f"File not found at path: {self.data_path}")
            raise CustomException(f"File not found: {self.data_path}", e)

        except pd.errors.ParserError as e:
            logger.error(f"Parsing CSV failed at: {self.data_path}")
            raise CustomException("Parsing CSV failed", e)

        except Exception as e:
            logger.error(f"Unexpected error during data ingestion: {str(e)}")
            raise CustomException("Unexpected error during data ingestion", e)
