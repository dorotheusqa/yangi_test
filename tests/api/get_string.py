from api.base_api import API


class GetStringAPI(API):
    def get_string(self, uuid):
        self._request(self.base_url + f"/{uuid}", "GET")
