import boto3

# Configure the S3 client to use LocalStack
s3_client = boto3.client(
    's3',
    region_name='us-east-1',
    endpoint_url='http://localhost:4566',  # Replace with the LocalStack endpoint
    aws_access_key_id='test',              # Replace with your LocalStack AWS access key
    aws_secret_access_key='test',          # Replace with your LocalStack AWS secret key
)

# List all S3 buckets
response = s3_client.list_buckets()

# Print the bucket names
for bucket in response['Buckets']:
    print(bucket['Name'])
