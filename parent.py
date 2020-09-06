import boto3
import time
import os
from troposphere import Base64, FindInMap, GetAtt, Join, Output
from troposphere import Parameter, Ref, Tags, Template
from troposphere.cloudformation import Stack
from troposphere.ec2 import PortRange, NetworkAcl, Route, \
    SubnetRouteTableAssociation, Subnet, RouteTable, \
    VPCGatewayAttachment, VPC, NetworkInterfaceProperty, NetworkAclEntry, \
    SubnetNetworkAclAssociation, EIP, Instance, InternetGateway

baseUrl='https://cfntemplates-1.s3.amazonaws.com/networks'
t = Template()

t.add_resource(Stack(
    'Child1',
    TemplateURL=baseUrl + "/child1.template",
))

#t.add_resource(Stack(
#    'Child2',
#    TemplateURL=baseUrl + "/child2.template",
#    Parameters={
#        'Vpc': GetAtt('Child1', 'Outputs.Vpc'),
#    }
#))


file_name="parent.template"
f = open(file_name,"w+")
f.write(t.to_json())
f.close()
s3_client = boto3.client('s3')


response = s3_client.upload_file(file_name, 'cfntemplates-1', 'networks/'+file_name)

