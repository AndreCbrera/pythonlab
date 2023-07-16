import boto3
from botocore.exceptions import NoCredentialsError
import os

# Configure the S3 client to use LocalStack
s3_client = boto3.client(
    's3',
    region_name='us-east-1',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
)

bucket_name = 'my-test-bucket'
folder_path = '/home/dacq/code/pythonlab/OOP/localstack/aws/tests3upload'

def upload_file_to_s3(file_path, bucket, s3_key):
    try:
        s3_client.upload_file(file_path, bucket, s3_key)
        print(f"Uploaded file: {file_path} to S3 bucket: {bucket} with key: {s3_key}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except NoCredentialsError:
        print("AWS credentials not found or invalid")

# Walk through the folder structure and upload files to S3
for root, dirs, files in os.walk(folder_path):
    for file in files:
        local_file_path = os.path.join(root, file)
        s3_key = os.path.relpath(local_file_path, folder_path)
        upload_file_to_s3(local_file_path, bucket_name, s3_key)
