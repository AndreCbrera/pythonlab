import boto3

# Configure the S3 client to use LocalStack
s3_client = boto3.client(
    's3',
    region_name='us-east-1',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
)

bucket_name = 'my-test-bucket'

def list_files_and_folders(bucket):
    response = s3_client.list_objects_v2(Bucket=bucket)

    for obj in response.get('Contents', []):
        key = obj['Key']
        if key.endswith('/'):
            print(f"Folder: {key}")
        else:
            print(f"File: {key}")

list_files_and_folders(bucket_name)
