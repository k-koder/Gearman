from gearman import GearmanClient
import gearman 

import pickle

class PickleDataEncoder(gearman.DataEncoder):
    @classmethod
    def encode(cls, encodable_object):
        return pickle.dumps(encodable_object)

    @classmethod
    def decode(cls, decodable_string):
        return pickle.loads(decodable_string)

class PickleExampleClient(gearman.GearmanClient):
    data_encoder = PickleDataEncoder
    
mypythonobject = {'hello': 'there'}
    
new_client = PickleExampleClient(['127.0.0.1:4730']) # input localhost
current_request=new_client.submit_job("dict", mypythonobject) #summit task     
new_result = current_request.result 
print new_result
