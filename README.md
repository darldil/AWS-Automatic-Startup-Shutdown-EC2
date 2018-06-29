# AWS-Automatic-Startup-Shutdown-EC2
Automatic Scripts to start and shutdown EC2 machines on Amazon Web Services

To work automatically it is necessary to configure a rule in CloudWatch with a target calling lambda functions and containing the following data as input:

Constant: { "region": "the region of the ec2 instance", "instances": [ "The id of the ec2 instances" ] }	
