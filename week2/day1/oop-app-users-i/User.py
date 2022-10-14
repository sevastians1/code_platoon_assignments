# your User class goes here

class User:
    def __init__(self, name, email, driver_license):
        self.name = name
        self.email = email
        self.driver_license = driver_license

    def __str__(self):
        return f"My name is {self.name}, email address is {self.email} and my driver's license is {self.driver_license}"

    
samuel = User('Sam', 'Samuel.Daehan@gmail.com', 'DMJLKASK65165165')

print(samuel)
print(samuel.email)