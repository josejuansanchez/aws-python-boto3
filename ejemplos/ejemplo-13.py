from common.aws_resource_class import AWS

# Create an object of the AWS class
aws = AWS()

# Get instance ID from instance name
instance_name = input('Instance name: ')
instance_id = aws.get_instance_id(instance_name)

if instance_id == None:
    print('There is no instance with that name')
    exit()

# Get Elastic IP from instance ID
elastic_ip = aws.get_instance_public_ip(instance_id)

# Release Elastic IP
aws.release_elastic_ip(elastic_ip)