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
import child1
import child2

timestr = time.strftime("%Y%m%d-%H%M%S")

def upload_file_to_s3(t, file_name):
    f = open(file_name,"w+")
    f.write(t.to_json())
    f.close()
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, 'cfntemplates-2', timestr + '/' + file_name)

def main():
    baseUrl='https://cfntemplates-1.s3.amazonaws.com/networks'
    t = Template()

    t.add_resource(Stack(
        'Child1',
        TemplateURL=baseUrl + "/child1.template",
    ))

    t.add_resource(Stack(
        'Child2',
        TemplateURL=baseUrl + "/child2.template",
        Parameters={
            'Vpc': GetAtt('Child1', 'Outputs.Vpc'),
        }
    ))
    upload_file_to_s3(t, 'parent.template')
    t = child1.child1()
    upload_file_to_s3(t, 'child1.template')
    t=child2.child2()
    upload_file_to_s3(t, 'child2.template')
if __name__ == '__main__':
    main()
    print(timestr)
