from enum import Enum


class PaymentStatus(Enum):
  UNPAID, COMPLETED, FAILED = 1, 2, 3


class AccountStatus(Enum):
  ACTIVE, BLOCKED = 1, 2


class BookingStatus(Enum):
  RESERVED, PENDING, CANCELLED = 1, 2, 3


class Account:
  def __init__(self, id, password, status):
    self.id = id
    self.password = password
    self.status = status

  def resetPassword(self):
    pass


class Person:
  def __init__(self, full_name, address, phone_number, email, birth_date, emergency_contact, emergency_contact_phone_number):
    self.full_name = full_name
    self.address = address
    self.phone_number = phone_number
    self.email = email
    self.birth_date = birth_date
    self.emergency_contact = emergency_contact
    self.emergency_contact_phone_number = emergency_contact_phone_number

  def makeBooking(self):
    pass

  def getBooking(self):
    pass


class Admin(Person):
  def __init__(self, full_name, address, phone_number, email, birth_date, emergency_contact, emergency_contact_phone_number):
    super().__init__(full_name, address, phone_number, email,
                     birth_date, emergency_contact, emergency_contact_phone_number)

  def addField(self):
    pass

  def addBooking(self):
    pass

  def addNews(self):
    pass

  def addSlot(self):
    pass


class Customer(Person):
  def __init__(self, full_name, address, phone_number, email, birth_date, emergency_contact, emergency_contact_phone_number):
    super().__init__(full_name, address, phone_number, email,
                     birth_date, emergency_contact, emergency_contact_phone_number)


class Guest:
  def __init__(self):
    pass

  def registerAccount(self):
    pass


class Booking:
  def __init__(self, booking_id, status, created_on, description):
    self.booking_id = booking_id
    self.status = status
    self.created_on = created_on
    self.description = description

  def cancel(self):
    pass

  def approve(self):
    pass


class Slot:
  def __init__(self, created_on, start_time, end_time):
    self.created_on = created_on
    self.start_time = start_time
    self.end_time = end_time


class SlotDate(Slot):
  def __init__(self, created_on, start_time, end_time, date):
    super().__init__(created_on, start_time, end_time)
    self.date = date


class Field:
  def __init__(self, name, description, price_by_slot, category, type):
    self.name = name
    self.description = description
    self.price_by_slot = price_by_slot
    self.category = category
    self.type = type

  def getSlot(self):
    pass


class Category:
  def __init__(self, field_category):
    self.field_category = field_category


class News:
  def __init__(self, title, content, image_url, created_on, status):
    self.title = title
    self.content = content
    self.image_url = image_url
    self.created_on = created_on
    self.status = status


class Equipment:
  def __init__(self, name, price, item):
    self.name = name
    self.price = price
    self.item = item


class Vest(Equipment):
  def __init__(self, name, price, item):
    super().__init__(name, price, item)


class Football(Equipment):
  def __init__(self, name, price, item):
    super().__init__(name, price, item)


class Payment:
  def __init__(self, amount, created_on, payment_status, transaction_id):
    self.amount = amount
    self.created_on = created_on
    self.payment_status = payment_status
    self.transaction_id = transaction_id


class QRCodeTransaction(Payment):
  def __init__(self, amount, created_on, payment_status, transaction_id, qrcode_url):
    super().__init__(amount, created_on, payment_status, transaction_id)
    self.qrcode_url = qrcode_url


class CashTransaction(Payment):
  def __init__(self, amount, created_on, payment_status, transaction_id):
    super().__init__(amount, created_on, payment_status, transaction_id)
