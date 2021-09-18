from kafka import KafkaConsumer
import rocksdb
import json
import time
import threading
import ipfshttpclient
import functions
import document
import collision

from nanoid import generate
import time

client = ipfshttpclient.connect("/ip4/127.0.0.1/tcp/5002")
config = client.config.get()
print(config['Addresses'])



# Creating the db for collision and fire
db_collision = rocksdb.DB("test1.db", rocksdb.Options(create_if_missing=True))
# db_fire = rocksdb.DB("test2.db", rocksdb.Options(create_if_missing=True))

# Starting the Kafka Consumer
consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                                 auto_offset_reset='earliest')
                                #  value_deserializer=lambda m: json.loads(m.decode('utf-8')))

# Consuming the messages and pushing into rocksdb
def Kafka_consumer():
    consumer.subscribe(['incident_manager_topic'])
    for message in consumer:
        try:
            x = message.value # CID
            y = x.decode('UTF-8') # Converting from bytes to string
            y = y.replace('"', '')
            z = client.get_json(y) 
        except:
            if message is None:
                continue
            if message.error():
                print("Consumer error: {}".format(message.error()))
                continue
        else:
            if z['incident']['type'] == "collision":
                b_incidentid = bytes(z['incident']['id'], 'utf-8') # Converting into bytes
                b_z = json.dumps(z).encode('utf-8')
                db_collision.put(b_incidentid, b_z)
            # if x["incident_type"] == "fire":
            #     db_fire.put(y)
    consumer.close()

    

# Processing the items from db_collision
def collision_process():
    it = db_collision.iteritems()
    it.seek_to_first()   
    input_list = list(it) # Getting all the items from the db as list
    print("INPUT ITEM:")
    print(input_list)
    # db_collision.Close()
    try:
        if len(input_list) != 0:
            item = input_list.pop(0) # Fetching the first item from the input_list 
            name_key = item[0].decode('UTF-8') # Fetching the first element from item
            db_collision.delete(item[0]) # Deleting that key-value pair from db
            incident_block = json.loads(item[1].decode('utf-8')) # Converting the bytes to json type
            print("\nINCIDENT BLOCK:")
            print(incident_block)
            # db_collision.Close() 
        else:
            raise Exception()    
    except:
        print("Collision Db is empty")
        #terminate the thread
    else:       
        chain = []
        initial_document = document.document(generate(size=24), generate(size=24), "Q5bWqxBEKC6P8tqsKc98xmWNzrzDuRLMiMPL8wBuTGtMnR", time.time(), "document", "QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR", "0", "", "", "", "", "", "")
        print("\nINITIAL DOCUMENT")   
        print(initial_document)
        json_document = json.loads(initial_document)
        Document = functions.IncidentDocument(json_document, incident_block) # Creation of Initial Document
        print("\nDOCUMENT AFTER UPDATING WITH INCIDENT BLOCK:")
        print(Document)
        name_key = functions.createNamekey(Document) # Creation of name key
        print("\nNAME KEY:")
        print(name_key)
        document_cid = functions.publish_block(Document, name_key) # Publishing the Initial Document to IPFS
        print("\nDOCUMENT CID:")
        print(document_cid)
        functions.Blockchain(Document, chain) # Adding that to blockchain
        conversation_block = functions.createConversationBlock() # Creation of the Conversation block
        print("\nCONVERSATION BLOCK:")
        print(conversation_block)
        conversation_block_cid = functions.publish_block(conversation_block, name_key) # Publishing the Conversation block to IPFS
        print("\nCONVERSATION CID:")
        print(conversation_block_cid)
        document_update = functions.UpdateDocument(document_cid, conversation_block_cid) # Updation of Document with Conversation block
        print("\nDOCUMENT AFTER UPDATING WITH CONVERSATION BLOCK:")
        print(document_update)
        new_document_cid = functions.publish_block(document_update, name_key) # Publishing the updated document
        print("\nNEW DOCUMENT CID:")
        print(new_document_cid)
        functions.Blockchain(document_update, chain) # Adding the updated document to blockchain
        update_conversation = UpdateConversation(conversation_block_cid, new_document_cid, name_key, chain) # Updating the Conversation block
    

# Updation of Conversation block
def UpdateConversation(conversation_block_cid, new_document_cid, name_key, chain):
    conversation_block = client.get_json(conversation_block_cid)
    Document = client.get_json(new_document_cid)
    location = Document['document']['intialData']['location']
    vehicle_info = Document['document']['intialData']['vehicleInformation']
    collision.Collision()
    BOT = collision.Bot
    CLIENT = collision.User
    conversation_block['conversation_data']['BOT'] = BOT
    conversation_block['conversation_data']['CLIENT'] = CLIENT
    new_conversation_cid = functions.publish_block(conversation_block, name_key)
    new_document = functions.UpdateDocument(new_document_cid, new_conversation_cid)
    new_document_cid = functions.publish_block(new_document, name_key)
    functions.Blockchain(new_document, chain)
    collision.collision_Location(location)
    BOT = collision.Bot
    CLIENT = collision.User
    conversation_block['conversation_data']['BOT'] = BOT
    conversation_block['conversation_data']['CLIENT'] = CLIENT
    new_conversation_cid = functions.publish_block(conversation_block, name_key)
    new_document = functions.UpdateDocument(new_document_cid, new_conversation_cid)
    new_document_cid = functions.publish_block(new_document, name_key)
    functions.Blockchain(new_document, chain)
    collision.collision_Details(vehicle_info)
    BOT = collision.Bot
    CLIENT = collision.User
    conversation_block['conversation_data']['BOT'] = BOT
    conversation_block['conversation_data']['CLIENT'] = CLIENT
    new_conversation_cid = functions.publish_block(conversation_block, name_key)
    new_document = functions.UpdateDocument(new_document_cid, new_conversation_cid)
    new_document_cid = functions.publish_block(new_document, name_key)
    functions.Blockchain(new_document, chain)
    collision.collision_Livestatus()
    BOT = collision.Bot
    CLIENT = collision.User
    conversation_block['conversation_data']['BOT'] = BOT
    conversation_block['conversation_data']['CLIENT'] = CLIENT
    new_conversation_cid = functions.publish_block(conversation_block, name_key)
    new_document = functions.UpdateDocument(new_document_cid, new_conversation_cid)
    new_document_cid = functions.publish_block(new_document, name_key)
    functions.Blockchain(new_document, chain)
    collision.collision_EmergencyNum()
    BOT = collision.Bot
    CLIENT = collision.User
    conversation_block['conversation_data']['BOT'] = BOT
    conversation_block['conversation_data']['CLIENT'] = CLIENT
    new_conversation_cid = functions.publish_block(conversation_block, name_key)
    new_document = functions.UpdateDocument(new_document_cid, new_conversation_cid)
    new_document_cid = functions.publish_block(new_document, name_key)
    functions.Blockchain(new_document, chain)
    collision.collision_Call()
    BOT = collision.Bot
    CLIENT = collision.User
    conversation_block['conversation_data']['BOT'] = BOT
    conversation_block['conversation_data']['CLIENT'] = CLIENT
    new_conversation_cid = functions.publish_block(conversation_block, name_key)
    new_document = functions.UpdateDocument(new_document_cid, new_conversation_cid)
    new_document_cid = functions.publish_block(new_document, name_key)
    functions.Blockchain(new_document, chain)
    


    
# Starting the threads
threading.Thread(target=Kafka_consumer).start()
time.sleep(5)
threading.Thread(target=collision_process).start()