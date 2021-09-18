# initial_document = {
#     "id": "",
#     "botid": "",
#     "did": "",
#     "timestamp": "",
#     "type": "",
#     "odid": "",
#     "previousLink": "0",
#     "signature": "",
#     "payload": "",
#     "controller": (),
#     "created_at": "",
#     "actions": "",
#     "document":{
#         "registrationType": "",
#         "registeredByDID": "",
#         "peopleInvolvedDid": "",
#         "adminDid": "",
#         "organisationdid": "",
#         "intialData":{
#             "location":{
#                 "id": "",
#                 "latitude": "",
#                 "longitude": "",
#                 "direction": "",
#                 "timestamp": ""
#             },
#             "media":{
#                 "id": "",
#                 "timestamp": "",
#                 "devicedid": "",
#                 "meta":{

#                 },
#                 "link":{ 

#                 }
#             },
#             "incident":{
#                 "id": "",
#                 "type": "",
#                 "locationid": ""
#             },
#             "vehicleInformation":{
#                 "id": "",
#                 "registrationNumber": ""
#             }
#         },
        
#         "isVerified": "",
#         "meta":{

#         },

#         "chatInformation":{
#             "id": "",
#             "conversation":{
#                 "id": "",
#                 "fromid": "",
#                 "toid": ""
#             } 
#         },
#         "media":{
#             "id": ""
#         },
#         "registrationVerificationBlock":{
#             "timestamp": "",
#             "id": "",
#             "content":{
#                 "payload": "",
#                 "verificiationPayload": ""
#             },
#             "signature": "",
#             "organisationSignature": "",
#             "adminSignature": "",
#             "ckdrSignature": "",
#             "controller": "",
#             "proof": "",
#             "nonce": "",
#             "verificationType": "",
#             "verificationMethod": ""
#         }
#     }
# }


# Import Module
import json

  
# Create function
  
  
def document(doc_id, bot_id, did, timestamp, type, odid, previousLink, signature, payload, controller, created_at, actions, isVerified):
  
    # Create Dictionary
    value = {
    "id": doc_id,
    "botid": bot_id,
    "did": did,
    "timestamp": timestamp,
    "type": type,
    "odid": odid,
    "previousLink": previousLink,
    "signature": signature,
    "payload": payload,
    "controller": controller,
    "created_at": created_at,
    "actions": actions,
    "document":{
        "registrationType": "",
        "registeredByDID": "",
        "peopleInvolvedDid": "",
        "adminDid": "",
        "organisationdid": "",
        "intialData":{
            "location":{
                "id": "",
                "latitude": "",
                "longitude": "",
                "direction": "",
                "timestamp": ""
            },
            "media":{
                "id": "",
                "timestamp": "",
                "devicedid": "",
                "meta":{

                },
                "link":{ 

                }
            },
            "incident":{
                "id": "",
                "type": "",
                "locationid": ""
            },
            "vehicleInformation":{
                "id": "",
                "registrationNumber": ""
            }
        },
        
        "isVerified": isVerified,
        "meta":{

        },

        "chatInformation":{
            "id": "",
            "conversation":{
                "id": "",
                "fromid": "",
                "toid": ""
            } 
        },
        "media":{
            "id": ""
        },
        "registrationVerificationBlock":
        {
            "timestamp": "",
            "id": "",
            "content":{
                "payload": "",
                "verificiationPayload": ""
            },
            "signature": "",
            "organisationSignature": "",
            "adminSignature": "",
            "ckdrSignature": "",
            "controller": "",
            "proof": "",
            "nonce": "",
            "verificationType": "",
            "verificationMethod": ""
        }
    }
}
  
    # Dictionary to JSON Object using dumps() method
    # Return JSON Object
    return json.dumps(value)
  
  
