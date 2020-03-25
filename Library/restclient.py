from requests import  request
import json

class RestClient():
    
    def __init__(self):
        base_url = "https://api.trello.com/1"
        _media_type = "application/json"
        _consumer_key = "&oauth_consumer_key=a4cb61246f4bcb00a50b53cdacb63d7f"
        _consumer_secret = "&oauth_token=139dfa49b73d81287c50ce0660b4119db55034b4e9b2ff93ac57f79dada8465c"
        _payload = {}
        _headers = {"Accept": _media_type, "Content-Type": _media_type}
        _query_string = {}
        _end_point = None
        _url = None
    
    def create_request(self, end_point, query_string=None, payload=None):        
        # _url = RestClient._base_url + end_point + "?" + query_string + "&" + RestClient._consumer_key + RestClient._consumer_secret
        try:
            response = request("POST", self.base_url, headers=self._headers, data = self._payload)
            return json.loads(response.text).encode('uft8')            
        except Exception as err:
            pass
 
    
    @staticmethod
    def update_request():
        assert True
    
    @staticmethod
    def delete_request():
        assert True
    
    @staticmethod
    def read_request():
        assert True
