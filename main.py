from datetime import datetime
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Test:
  name: str


class Movie:
  def __init__(self, name: str, detail: str, genre: str, rating: float, length: int, release_date: datetime) -> None:
    self.__name = name
    self.__detail = detail
    self.__genre = genre
    self.__rating = rating
    self.__length = length
    self.__release_date = release_date

  @property
  def name(self) -> str:
    return self.__name

  @name.setter
  def name(self, name: str) -> None:
    self.__name = name


class Cinema:
  def __init__(self, name: str, total_cinema_hall: int, location: str) -> None:
    self.__name = name
    self.__total_cinema_hall = total_cinema_hall
    self.__location = location


class CinemaHall:
  def __init__(self, name: str, total_seat: int, shows: list) -> None:
    self.__name = name
    self.__total_seat = total_seat
    self.__shows = shows


class CinemaHallSeat:
  def __init__(self, seat_row: int, seat_col: int, seat_type: str) -> None:
    self.__seat_row = seat_row
    self.__seat_col = seat_col
    self.__seat_type = seat_type


class SeatPrice:
  def __init__(self, seat_type: str, price: float) -> None:
    self.__seat_type = seat_type
    self.__price = price


class Show:
  def __init__(self, start_time: datetime, end_time: datetime, played_at: str, movie: Movie) -> None:
    self.__start_time = start_time
    self.__end_time = end_time
    self.__played_at = played_at
    self.__movie = movie


class MovieCatalog:
  def __init__(self, last_update: datetime) -> None:
    self.__last_update = last_update
    self.__movies = []


class ShowSeat:
  def __init__(self, seat_no: int, price: float) -> None:
    self.__seat_no = seat_no
    self.__price = price
    self.__is_reserved = False


class Payment:
  def __init__(self, amount: float, transaction_id: str, payment_status: str) -> None:
    self.__amount = amount
    self.__transaction_id = transaction_id
    self.__payment_status = payment_status
    self.__created_at = datetime.now()


class Booking:
  def __init__(self, booking_no: str, no_of_seat: int, status: str, payment: Payment, show: Show) -> None:
    self.__booking_no = booking_no
    self.__no_of_seat = no_of_seat
    self.__status = status
    self.__payment = payment
    self.__show = show


class Admin:
  def __init__(self, name: str, email: str, phone: str) -> None:
    self.__name = name
    self.__email = email
    self.__phone = phone


class Customer:
  def __init__(self, name: str, email: str, phone: str) -> None:
    self.__name = name
    self.__email = email
    self.__phone = phone


class FrontDeskOfficer:
  def __init__(self, name: str, email: str, phone: str) -> None:
    self.__name = name
    self.__email = email
    self.__phone = phone


class PaymentProcessor(ABC):
  
  @abstractmethod
  def pay(self, order):
    pass
  
  
class PromptPay(PaymentProcessor):
  
  def pay(self, order):
    print('Paying with PromptPay')
    return Payment(order.total_price, '123456789', 'success')
 
if __name__ == '__main__':
  movie = Movie('The Godfather', 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
                'Crime, Drama', 9.2, 175, datetime(1972, 3, 24))
  print(movie.name)
  movie.name = 'The Godfather II'
  print(movie.name)
  
  test = Test('test')
  print(test.name)
