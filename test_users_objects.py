import csv

import pytest


# -------------------------------------------------------------------
# Используем объектный подход работы с данными
# -------------------------------------------------------------------

@pytest.fixture
def users(provider) -> list:
    pass


@pytest.fixture
def workers(users) -> list:
    pass


def test_workers_are_adults_v3(workers):
    pass