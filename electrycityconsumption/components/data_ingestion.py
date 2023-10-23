import os
import shutil
from electrycityconsumption.electricity_consumption_prediction import logger_1  

class DataIngestion:
    def __init__(self, config):

        self.config = config

    def copy_local_data(self):
        """
        Copies the local .csv file to the data directory.
        """
        local_file_path = self.config.local_data_path
        destination_dir = self.config.root_dir
        os.makedirs(destination_dir, exist_ok=True)

        logger_1.info(f"Copying local data file from {local_file_path} to {destination_dir}")
        
        try:
            shutil.copy(local_file_path, destination_dir)
            logger_1.info("Data file copied successfully.")
        except Exception as e:
            logger_1.error(f"Error copying data file: {str(e)}")