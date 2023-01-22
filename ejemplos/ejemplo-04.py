from common import aws_resource_functions as aws

# Read instance name
instance_name = input('Instance name: ')

# Terminate instance
aws.terminate_instance(instance_name)

# List instances
aws.list_instances()