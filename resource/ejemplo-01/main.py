import aws

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
            name = input('Security group name: ')
            description = input('Security group description: ')
            aws.create_security_group(name, description, ingress_permissions)
        elif option == 2:
            name = input('Security group name: ')
            aws.delete_security_group(name)
        elif option == 3:
            aws.list_security_groups()
        elif option == 4:
            min_count = int(input('Min count: '))
            security_group = input('Security group: ')
            aws.create_instance(ami, min_count, instance_type, key_name, security_group)
        elif option == 5:
            name = input('Instance name: ')
            aws.start_instance(name)
        elif option == 6:
            name = input('Instance name: ')
            aws.stop_instance(name)
        elif option == 7:
            name = input('Instance name: ')
            aws.terminate_instance(name)
        elif option == 8:
            aws.list_instances()
        elif option == 9:
            aws.start_instances()
        elif option == 10:
            aws.stop_instances()
        elif option == 11:
            aws.terminate_instances()
        elif option == 12:
            print('Bye!')
        else:
            print('Invalid option')

if __name__ == "__main__":
    main()