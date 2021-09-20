import document
import ipfshttpclient
import time

client = ipfshttpclient.connect("/ip4/127.0.0.1/tcp/5001")

# Creation of Blockchain
def Blockchain(Document, chain):
    chain.append(Document)
    print("\nBLOCKCHAIN")
    print(*chain, sep = "\n")

# Creation of Initial Document
def IncidentDocument(json_document, incident_block):
    initial_document = json_document 
    initial_document['document']['intialData'] = incident_block # Updation with Incident Block
    return initial_document

# Creation of Name key
def createNamekey(Document):
    try:
        keyname = Document['document']['intialData']['incident']['id']
        keys = client.key.list()
        list = keys['Keys']
        if not any(d['Name'] == keyname for d in list):
            print("Does not exist")
        else:
            raise Exception()
    except:
        print("The given key exist")
        name_key = keyname
    else:
        key_name = client.key.gen(key_name = keyname, type = "ed25519")
        name_key = key_name['Name']

    return name_key

# Publishing to IPFS under a name key
def publish_block(block, name_key):
    res = client.add_json(block) 
    path1 = '/ipfs/'
    path = path1+res
    print("\nPublishing to IPFS")
    start = time.perf_counter()
    res1 = client.name.publish(path, key = name_key)  
    print("\nIPNS NAME ID:")
    print(res1)
    print("\nTIME TAKEN FOR EXECUTION:")
    print(time.perf_counter() - start)
    return res

# Creation of Conversation block
def createConversationBlock():
    chatConversation_block = {
        "id": "string",
        "conversation":
        {
            "id": "string",
            "fromid": "string",
            "toid": "string"
        },
        "conversation_data":
        {
            "BOT": [],
            "CLIENT": []
        }
    }
    return chatConversation_block

# Updation of Document with Conversation block
def UpdateDocument(document_cid, conversation_block_cid, ):
    conversation_block = client.get_json(conversation_block_cid)
    Document = client.get_json(document_cid)
    Document['document']['chatInformation'] = conversation_block
    Document['previousLink'] = document_cid
    return Document