from API_Requests.endpoints import EndPoints


class UserAPI:

    def __init__(self, client, logger):
        self.client = client
        self.logger = logger

    def get_current_user(self):
        self.logger.info("Fetching current user")
        endpoint = EndPoints.Auth_User_Details
        response = self.client.get(endpoint)
        return response

    def get_all_users(self):
        self.logger.info("Fetching all users")
        endpoint = EndPoints.User_Get_All
        response = self.client.get(endpoint)
        return response

    def get_user_by_id(self, user_id):
        self.logger.info(f"Fetching user {user_id}")
        endpoint = EndPoints.User_Get_By_Id.format(id=user_id)
        response = self.client.get(endpoint)
        return response

    def create_user(self, payload):
        self.logger.info(f"Creating user: {payload}")
        endpoint = EndPoints.User_Create
        response = self.client.post(endpoint, json=payload)
        return response

    def update_user(self, user_id, payload):
        self.logger.info(f"Updating user {user_id}")
        endpoint = EndPoints.User_Update.format(id=user_id)
        response = self.client.put(endpoint, json=payload)
        return response

    def delete_user(self, user_id):
        self.logger.info(f"Deleting user {user_id}")
        endpoint = EndPoints.User_Delete.format(id=user_id)
        response = self.client.delete(endpoint)
        return response
