import boto3
import botocore

class ec2:
  def __init__(self):
    self.ec2 = boto3.resource('ec2')

  """
  List all security groups
  """
  def list_security_groups(self):
    for sg in self.ec2.security_groups.all():
      print(f"group_id: {sg.group_id} \t group_name: {sg.group_name} \t description: {sg.description}")
      for rule in sg.ip_permissions:
        print(rule)
      print()

  """
  List EC2 instances
  """
  def list_instances(self):
    print("Instance \t\t State \t\t Name \t\t Private IP \t Public IP")
    for i in self.ec2.instances.all():
      print(f"{i.id} \t {i.state['Name']} \t {i.tags[0]['Value']} \t {i.private_ip_address} \t {i.public_ip_address}")

  """
  Start all EC2 instances
  """
  def start_instances(self):
    for i in self.ec2.instances.all():
      if i.state['Name'] == 'stopped':
        i.start()
        print(f"Starting instance: {i.id} \t Name: {i.tags[0]['Value']}")
  """
  Stop all EC2 instances
  """
  def stop_instances(self):
    for i in self.ec2.instances.all():
      if i.state['Name'] == 'running':
        i.stop()
        print(f"Stopping instance: {i.id} \t Name: {i.tags[0]['Value']}")

  """
  Start an EC2 instance
  """
  def start_instance(self, instance_id):
    try:
      for i in self.ec2.instances.all():
        if i.id == instance_id:
          i.start()
          print(f"Starting instance: {i.id} \t Name: {i.tags[0]['Value']}")
    except botocore.exceptions.ClientError as error:
      print(f"ERROR: {error.response['Error']['Code']}. {error.response['Error']['Message']}")
      #raise error

  """
  Stop an EC2 instance
  """
  def stop_instance(self, instance_id):
    try:
      for i in self.ec2.instances.all():
        if i.id == instance_id:
          i.stop()
          print(f"Stopping instance: {i.id} \t Name: {i.tags[0]['Value']}")
    except botocore.exceptions.ClientError as error:
      print(f"ERROR: {error.response['Error']['Code']}. {error.response['Error']['Message']}")
      #raise error

  """
  Terminate an EC2 instance
  """
  def terminate_instance(self, instance_id):
    for i in self.ec2.instances.all():
      if i.id == instance_id:
        i.terminate()
        print(f"Terminating instance: {i.id} \t Name: {i.tags[0]['Value']}")

  """
  Create a new EC2 instance
  """
  def create_instance(self, image_id, max_count, instance_type, key_name, instance_name):
    instance = self.ec2.create_instances(
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
    ec2 = ec2()
    ec2.list_security_groups()

    ec2.list_instances()
    #ec2.stop_instances()
    #ec2.start_instances()

    ec2.create_instance("ami-08c40ec9ead489470", 1, "t2.micro", "vockey", "boto3-test-a")

    ec2.stop_instance("i-09046bf56dc0c4e05")
    ec2.stop_instance("i-0e8ec3490c4203c26")
    ec2.stop_instance("i-0f1d960adbdeded31")
    ec2.stop_instance("i-07ddba56ac71a5ba4")
    ec2.stop_instance("i-0fffdd7ad1be1c1c5")

    ec2.terminate_instance("i-09046bf56dc0c4e05")
    ec2.terminate_instance("i-0e8ec3490c4203c26")
    ec2.terminate_instance("i-0f1d960adbdeded31")
    ec2.terminate_instance("i-07ddba56ac71a5ba4")
    ec2.terminate_instance("i-0fffdd7ad1be1c1c5")