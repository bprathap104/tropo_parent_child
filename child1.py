import boto3
import time
import os
from troposphere import Base64, FindInMap, GetAtt, Join, Output
from troposphere import Parameter, Ref, Tags, Template
from troposphere.ec2 import PortRange, NetworkAcl, Route, \
    SubnetRouteTableAssociation, Subnet, RouteTable, \
    VPCGatewayAttachment, VPC, NetworkInterfaceProperty, NetworkAclEntry, \
    SubnetNetworkAclAssociation, EIP, Instance, InternetGateway

def child1():
    t = Template()
    Vpc = t.add_resource(VPC(
        'Vpc',
        EnableDnsSupport=True,
        CidrBlock='10.1.0.0/16',
        EnableDnsHostnames=True,
    ))
    t.add_output(Output('Vpc', Value=Ref(Vpc)))
    return(t)
