import boto3
from botocore.exceptions import NoCredentialsError
import os

class S3AWSClient:
    def __init__(self, region_name, endpoint_url, aws_access_key_id, aws_secret_access_key):
        self.s3_client = boto3.client(
            's3',
            region_name=region_name,
            endpoint_url=endpoint_url,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )

    def upload_file(self, file_path, bucket_name, s3_key):
        try:
            self.s3_client.upload_file(file_path, bucket_name, s3_key)
            print(f"Uploaded file: {file_path} to S3 bucket: {bucket_name} with key: {s3_key}")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except NoCredentialsError:
            print("AWS credentials not found or invalid")

    def upload_folder(self, folder_path, bucket_name):
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                local_file_path = os.path.join(root, file)
                s3_key = os.path.relpath(local_file_path, folder_path)
                self.upload_file(local_file_path, bucket_name, s3_key)

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
