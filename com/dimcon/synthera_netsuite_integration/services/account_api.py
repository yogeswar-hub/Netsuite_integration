from com.dimcon.synthera_netsuite_integration.utilities.base_api_structure import BaseAPI

NETSUITE_BASE_URL = "https://TD3001609.suitetalk.api.netsuite.com/services/rest/record/v1"

class AccountAPI(BaseAPI):
    def __init__(self):
        super().__init__(NETSUITE_BASE_URL)
        self.endpoint = "account"
    
    def get_all(self, params=None):
        return self.fetch_all(self.endpoint, params)
    
    def get_by_id(self, account_id):
        return self.fetch_by_id(self.endpoint, account_id)
    
    def create(self, account_data):
        return self.insert(self.endpoint, account_data)
    
    def update(self, account_id, account_data):
        return self.update(self.endpoint, account_id, account_data)
    
    def delete(self, account_id):
        return self.delete(self.endpoint, account_id)

# Instantiate the AccountAPI for reuse, e.g., in your lambda entry point.
account_api = AccountAPI()