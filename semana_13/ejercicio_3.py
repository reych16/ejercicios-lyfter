from datetime import date

class User:
    def __init__(self, birth_year):
        self.birth_year = birth_year

    @property
    def age(self):
        today = date.today().year
        return today - self.birth_year


def adult_only(func):
    def wrapper(user, *args, **kwargs):
        if user.age < 18:
            raise Exception("User is underage.")
        return func(user, *args, **kwargs)
    return wrapper

@adult_only
def buy_alcohol(user):
    print("Purchase allowed!")

user1 = User(2000)
user2 = User(2010)

buy_alcohol(user1)