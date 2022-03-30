import abc
from hexa.domain.model.reservation import Reservation
from hexa.domain.repository.reservation import AbstractReservationRepository


# Service Interface
class AbstractReservationService(abc.ABC):
    @abc.abstractmethod
    def create_reservation(self, reservation: Reservation):
        raise NotImplementedError

    @abc.abstractmethod
    def list_reservations(self) -> list[Reservation]:
        raise NotImplementedError


# Implementation of Abstract Class
class ReservationService(AbstractReservationService):
    def __init__(self, reservation_repository: AbstractReservationRepository):
        self.reservation_repository: AbstractReservationRepository = reservation_repository

    def create_reservation(self, reservation: Reservation):
        print('create reservation in service')
        self.reservation_repository.create_reservation(reservation=reservation)

    def list_reservations(self) -> list[Reservation]:
        print('list reservations in service')
        return self.reservation_repository.list_reservations()
