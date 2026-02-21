class Login:
    def authenticate(self):
        pass

class Password(Login):
    def authenticate(self):
        print("Authenticated using Password")

class OTP(Login):
    def authenticate(self):
        print("Authenticated using OTP")


u = OTP()
u.authenticate()