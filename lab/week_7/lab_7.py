from enum import Enum


class PaymentStatus(Enum):
  UNPAID, COMPLETED, FAILED = 1, 2, 3


class AccountStatus(Enum):
  ACTIVE, BLOCKED = 1, 2


class BookingStatus(Enum):
  RESERVED, PENDING, CANCELLED = 1, 2, 3


class Account:
  def __init__(self, id, password, status):
    self.__id = id
    self.__password = password
    self.__status = status

  def changePassword(self):
    pass


class Person:
  def __init__(self, fullname, email, phone_number, address, birth_date, emergency_contact_fullname, emergency_contact_phone_number):
    self.__fullname = fullname
    self.__email = email
    self.__phone_number = phone_number
    self.__address = address
    self.__birth_date = birth_date
    self.__emergency_contact_fullname = emergency_contact_fullname
    self.__emergency_contact_phone_number = emergency_contact_phone_number

  def makeBooking(self):
    pass

  def getBooking(self):
    pass


class FrontDesk(Person):
  def __init__(self, fullname, email, phone_number, address, birth_date, emergency_contact_fullname, emergency_contact_phone_number):
    super().__init__(fullname, email, phone_number, address, birth_date,
                     emergency_contact_fullname, emergency_contact_phone_number)

  def addBooking(self):
    pass

  def addSlot(self):
    pass

  def approveBooking(self):
    pass


class Customer(Person):
  def __init__(self, fullname, email, phone_number, address, birth_date, emergency_contact_fullname, emergency_contact_phone_number):
    super().__init__(fullname, email, phone_number, address, birth_date,
                     emergency_contact_fullname, emergency_contact_phone_number)


class Admin(Person):
  def __init__(self, fullname, email, phone_number, address, birth_date, emergency_contact_fullname, emergency_contact_phone_number):
    super().__init__(fullname, email, phone_number, address, birth_date,
                     emergency_contact_fullname, emergency_contact_phone_number)

  def addField(self):
    pass

  def editField(self):
    pass

  def deleteField(self):
    pass

  def addBooking(self):
    pass

  def approveBooking(self):
    pass

  def addNews(self):
    pass

  def editNews(self):
    pass

  def deleteNews(self):
    pass

  def addSlot(self):
    pass

  def editSlot(self):
    pass

  def deleteSlot(self):
    pass

  def blockUser(self):
    pass


class Guest:
  def __init__(self):
    pass

  def registerAccount(self):
    pass

  def loginAccount(self):
    pass


class News:
  def __init__(self, title, content, image_url, created_on, status):
    self.__title = title
    self.__content = content
    self.__image_url = image_url
    self.__created_on = created_on
    self.__status = status


class Booking:
  def __init__(self, booking_id, status, created_on, description):
    self.__booking_id = booking_id
    self.__status = status
    self.__created_on = created_on
    self.__description = description

  def cancel(self):
    pass


class BookingHistory:
  def __init__(self, booking):
    self.__booking = booking


class Equipment:
  def __init__(self, name, price, item):
    self.__name = name
    self.__price = price
    self.__item = item


class Vest(Equipment):
  def __init__(self, name, price, item):
    super().__init__(name, price, item)


class Football(Equipment):
  def __init__(self, name, price, item):
    super().__init__(name, price, item)


class Slot:
  def __init__(self, created_on, start_time, end_time):
    self.__created_on = created_on
    self.__start_time = start_time
    self.__end_time = end_time


class SlotDate(Slot):
  def __init__(self, created_on, start_time, end_time, date):
    super().__init__(created_on, start_time, end_time)
    self.__date = date


class Field:
  def __init__(self, name, description, price_by_slot, category, type):
    self.__name = name
    self.__description = description
    self.__price_by_slot = price_by_slot
    self.__category = category
    self.__type = type

  def getSlot(self):
    pass


class Category:
  def __init__(self, fields):
    self.__field_category = fields
    
  def search_by_category(self):
    pass
  
  def search_by_date(self):
    pass
    

class Payment:
  def __init__(self, amount, created_on, payment_status, transaction_id):
    self.__amount = amount
    self.__created_on = created_on
    self.__payment_status = payment_status
    self.__transaction_id = transaction_id


class QRCodeTransaction(Payment):
  def __init__(self, amount, created_on, payment_status, transaction_id, qr_code):
    super().__init__(amount, created_on, payment_status, transaction_id)
    self.__qr_code = qr_code


class CashTransaction(Payment):
  def __init__(self, amount, created_on, payment_status, transaction_id):
    super().__init__(amount, created_on, payment_status, transaction_id)
