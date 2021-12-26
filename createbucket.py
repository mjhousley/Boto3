import boto3
import pprint
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
print(pprint.pprint(rsp1))