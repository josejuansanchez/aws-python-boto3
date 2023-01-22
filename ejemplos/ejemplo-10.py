from common.aws_resource_class import AWS

# AMI ID
ami = 'ami-08c40ec9ead489470'

# Instance type
instance_type = 't2.small'

# SSH key name
key_name = 'vockey'

# Read the input parameters
instance_name = input('Instance name: ')
sg_name = input('Security group: ')

# Create an object of the AWS class
aws = AWS()

# Check if security group exists
if aws.security_group_exists(sg_name) == False:
    print('The security group does not exist')
    exit()

# Create the instance
aws.create_instance(ami, 1, instance_type, key_name, instance_name, sg_name)

# List instances
aws.list_instances()