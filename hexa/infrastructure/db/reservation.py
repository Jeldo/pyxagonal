from hexa.domain.model.reservation import Reservation
from hexa.domain.repository.reservation import AbstractReservationRepository


# Implementation of Abstract Class
class ReservationRepository(AbstractReservationRepository):
    def __init__(self, db: list[Reservation]):  # 의존성 주입
        self.reservation_db = db

    def create_reservation(self, reservation: Reservation):
        print('create reservation in repository')
        self.reservation_db.append(reservation)

    def list_reservations(self) -> list[Reservation]:
        print('list reservations in repository')
        return self.reservation_db
