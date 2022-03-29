# Repository(Secondary Port) Interface
from abc import ABC

from hexa.domain.model.reservation import Reservation


class AbstractReservationRepository(ABC):
    def create_reservation(self, reservation: Reservation):
        raise NotImplementedError

    def list_reservations(self) -> list[Reservation]:
        raise NotImplementedError
