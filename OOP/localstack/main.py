import os
from s3.s3_aws_client import S3AWSClient
from dynamodb.dynamodb_client import DynamoDBClient

def main():
    s3_client = S3AWSClient(
        region_name='us-east-1',
        endpoint_url='http://localhost:4566',
        aws_access_key_id='test',
        aws_secret_access_key='test',
    )

    bucket_name = 'my-test-bucket'
    folder_path = '/home/dacq/code/pythonlab/OOP/localstack/aws/tests3upload'

    s3_client.upload_folder(folder_path, bucket_name)

    dynamodb_client = DynamoDBClient(
        region_name='us-east-1',
        endpoint_url='http://localhost:4566',
        aws_access_key_id='test',
        aws_secret_access_key='test',
    )

    tables = dynamodb_client.get_tables()
    print("DynamoDB Tables:")
    for table in tables:
        print(table)

if __name__ == '__main__':
    main()
