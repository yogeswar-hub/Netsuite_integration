import os
import json
from requests_oauthlib import OAuth1
from com.dimcon.synthera_netsuite_integration.utilities.secrets_manager import SecretsManagerHandler

# Compute the absolute path to config.ini located in the same folder as auth_service.py
current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, "config.ini")

class AuthService:
    def __init__(self):
        # Load the secret JSON string from the "netsuite" section.
        secret_str = SecretsManagerHandler.get_secret(config_file=config_path, section="netsuite")
        
        # Parse it into a dict.
        creds = json.loads(secret_str)
        print("Credentials loaded:", creds)
        
        # Build the OAuth1 object once (per cold start) including the realm if provided.
        self.auth = OAuth1(
            creds["consumer_key"],
            client_secret=creds["consumer_secret"],
            resource_owner_key=creds["token_key"],
            resource_owner_secret=creds["token_secret"],
            signature_method="HMAC-SHA256",
            realm=creds.get("account")  # if NetSuite expects the account as realm
        )

    def get_oauth(self):
        return self.auth

# Instantiate at module load.
auth_service = AuthService()