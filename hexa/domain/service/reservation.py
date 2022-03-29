from abc import ABC

from hexa.domain.model.reservation import Reservation
from hexa.domain.repository.reservation import AbstractReservationRepository


# Service Interface
class AbstractReservationService(ABC):
    def create_reservation(self, reservation: Reservation):
        raise NotImplementedError

    def list_reservations(self) -> list[Reservation]:
        raise NotImplementedError


# Implement Abstract Class
class ReservationService(AbstractReservationService):
    def __init__(self, reservation_repository: AbstractReservationRepository):
        self.reservation_repository: AbstractReservationRepository = reservation_repository

    def create_reservation(self, reservation: Reservation):
        print('create reservation in service')
        self.reservation_repository.create_reservation(reservation=reservation)

    def list_reservations(self) -> list[Reservation]:
        print('list reservations in service')
        return self.reservation_repository.list_reservations()
