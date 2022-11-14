class CookieJar:
    def __init__(self, cookie_number):
        self.cookie_number = cookie_number

    @property
    def cookie_number(self):
        return self.__cookie_number

    @cookie_number.setter
    def cookie_number(self, cookie_number):
        self.__cookie_number = cookie_number


jar_cookie = CookieJar(5)
print(jar_cookie.cookie_number)
jar_cookie.cookie_number = 10
print(jar_cookie.cookie_number)

