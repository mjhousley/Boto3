import pathlib
import boto3

BASE_DIR = pathlib.Path(__file__).parent.resolve()

AWS_REGION = input("Enter the name of your region:  ")
S3_BUCKET_NAME = input("Enter the name of your bucket:  ")

s3_client = boto3.client("s3", region_name=AWS_REGION)

def upload_files(file_name, bucket, object_name=None, args=None):
    if object_name is None:
        object_name = file_name
    s3_client.upload_file(file_name, bucket, object_name, ExtraArgs=args)
    print(f"'{file_name}' has been uploaded to '{S3_BUCKET_NAME}'")
file = input("Enter name of file you want to upload:  ")
upload_files(file, S3_BUCKET_NAME)
