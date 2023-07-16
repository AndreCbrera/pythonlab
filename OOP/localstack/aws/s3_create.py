import boto3

# Configure the S3 client to use LocalStack
s3_client = boto3.client(
    's3',
    region_name='us-east-1',
    endpoint_url='http://localhost:4566',  # Replace with the LocalStack endpoint
    aws_access_key_id='test',              # Replace with your LocalStack AWS access key
    aws_secret_access_key='test',          # Replace with your LocalStack AWS secret key
)

# Create an S3 bucket
bucket_name = 'my-test-bucket'  # Replace with your desired bucket name
s3_client.create_bucket(Bucket=bucket_name)

# Verify the bucket was created
response = s3_client.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]
if bucket_name in buckets:
    print(f"Bucket '{bucket_name}' created successfully.")
else:
    print(f"Failed to create bucket '{bucket_name}'.")
