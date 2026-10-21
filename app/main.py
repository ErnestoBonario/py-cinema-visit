from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    customers_objects = []
    for customer in customers:
        customers_objects.append(
            Customer(name=customer["name"], food=customer["food"])
        )
    for customer_object in customers_objects:
        CinemaBar.sell_product(
            product=customer_object.food,
            customer=customer_object,
        )
    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=customers_objects,
        cleaning_staff=cleaning_staff,
    )
