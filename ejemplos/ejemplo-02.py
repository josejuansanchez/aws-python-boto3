from common import aws_resource_functions as aws

# Read security group name and sescription
sg_name = input('Security group name: ')

# Delete security group
aws.delete_security_group(sg_name)

# List security groups
aws.list_security_groups()