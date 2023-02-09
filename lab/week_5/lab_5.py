class Person:
    def __init__(self, fullname, address, email, phone, birth_date, tel, emergency_contact, account):
        self.__fullname = fullname
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__birth_date = birth_date
        self.__tel = tel
        self.__emergency_contact = emergency_contact
        self.__account = account


class Account:
    def __init__(self, id, password, status):
        self.__id = id
        self.__password = password
        self.__status = status


class Admin(Person):
    def __init__(self, fullname, address, email, phone, birth_date, tel, emergency_contact, account, managers_booking, adds_news, manages_field, manages_slot):
        super().__init__(fullname, address, email, phone,
                         birth_date, tel, emergency_contact, account)
        self.__managers_booking = managers_booking
        self.__adds_news = adds_news
        self.__manages_field = manages_field
        self.__manages_slot = manages_slot


class Customer(Person):
    def __init__(self, fullname, address, email, phone, birth_date, tel, emergency_contact, account, creates_booking):
        super().__init__(fullname, address, email, phone,
                         birth_date, tel, emergency_contact, account)
        self.__creates_booking = creates_booking


class News:
    def __init__(self, title, content, created_on, status, image_url, admins):
        self.__title = title
        self.__content = content
        self.__created_on = created_on
        self.__status = status
        self.__image_url = image_url
        self.admins = admins


class Booking:
    def __init__(self, booking_id, created_on, status, payment, customers, admins, slot_date):
        self.__booking_id = booking_id
        self.__created_on = created_on
        self.__status = status
        self.__payment = payment
        self.__customers = customers
        self.__admins = admins
        self.__slot_date = slot_date


class Payment:
    def __init__(self, amount, created_on, payment_status, transaction_id):
        self.__amount = amount
        self.__created_on = created_on
        self.__payment_status = payment_status
        self.__transaction_id = transaction_id


class CashTransaction(Payment):
    def __init__(self, amount, created_on, payment_status, transaction_id):
        super().__init__(amount, created_on, payment_status, transaction_id)


class QrcodeTransaction(Payment):
    def __init__(self, amount, created_on, payment_status, transaction_id, qrcode):
        super().__init__(amount, created_on, payment_status, transaction_id)
        self.__qrcode = qrcode


class Slot:
    def __init__(self, created_on, start_time, end_time, admins):
        self.__created_on = created_on
        self.__start_time = start_time
        self.__end_time = end_time
        self.__admins = admins


class SlotDate(Slot):
    def __init__(self, created_on, start_time, end_time, date):
        super().__init__(created_on, start_time, end_time)
        self.__date = date


class Field:
    def __init__(self, name, description, price_by_slot, category, type, slots, admins):
        self.__name = name
        self.__desciprtion = description
        self.__price_by_slot = price_by_slot
        self.__category = category
        self.__type = type
        self.__slots = slots
        self.__admins = admins
