import boto3

ec2 = boto3.resource('ec2')

# Reference: 
# - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#securitygroup
#
def list_security_groups():
  for sg in ec2.security_groups.all():
    print(f"group_id: {sg.group_id} \t group_name: {sg.group_name} \t description: {sg.description}")
    print(sg.ip_permissions)
    print()

# Reference:
# - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#instance
def list_ec2_instances():
  for i in ec2.instances.all():
    print(f"Instance: {i.id} \t State: {i.state['Name']} \t Name: {i.tags[0]['Value']}")

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

def create_ec2_instance(image_id, min_count, max_count, instance_type, key_name, instance_name):
  instance = ec2.create_instances(
    ImageId = image_id,
    MinCount = min_count,
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

if __name__ == "__main__":
    #list_security_groups()
    #list_ec2_instances()
    #stop_ec2_instances()
    start_ec2_instances()
    #create_ec2_instance("ami-08c40ec9ead489470", 1, 1, "t2.micro", "vockey", "boto3-test")