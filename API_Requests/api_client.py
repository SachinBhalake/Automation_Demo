import requests


class APIClient:
    def __init__(self, base_url, headers=None, timeout=30, logger=None):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(headers or {})
        self.timeout = timeout
        self.logger = logger

    def request(self, method, endpoint, timeout=None, **kwargs):
        url = f"{self.base_url}{endpoint}"

        self.logger.info(f"{method} {url}")

        try:
            response = self.session.request(
                method=method,
                url=url,
                timeout=timeout or self.timeout,
                **kwargs
            )
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Request failed: {e}")
            raise

        self.logger.info(f"Response: {response.status_code}")

        if response.status_code >= 400:
            self.logger.error(f"Response Body: {response.text[:500]}")
        else:
            self.logger.debug(f"Response Body: {response.text[:500]}")

        return response

    def get(self, endpoint, **kwargs):
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self.request("POST", endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self.request("PUT", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.request("DELETE", endpoint, **kwargs)

    def set_token(self, token):
        self.session.headers.update({
            "Authorization": f"Bearer {token}"
        })