from aws import AWS

def show_menu():
    print('\n-- Security Group --')
    print(' 1. Create security group')
    print(' 2. Delete security group')
    print(' 3. List security groups')
    print('-- EC2 Instance --')
    print(' 4. Create EC2 instance')
    print(' 5. Start EC2 instance')
    print(' 6. Stop EC2 instance')
    print(' 7. Terminate EC2 instance')
    print('-- EC2 Instances --')    
    print(' 8. List all EC2 instances')
    print(' 9. Start all EC2 instances')
    print(' 10. Stop all EC2 instances')
    print(' 11. Terminate all EC2 instances')
    print(' 12. Exit')

def main():
    # Create an object of the AWS class
    aws_object = AWS()
  
    # Security group ingress permissions
    ingress_permissions = [
      {'CidrIp': '0.0.0.0/0', 'IpProtocol': 'tcp', 'FromPort': 22, 'ToPort': 22},    
      {'CidrIp': '0.0.0.0/0', 'IpProtocol': 'tcp', 'FromPort': 80, 'ToPort': 80},    
      {'CidrIp': '0.0.0.0/0', 'IpProtocol': 'tcp', 'FromPort': 443, 'ToPort': 443}]

    # AMI ID
    ami = 'ami-08c40ec9ead489470'

    # Instance type
    instance_type = 't2.small'

    # SSH key name
    key_name = 'vockey'

    option = 0
    while option != 12:
        show_menu()
        option = int(input('\nSelect an option (1-12): '))
        if option == 1:
            sg_name = input('Security group name: ')
            sg_description = input('Security group description: ')
            aws_object.create_security_group(sg_name, sg_description, ingress_permissions)
        elif option == 2:
            sg_name = input('Security group name: ')
            aws_object.delete_security_group(sg_name)
        elif option == 3:
            aws_object.list_security_groups()
        elif option == 4:
            instance_name = input('Instance name: ')
            min_count = int(input('Min count: '))
            sg_name = input('Security group name: ')
            aws_object.create_instance(ami, min_count, instance_type, key_name, instance_name, sg_name)
        elif option == 5:
            instance_name = input('Instance name: ')
            aws_object.start_instance(name)
        elif option == 6:
            instance_name = input('Instance name: ')
            aws_object.stop_instance(instance_name)
        elif option == 7:
            instance_name = input('Instance name: ')
            aws_object.terminate_instance(instance_name)
        elif option == 8:
            aws_object.list_instances()
        elif option == 9:
            aws_object.start_instances()
        elif option == 10:
            aws_object.stop_instances()
        elif option == 11:
            aws_object.terminate_instances()
        elif option == 12:
            print('Bye!')
        else:
            print('Invalid option')

if __name__ == "__main__":
    main()