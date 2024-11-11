from api.base_api import API


class PalindromeAPI(API):

    def create_palindrome_in_db(self):
        body = self._create_body(palindrome_flag=True)
        self._request(self.base_url, "POST", body)
        return self.response.json()

    def create_random_string_in_db(self):
        body = self._create_body(palindrome_flag=False)
        self._request(self.base_url, "POST", body)

    def send_empty_body(self):
        body = self._create_body(palindrome_flag="Empty")
        self._request(self.base_url, "POST", body)

    def send_method_not_allowed(self, method):
        body = self._create_body()
        self._request(self.base_url, method, body)

    def send_non_boolean_value_in_body(self, value):
        body = self._create_body(value=value, palindrome_flag="Non_boolean")
        self._request(self.base_url, "POST", body)


