import abc

from hexa.domain.model.reservation import Reservation


# Repository(Secondary Port) Interface
class AbstractReservationRepository(abc.ABC):
    @abc.abstractmethod
    def create_reservation(self, reservation: Reservation):
        raise NotImplementedError

    @abc.abstractmethod
    def list_reservations(self) -> list[Reservation]:
        raise NotImplementedError
