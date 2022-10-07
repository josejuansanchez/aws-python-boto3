import boto3

# resource vs client
#
# resorce: Devuelve una estructura de datos (high-level interface)
# client: Devuelve un JSON (low-level interface)
#
# Referencia:
# - https://www.learnaws.org/2021/02/24/boto3-resource-client/

client = boto3.client('ec2')

def client_list_instances():
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


if __name__ == "__main__":
    client_list_instances()