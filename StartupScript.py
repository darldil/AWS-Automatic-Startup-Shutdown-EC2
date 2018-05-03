import boto3

def lambda_handler(event, context):

    if not bool(event):
        raise Exception('No se ha definido ningún evento.')
        
    instances = event.get("instances")
    region = event.get("region")
        
    if not bool(instances):
        raise Exception('Error: No se han proporcionado instancias')
        
    if not type(instances) is list:
        raise Exception('Error: Las instancias no están en la lista')
        
    if not bool(instances):
        raise Exception('Error: No se han proporcionado instancias')

    if not bool(region):
        raise Exception('Error: No se ha proporcionado una region')

    ec2 = boto3.client('ec2', region_name=region)
    ec2.start_instances(InstanceIds=instances)
        
    for instance in instances:
         print "Iniciada instancia {} en la region {}".format(instance, region)
