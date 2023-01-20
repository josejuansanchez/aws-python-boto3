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
    print('-- Elastic IP --')
    print(' 12. Allocate and associate Elastic IP')
    print(' 13. Release Elastic IP')
    print(' 14. Exit')

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
    while option != 14:
        show_menu()
        option = int(input('\nSelect an option (1-14): '))

        if option == 1:
            sg_name = input('Security group name: ')
            sg_description = input('Security group description: ')
            aws.create_security_group(sg_name, sg_description, ingress_permissions)
        elif option == 2:
            sg_name = input('Security group name: ')
            aws.delete_security_group(sg_name)
        elif option == 3:
            aws.list_security_groups()
        elif option == 4:
            # Read the input parameters
            instance_name = input('Instance name: ')
            min_count = int(input('Min count: '))
            sg_name = input('Security group: ')

            # Check if security group exists
            if aws.security_group_exists(sg_name) == False:
                print('The security group does not exist')
                continue
            
            # Create the instance
            aws.create_instance(ami, min_count, instance_type, key_name, instance_name, sg_name)
        elif option == 5:
            instance_name = input('Instance name: ')
            aws.start_instance(instance_name)
        elif option == 6:
            instance_name = input('Instance name: ')
            aws.stop_instance(instance_name)
        elif option == 7:
            instance_name = input('Instance name: ')
            aws.terminate_instance(instance_name)
        elif option == 8:
            aws.list_instances()
        elif option == 9:
            aws.start_instances()
        elif option == 10:
            aws.stop_instances()
        elif option == 11:
            aws.terminate_instances()
        elif option == 12:
            # Get instance ID from instance name
            instance_name = input('Instance name: ')
            instance_id = aws.get_instance_id(instance_name)

            if instance_id == None:
                print('There is no instance with that name')
                continue

            # Allocate and associate Elastic IP
            elastic_ip = aws.allocate_elastic_ip()
            aws.associate_elastic_ip(elastic_ip, instance_id)
        elif option == 13:
            # Get instance ID from instance name
            instance_name = input('Instance name: ')
            instance_id = aws.get_instance_id(instance_name)

            if instance_id == None:
                print('There is no instance with that name')
                continue

            # Get Elastic IP from instance ID
            elastic_ip = aws.get_instance_public_ip(instance_id)

            # Release Elastic IP
            aws.release_elastic_ip(elastic_ip)
        elif option == 14:
            print('Bye!')
        else:
            print('Invalid option')
        
        input('\nPress any key to continue...')

if __name__ == "__main__":
    main()