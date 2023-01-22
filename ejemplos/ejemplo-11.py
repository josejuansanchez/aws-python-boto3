from common.aws_resource_class import AWS

# Read instance name
instance_name = input('Instance name: ')

# Create an object of the AWS class
aws = AWS()

# Terminate instance
aws.terminate_instance(instance_name)

# List instances
aws.list_instances()