from hexa.app.reservation import ReservationAPIView
from hexa.domain.model.reservation import Reservation
from hexa.domain.service.reservation import ReservationService
from hexa.infrastructure.db.reservation import ReservationRepository

mysql = []
repository = ReservationRepository(db=mysql)
service = ReservationService(reservation_repository=repository)
view = ReservationAPIView(reservation_service=service)

# HTTP 요청으로 가정
create_reservation_request = Reservation("NAME")
view.create_reservation(reservation=create_reservation_request)  # POST Create Reservation
reservations = view.list_reservations()  # GET List Reservations
print(reservations)
