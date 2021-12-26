#Creates New User based on user input. Adds tag to user. Attaches S3 Full access policy based on response!
import boto3
iam = boto3.client('iam')
attach_policy = boto3.resource('iam')
Arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess" #Arn of policy you want to attach to user

user = input("Please enter your Name: ")
response = iam.create_user(
    UserName=user,
Tags=[ # adding tags to identify that user in IAM
        {
            'Key': 'Env',
            'Value': 'Test'
        }
    ]
)
rsp = input("Do you require S3 Full Access?(y/n): ")
if rsp == "y":
    output = iam.attach_user_policy(UserName=user, PolicyArn=Arn)
    print("\n", response)
    print("\n", output)
    print("\n""User now has full access to Amazon S3")
elif rsp == "n":
    print("\n", response) 
    print("\n""No permissions were granted for Amazon S3")