
class User:

    name = None
    surname = None
    mail = None

    def __init__(self, mail, name, surname):
        self.mail = mail
        self.name = name
        self.surname = surname

    def say_hello(self):
        return "User %(name)s %(surname)s says hello." % {
            "name": self.name,
            "surname": self.surname
        }


class VIPUser(User):
    def __init__(self, mail, name, surname, vip_card_number):
        super(User, self).__init__(mail, surname)

        if(not isinstance(vip_card_number,(int))):
            vip_card_number = None
        self.vip_card_number = vip_card_number

    def check_card(self, new_number):
        if new_number > 999 and new_number % 2 == 0:
            return True
        else:
            return False

    def use_vip_card(self):
        return None

    def set_vip_card(self, new_card_number):
        if VIPUser.check_card(new_card_number):
        #if isinstance(new_card_number(int)) and new_card_number % 2 == 0:
            self.new_card_number = new_card_number

    def get_vip_number(self):
        return self.new_card_number





