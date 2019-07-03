# -*- coding: utf-8 -*-


import requests

from zeep import Client
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep.transports import Transport

session = Session()
session.auth = HTTPBasicAuth(' ', ' ')
addressWsdl = "http://189.90.58.142:8080/SipPulse/AddressWS?wsdl"
transport = Transport(session=session)




def insertAddress(accountcode, domain, ipAddress, mask, method, port, protocol, username, techprefix, login, password): 
    client = Client(addressWsdl, transport=transport)

   
    address = {
        'address' : [{
            'account': accountcode,
            'domain': domain,
            'ipAddress': ipAddress, 
            'mask': mask,
            'method': method,
            'username': username, 
            'techPrefix': techprefix,
            'protocol': protocol,
            'port': port,
            'group': '1000',
        }],
        'principal' : [{
            'login': login,
            'password': password,
        }]

    }
    print(dir(client.service))
    #response = client.service.sendData(**address)
    response = client.service.insertAddress(**address)

insertAddress('eliakim@189.90.58.141', '189.90.58.141', '189.90.58.138', '32' 'techprefix','5060', 'udp','eliakim','9197',' ',' ')
