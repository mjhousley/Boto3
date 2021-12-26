import boto3
iam = boto3.resource('iam')
detach_policy = boto3.resource('iam')
"""
    Before deleting user we need to remove
    policies attached to that user
    Otherwise we will get following error
    An error occurred (DeleteConflict) when calling the DeleteUser operation:
    Cannot delete entity, must detach all policies first.
"""
#policy arn which we want to detach from user
Useraccount = input("Enter name of user:  ")
policy = iam.Policy('arn:aws:iam::aws:policy/AmazonS3FullAccess')
response = policy.detach_user(
UserName=Useraccount
)
group = iam.Group('Tester')
response = group.remove_user(
    UserName=Useraccount
)
#Now we can delete user
user = iam.User(Useraccount)
user.delete()