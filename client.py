import boto3

# resource vs client
#
# resource: Devuelve una estructura de datos (high-level interface)
# client: Devuelve un JSON (low-level interface)
#
# Referencia:
# - https://www.learnaws.org/2021/02/24/boto3-resource-client/


def list_instances():
  client = boto3.client('ec2')
  response = client.describe_instances()
  #print(response)

  for r in response['Reservations']:
    #print(f"{r['Instances'][0]}")
    print(f"{r['Instances'][0]['InstanceId']}")
    print(f"{r['Instances'][0]['InstanceType']}")
    print(f"{r['Instances'][0]['KeyName']}")
    print(f"{r['Instances'][0]['PrivateIpAddress']}")
    print(f"{r['Instances'][0]['PublicIpAddress']}")
    print(f"{r['Instances'][0]['State']}")
    print(f"{r['Instances'][0]['Tags']}")
    print()

def list_amis(name, architecture, owner_alias):
  client = boto3.client('ec2')

  filters = [
    {'Name': 'name', 'Values': [ name ]},
    {'Name': 'architecture', 'Values': [ architecture ]},
    {'Name': 'owner-alias', 'Values': [ owner_alias ]}]

  response = client.describe_images(Filters=filters)

  for ami in response['Images']:
    try:
      #print(ami)
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
    #list_instances()
    list_amis(name="*ubuntu*22.04*", architecture="x86_64", owner_alias="amazon")
    list_amis(name="*debian*", architecture="x86_64", owner_alias="amazon")