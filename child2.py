import boto3
import time
import os
from troposphere import Base64, FindInMap, GetAtt, Join, Output
from troposphere import Parameter, Ref, Tags, Template
from troposphere.ec2 import PortRange, NetworkAcl, Route, \
    SubnetRouteTableAssociation, Subnet, RouteTable, \
    VPCGatewayAttachment, VPC, NetworkInterfaceProperty, NetworkAclEntry, \
    SubnetNetworkAclAssociation, EIP, Instance, InternetGateway, SecurityGroup
def child2():
    t = Template()

    t.add_parameter(Parameter(
        'Vpc',
        Type='String',
        Description='Vpc Ref'))

    t.add_resource(SecurityGroup(
        'SG1',
        GroupDescription='Allows SSH access from anywhere',
        VpcId=Ref('Vpc'),  # finally I can reference a sibling stack's resource
    ))
    return(t)
