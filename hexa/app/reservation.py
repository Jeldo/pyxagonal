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


# Implement Abstract Class
class ReservationAPIView(AbstractReservationAPIView):
    def __init__(self, reservation_service: AbstractReservationService):
        self.reservation_service: AbstractReservationService = reservation_service

    # 실제 파라미터는 도메인 모델이 아닌 gRPC, REST 등 클라이언트로부터의 통신 규약을 통해 받아오는 데이터
    def create_reservation(self, reservation: Reservation):
        print('create reservation in API View')
        self.reservation_service.create_reservation(reservation=reservation)

    def list_reservations(self) -> list[Reservation]:
        print('list reservations in API View')
        return self.reservation_service.list_reservations()
