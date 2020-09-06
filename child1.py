import boto3
import time
import os
from troposphere import Base64, FindInMap, GetAtt, Join, Output
from troposphere import Parameter, Ref, Tags, Template
from troposphere.ec2 import PortRange, NetworkAcl, Route, \
    SubnetRouteTableAssociation, Subnet, RouteTable, \
    VPCGatewayAttachment, VPC, NetworkInterfaceProperty, NetworkAclEntry, \
    SubnetNetworkAclAssociation, EIP, Instance, InternetGateway

t = Template()

Vpc = t.add_resource(VPC(
    'Vpc',
    EnableDnsSupport=True,
    CidrBlock='10.1.0.0/16',
    EnableDnsHostnames=True,
))

t.add_output(Output('Vpc', Value=Ref(Vpc)))

file_name="child1.template"
f = open(file_name,"w+")
f.write(t.to_json())
f.close()
s3_client = boto3.client('s3')


response = s3_client.upload_file(file_name, 'cfntemplates-1', 'networks/'+file_name)

