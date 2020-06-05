#!/usr/bin/env python3

import zeep

wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
client = zeep.Client(wsdl=wsdl)
response = client.service.Method1('Zeep', 'is cool')
print("Response is of type:",type(response))
print("Reponse:",response)