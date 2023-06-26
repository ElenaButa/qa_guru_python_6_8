import csv

from models.users import User


class UserProvider:

    def get_users(self) -> list[User]:
        raise NotImplementedError("Реализуйте эту функцию в конкретном провайдере")
