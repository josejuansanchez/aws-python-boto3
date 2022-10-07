import boto3
import json
import datetime

def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")


ec2 = boto3.client('ec2')
response = ec2.describe_instances()
#print(response)
json_formatted_str = json.dumps(response, default=datetime_handler)
print(json_formatted_str)

#for instance in ec2.describe_instances():
#    print(instance)

#for bucket in s3.buckets.all():
#        print(bucket.name)