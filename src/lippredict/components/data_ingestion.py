import os
import zipfile
import gdown
from lippredict import logger
from lippredict.utils.common import get_size
from lippredict.entity.config_entity import DataIngestionConfig


# The `DataIngestion` class is responsible for downloading and extracting a zip file from a given URL.
class DataIngestion:
    """
    Class responsible for data ingestion operations.

    Attributes:
    - config (DataIngestionConfig): Configuration object containing data ingestion settings.
    """

    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self) -> str:
        """
        Downloads a file from a specified URL.

        Returns:
        - None

        Downloads the file from the URL specified in the configuration object.
        """
        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(
                f"Starting download data from {dataset_url} into file {zip_download_dir}."
            )

            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix + file_id, zip_download_dir)

            logger.info(
                f"Data download completed from {dataset_url} into file {zip_download_dir}."
            )

        except Exception as e:
            raise e

    def extract_zip_file(self):
        """
        Extracts a zip file to a specified directory.

        Returns:
        - None

        Extracts the contents of the zip file to the directory specified in the configuration object.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)
