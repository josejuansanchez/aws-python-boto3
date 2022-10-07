import boto3
import botocore

ec2 = boto3.resource('ec2')

# Reference: 
# - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#securitygroup
#
def list_security_groups():
  for sg in ec2.security_groups.all():
    print(f"group_id: {sg.group_id} \t group_name: {sg.group_name} \t description: {sg.description}")
    for rule in sg.ip_permissions:
      print(rule)
    print()

# Reference:
# - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#instance
def list_ec2_instances():
  print("Instance \t\t State \t\t Name \t\t Private IP \t Public IP")
  for i in ec2.instances.all():
    print(f"{i.id} \t {i.state['Name']} \t {i.tags[0]['Value']} \t {i.private_ip_address} \t {i.public_ip_address}")

def start_ec2_instances():
  for i in ec2.instances.all():
    if i.state['Name'] == 'stopped':
      i.start()
      print(f"Starting instance: {i.id} \t Name: {i.tags[0]['Value']}")

def stop_ec2_instances():
  for i in ec2.instances.all():
    if i.state['Name'] == 'running':
      i.stop()
      print(f"Stopping instance: {i.id} \t Name: {i.tags[0]['Value']}")

def start_ec2_instance(instance_id):
  try:
    for i in ec2.instances.all():
      if i.id == instance_id:
        i.start()
        print(f"Starting instance: {i.id} \t Name: {i.tags[0]['Value']}")
  except botocore.exceptions.ClientError as error:
    print(f"ERROR: {error.response['Error']['Code']}. {error.response['Error']['Message']}")
    #raise error

def stop_ec2_instance(instance_id):
  try:
    for i in ec2.instances.all():
      if i.id == instance_id:
        i.stop()
        print(f"Stopping instance: {i.id} \t Name: {i.tags[0]['Value']}")
  except botocore.exceptions.ClientError as error:
    print(f"ERROR: {error.response['Error']['Code']}. {error.response['Error']['Message']}")
    #raise error

def terminate_ec2_instance(instance_id):
  for i in ec2.instances.all():
    if i.id == instance_id:
      i.terminate()
      print(f"Terminating instance: {i.id} \t Name: {i.tags[0]['Value']}")

def create_ec2_instance(image_id, max_count, instance_type, key_name, instance_name):
  instance = ec2.create_instances(
    ImageId = image_id,
    MinCount = 1,
    MaxCount = max_count,
    InstanceType = instance_type,
    KeyName = key_name,
    TagSpecifications=[{
      'ResourceType': 'instance',
      'Tags': [{
        'Key': 'Name',
        'Value': instance_name
      }]
    }])

  print(instance)

if __name__ == "__main__":
    #list_security_groups()
    list_ec2_instances()
    #stop_ec2_instances()
    #start_ec2_instances()
    #create_ec2_instance("ami-08c40ec9ead489470", 1, "t2.micro", "vockey", "boto3-test-a")
    #client_list_instances()
    stop_ec2_instance("i-09046bf56dc0c4e05")
    stop_ec2_instance("i-0e8ec3490c4203c26")
    stop_ec2_instance("i-0f1d960adbdeded31")
    stop_ec2_instance("i-07ddba56ac71a5ba4")
    stop_ec2_instance("i-0fffdd7ad1be1c1c5")
    terminate_ec2_instance("i-09046bf56dc0c4e05")
    terminate_ec2_instance("i-0e8ec3490c4203c26")
    terminate_ec2_instance("i-0f1d960adbdeded31")
    terminate_ec2_instance("i-07ddba56ac71a5ba4")
    terminate_ec2_instance("i-0fffdd7ad1be1c1c5")