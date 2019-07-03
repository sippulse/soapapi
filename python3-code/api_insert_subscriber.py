#!/usr/bin/python3
# -*- coding: utf-8 -*-


import requests
from zeep import Client
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep.transports import Transport
from zeep import xsd

session = Session()
#Usuário e Senha da Integracao
session.auth = HTTPBasicAuth('', 'Senha')
subscriberWsdl = "http://189.90.58.142:8080/SipPulse/SubscriberWS?wsdl"
transport = Transport(session=session)

""""
Documentação das Bibliotecas utilizadas
Zeep: https://python-zeep.readthedocs.io/en/master/
Requests: https://requests.readthedocs.io/pt_BR/latest/user/quickstart.html
Data: 03/07/2019
Author: Eliakim F. Morais
Apoio Técnico: Vitor Hugo.
"""

def insertSubscriber():   
    client = Client(subscriberWsdl, transport=transport)
    #Insert com os parametros obrigatórios da API
    subscriber = {
        'subscriber' : [{
            'username': '4721060000',
            'domain':  '189.90.58.141',
            'password': '#4933300808#', 
            'profile': 'FLN_4396_STFC',
            'ratePlanId': 0,
            'resellerId': 0,
            'emailAddress': 'eliakim@sippulse.com', 
            'countryCode': '55',
            'areaCode': '48',
            'callLimit': 1,
            'voicemail': '0',
            'passwordPortal': '$senhadoportal#',
            'activeIncomingCalls': '1',
            'activeOutgoingCalls': '1',
            'blockAnonymousCalls': 'false',
            'blockCollectCalls': 'false',
            'lowCreditLimit': 'false',
            'lowCreditNotification': 'true',
            'resellerBillingType': '0',
            'resellerMarkup': '0.0',

        }],
        #Usuário e Senha da Integracao
        'principal' : [{
            'login': ' ',
            'password': ' ',
        }]
    } 
   
    response = client.create_message(client.service, "insertSubscriber", **subscriber)


insertSubscriber()
