import time
import json

IIncident = {
        "@context": ['http://schema.org'],
        "@id": "Cf3RvmCbuYLzi-106UfgFAYt",
        "location":
        {
            "id": "H0hOQiyKFF5D9wtypPBxqFQ7",
            "latitude": "12.9516° N",
            "longitude": "80.1462° E",
            "direction": "",
            "timestamp": time.time()

        },
        "media":
        {
            "id": "QNQ_WvdBh-amSnT5jLfMB2SD",
            "timestamp": time.time(),
            "devicedid": "Wi0Dr6A82-62CxHMyAJzlcVs",
            "link": ""
        },
        "incident":
        {
            "id": "nG8c6PQ3RjdgXN5luS59Icw5",
            "type": "collision",
            "location_id": "XO22yBqKarCnqxk_LH6JSvFu"
        },
        "vehicleInformation":
        {
            "id": "J5EwamAb-8JMZlde8suR5Dh3",
            "type": "car",
            "registrationNumber": "KA-03-HA-1985"
        }
}



# # # res = json.loads(initial_document)
# # initial_document['document']['intialData'] = IIncident
# # print (json.dumps(initial_document))

# import ipfshttpclient
# from ipfshttpclient.client import key
# client = ipfshttpclient.connect()
# guhan = QmS6Nz3aDxMcmcukAd7tueETj9mU451XbchD5BeuGqzvEm
# path1 = '/ipfs/'
# path2 = 'QmS6Nz3aDxMcmcukAd7tueETj9mU451XbchD5BeuGqzvEm'
# path = path1+path2
# print(path)
# # # client.key_gen(IIncident['incident']['id'])
# namekey = client.key.gen(key_name = "sample12", type = "rsa")
# print(namekey)
# res = client.name.publish(path, key = namekey['Name'])
# print(res)
# # print(key)

# # res1 = client.get_json("QmS6Nz3aDxMcmcukAd7tueETj9mU451XbchD5BeuGqzvEm")
# # print(res1)
