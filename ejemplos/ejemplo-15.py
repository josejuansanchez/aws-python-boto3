import boto3

"""
List all security groups
"""
def list_security_groups():
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_security_groups()

    for sg in response['SecurityGroups']:
      print(f"group_id: {sg.get('GroupId')} \t group_name: {sg.get('GroupName')} \t description: {sg.get('Description')}")
      for rule in sg.get('IpPermissions'):
        print(rule)
      print()

"""
List EC2 instances
"""
def list_instances():
    client = boto3.client('ec2')
    response = client.describe_instances()

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"InstanceId: {instance['InstanceId']}")
            print(f"InstanceType: {instance['InstanceType']}")
            print(f"KeyName: {instance['KeyName']}")
            print(f"PrivateIpAddress: {instance['PrivateIpAddress']}")
            print(f"PublicIpAddress: {instance['PublicIpAddress']}")
            print(f"State: {instance['State']}")
            print(f"Tags: {instance['Tags']}")
            print()

"""
List AMIs
"""
def list_amis(name, architecture, owner_alias):
  client = boto3.client('ec2')

  filters = [
    {'Name': 'name', 'Values': [ name ]},
    {'Name': 'architecture', 'Values': [ architecture ]},
    {'Name': 'owner-alias', 'Values': [ owner_alias ]}]

  response = client.describe_images(Filters=filters)

  for ami in response['Images']:
    try:
      print(f"ImageId: \t {ami['ImageId']}")
      print(f"Architecture: \t {ami['Architecture']}")
      print(f"Hypervisor: \t {ami['Hypervisor']}")
      print(f"Name: \t\t {ami['Name']}")
      print(f"ImageOwnerAlias: {ami['ImageOwnerAlias']}")
      print(f"PlatformDetails: {ami['PlatformDetails']}")
      print(f"Description: \t {ami['Description']}")
      print(f"CreationDate: \t {ami['CreationDate']}")
      print()
    except KeyError:
      print()
      pass

if __name__ == "__main__":
  list_security_groups()
  list_instances()
  list_amis(name="*ubuntu*22.04*", architecture="x86_64", owner_alias="amazon")
  #list_amis(name="*debian*", architecture="x86_64", owner_alias="amazon")