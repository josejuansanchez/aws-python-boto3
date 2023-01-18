import boto3
import botocore

class AWS:
  def __init__(self):
    self.ec2 = boto3.resource('ec2')

  """
  List all VPCs
  """
  def list_vpcs(self):
    for vpc in self.ec2.vpcs.all():
      print(vpc)
      print(f"id: {vpc.id}")
      print(f"cidr_block: {vpc.cidr_block}")
      print(f"cidr_block_association_set: {vpc.cidr_block_association_set}")
      print(f"dhcp_options_id: {vpc.dhcp_options_id}")
      print(f"instance_tenancy: {vpc.instance_tenancy}")
      print(f"ipv6_cidr_block_association_set: {vpc.ipv6_cidr_block_association_set}")
      print(f"is_default: {vpc.is_default}")
      print(f"owner_id: {vpc.owner_id}")
      print(f"state: {vpc.state}")
      print(f"tags: {vpc.tags}")
      print(f"vpc_id: {vpc.vpc_id}")
  
  """
  Returns default VPC id
  """
  def get_default_vpc_id(self):
    for vpc in self.ec2.vpcs.all():
      if vpc.is_default == True:
        return vpc.id

  """
  Create a security group
  """
  def create_security_group(self, group_name, description, ingress_permissions):
    try:
      sg = self.ec2.create_security_group(GroupName=group_name, Description=description)
      for p in ingress_permissions:
        sg.authorize_ingress(CidrIp=p['CidrIp'], IpProtocol=p['IpProtocol'], FromPort=p['FromPort'], ToPort=p['ToPort'])
      print(f"Security group {group_name} created")
    except botocore.exceptions.ClientError as error:
      print(error)

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
  Delete a security group
  """
  def delete_security_group(self, group_name):
    # Get the security group id from name
    group_id = self.get_security_group_id(group_name)

    # Check if security group exists
    if group_id is None:
      print('The security group does not exist')
      return

    # Delete the security group
    try:
      sg = self.ec2.SecurityGroup(group_id)
      sg.delete()
      print(f'The security group {group_name} has been deleted')
    except botocore.exceptions.ClientError as error:
      print(error)

  """
  Returns security group id
  """
  def get_security_group_id(self, group_name):
    for sg in self.ec2.security_groups.all():
      if sg.group_name == group_name:
        return sg.group_id

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
  Terminate all EC2 instances
  """
  def terminate_instances(self):
    for i in self.ec2.instances.all():
      if i.state['Name'] == 'running':
        i.terminate()
        print(f"Terminating instance: {i.id} \t Name: {i.tags[0]['Value']}")

  """
  Start an EC2 instance by id
  """
  def start_instance_by_id(self, instance_id):
    try:
      for i in self.ec2.instances.all():
        if i.id == instance_id:
          i.start()
          print(f"Starting instance: {i.id} \t Name: {i.tags[0]['Value']}")
    except botocore.exceptions.ClientError as error:
      print(f"ERROR: {error.response['Error']['Code']}. {error.response['Error']['Message']}")
      #raise error

  """
  Stop an EC2 instance by id
  """
  def stop_instance_by_id(self, instance_id):
    try:
      for i in self.ec2.instances.all():
        if i.id == instance_id:
          i.stop()
          print(f"Stopping instance: {i.id} \t Name: {i.tags[0]['Value']}")
    except botocore.exceptions.ClientError as error:
      print(f"ERROR: {error.response['Error']['Code']}. {error.response['Error']['Message']}")
      #raise error

  """
  Terminate an EC2 instance by id
  """
  def terminate_instance_by_id(self, instance_id):
    for i in self.ec2.instances.all():
      if i.id == instance_id:
        i.terminate()
        print(f"Terminating instance: {i.id} \t Name: {i.tags[0]['Value']}")

  """
  Start an EC2 instance by name
  """
  def start_instance(self, instance_name):
    # Get the instance using the filter method
    instances = self.ec2.instances.filter(Filters=[{'Name':'tag:Name', 'Values':[instance_name]}])

    # Store the instances in a list
    instances_list = [i for i in instances]

    if instances_list:
        # Start the instances
        for instance in instances_list:
            instance.start()
            print(f'Instance {instance.id} was started')
    else:
        print(f'The instance {instance_name} does not exist')

  """
  Stop an EC2 instance by name
  """
  def stop_instance(self, instance_name):
    # Get the instance using the filter method
    instances = self.ec2.instances.filter(Filters=[{'Name':'tag:Name', 'Values':[instance_name]}])

    # Store the instances in a list
    instances_list = [i for i in instances]

    if instances_list:
        # Stop the instances
        for instance in instances_list:
            instance.stop()
            print(f'Instance {instance.id} was stopped')
    else:
        print(f'The instance {instance_name} does not exist')

  """
  Terminate an EC2 instance by name
  """
  def terminate_instance(self, instance_name):
    # Get the instance using the filter method
    instances = self.ec2.instances.filter(Filters=[{'Name':'tag:Name', 'Values':[instance_name]}])

    # Store the instances in a list
    instances_list = [i for i in instances]

    if instances_list:
        # Terminate the instances
        for instance in instances_list:
            instance.terminate()
            print(f'Instance {instance.id} was terminated')
    else:
        print(f'The instance {instance_name} does not exist')

  """
  Create a new EC2 instance
  """
  def create_instance(self, image_id, max_count, instance_type, key_name, instance_name, security_group_name):
    instance = self.ec2.create_instances(
      ImageId = image_id,
      MinCount = 1,
      MaxCount = max_count,
      InstanceType = instance_type,
      SecurityGroups = [ security_group_name ],
      KeyName = key_name,
      TagSpecifications=[{
        'ResourceType': 'instance',
        'Tags': [{
          'Key': 'Name',
          'Value': instance_name
        }]
      }])

    #print(instance)
    print(f'The instance {instance[0].id} has been created')

  """
  Returns instance id
  """
  def get_instance_id(self, instance_name):
    for i in self.ec2.instances.all():
      if i.tags[0]['Value'] == instance_name:
        return i.id

  """
  Allocate an elastic IP
  """
  def allocate_elastic_ip(self):
    response = self.ec2.meta.client.allocate_address()
    print(f"The elastic IP {response['PublicIp']} has been allocated")
    return response['PublicIp']

  """
  Get the allocation id of an elastic IP
  """
  def get_allocation_id(self, public_ip):
    addresses = self.ec2.meta.client.describe_addresses(PublicIps=[public_ip])
    if addresses['Addresses']:
        return addresses['Addresses'][0]['AllocationId']
    else:
        return None

  """
  Associate an elastic IP to an instance
  """
  def associate_elastic_ip(self, public_ip, instance_id):
    print('Waiting until the instance is running...')
    self.ec2.Instance(instance_id).wait_until_running()

    allocation_id = self.get_allocation_id(public_ip)
    self.ec2.meta.client.associate_address(AllocationId=allocation_id, InstanceId=instance_id)
    print(f"The elastic IP {public_ip} has been associated to the instance {instance_id}")