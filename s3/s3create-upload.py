import boto3
import pathlib
client = boto3.client('s3')

bucket_name=str(input('Please input bucket name to be created: '))
rsp1 = client.create_bucket(
 ACL='private',
 Bucket=bucket_name
 )

tag_resp=str(input('Press "y" if you want to tag your bucket?: '))
if tag_resp == 'y':
    tag_key=str(input("Please enter key for the tag: "))
    tag_value = str(input("Please enter value for the tag: "))
response2 = client.put_bucket_tagging(
Bucket=bucket_name,
Tagging={
    'TagSet': [
        {
            'Key': tag_key,
            'Value': tag_value
        }
    ]
})

BASE_DIR = pathlib.Path(__file__).parent.resolve()

AWS_REGION = input("Enter the name of your region:  ")

s3_client = boto3.client("s3", region_name=AWS_REGION)

def upload_files(file_name, bucket, object_name=None, args=None):
    if object_name is None:
        object_name = file_name
    s3_client.upload_file(file_name, bucket, object_name, ExtraArgs=args)
    print(f"'{file_name}' has been uploaded to '{bucket_name}'")
file = input("Enter name of file you want to upload:  ")
upload_files(file, bucket_name)