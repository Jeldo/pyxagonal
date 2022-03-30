import abc

from hexa.domain.model.reservation import Reservation
from hexa.domain.service.reservation import AbstractReservationService


# API View (Primary Port) Interface
class AbstractReservationAPIView(abc.ABC):
    @abc.abstractmethod
    def create_reservation(self, reservation: Reservation):
        raise NotImplementedError

    @abc.abstractmethod
    def list_reservations(self) -> list[Reservation]:
        raise NotImplementedError


# Implementation of Abstract Class
class ReservationAPIView(AbstractReservationAPIView):
    def __init__(self, reservation_service: AbstractReservationService):
        self.reservation_service: AbstractReservationService = reservation_service

    def create_reservation(self, reservation: Reservation):
        print('create reservation in API View')
        self.reservation_service.create_reservation(reservation=reservation)

    def list_reservations(self) -> list[Reservation]:
        print('list reservations in API View')
        return self.reservation_service.list_reservations()
