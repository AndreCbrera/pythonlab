import os
import boto3
from botocore.exceptions import NoCredentialsError

class S3AWSClient:
    """
    A class for interacting with AWS S3 using Boto3.
    """

    def __init__(self, region_name, endpoint_url, aws_access_key_id, aws_secret_access_key):
        """
        Initialize the S3AWSClient object with the provided credentials and configurations.
        """
        self.s3_client = boto3.client(
            's3',
            region_name=region_name,
            endpoint_url=endpoint_url,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )

    def upload_file(self, file_path, bucket_name, s3_key):
        """
        Upload a file to the specified S3 bucket with the given key.
        """
        try:
            self.s3_client.upload_file(file_path, bucket_name, s3_key)
            print(f"Uploaded file: {file_path} to S3 bucket: {bucket_name} with key: {s3_key}")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except NoCredentialsError:
            print("AWS credentials not found or invalid")

    def upload_folder(self, folder_path, bucket_name):
        """
        Upload all files in a local folder to the specified S3 bucket.
        """
        for root, _, files in os.walk(folder_path):
            for file in files:
                local_file_path = os.path.join(root, file)
                s3_key = os.path.relpath(local_file_path, folder_path)
                self.upload_file(local_file_path, bucket_name, s3_key)

def main():
    """
    Entry point of the script.
    """
    # Configure the S3 client to use LocalStack
    s3_client = S3AWSClient(
        region_name='us-east-1',
        endpoint_url='http://localhost:4566',
        aws_access_key_id='test',
        aws_secret_access_key='test',
    )

    bucket_name = 'my-test-bucket'
    folder_path = '/home/dacq/code/pythonlab/OOP/localstack/aws/tests3upload'

    s3_client.upload_folder(folder_path, bucket_name)

if __name__ == '__main__':
    main()
