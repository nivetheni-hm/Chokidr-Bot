import document
import ipfshttpclient
import time

client = ipfshttpclient.connect()


print(client.id())