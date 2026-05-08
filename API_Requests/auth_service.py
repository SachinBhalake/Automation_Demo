from API_Requests.endpoints import EndPoints


class AuthService:

    def __init__(self, client, logger):
        self.client = client
        self.logger = logger
        self.access_token = None

    def login(self, username, password):
        self.logger.info(f"Login user: {username}")

        response = self.client.post(
            EndPoints.Auth_User_Login,
            json={"username": username, "password": password}
        )

        if response.status_code == 200:
            data = response.json()
            self.access_token = data.get("accessToken")

            if not self.access_token:
                self.logger.error("Access token missing")
                raise ValueError("Access token missing in login response")

            self.client.set_token(self.access_token)
        else:
            self.access_token = None
            self.client.session.headers.pop("Authorization", None)
        return response
