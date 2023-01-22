from common.aws_resource_class import AWS

# Read security group name and sescription
sg_name = input('Security group name: ')

# Create an object of the AWS class
aws = AWS()

# Delete security group
aws.delete_security_group(sg_name)

# List security groups
aws.list_security_groups()