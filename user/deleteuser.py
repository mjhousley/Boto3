import boto3
iam = boto3.resource('iam')
"""
    Before deleting user we need to remove
    policies attached to that user
    Otherwise we will get following error
    An error occurred (DeleteConflict) when calling the DeleteUser operation:
    Cannot delete entity, must detach all policies first.
"""
#policy arn which we want to detach from user
# Useraccount = input("Enter name of user you want to delete:  ")
#arn = input("Enter ARN of policy you want to detach from user:  ") 
#policy = iam.Policy(arn)
#response = policy.detach_user(

#Now we can delete user
Useraccount = input("Enter name of user you want to delete:  ")
UserName=Useraccount
user = iam.User(Useraccount)
user.delete()