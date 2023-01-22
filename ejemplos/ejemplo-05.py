from common import aws_resource_functions as aws

# Get instance ID from instance name
instance_name = input('Instance name: ')
instance_id = aws.get_instance_id(instance_name)

if instance_id == None:
    print('There is no instance with that name')
    exit()

# Allocate and associate Elastic IP
elastic_ip = aws.allocate_elastic_ip()
aws.associate_elastic_ip(elastic_ip, instance_id)