import pytest

import datetime

from unittest import mock

from app.main import outdated_products


class TestCorrectResults:

    @pytest.mark.parametrize(
        "input_list,expected_result,input_time",
        [
            (
                [
                    {
                        "name": "salmon",
                        "expiration_date": datetime.date(2022, 2, 10),
                        "price": 600
                    },
                    {
                        "name": "chicken",
                        "expiration_date": datetime.date(2022, 2, 5),
                        "price": 120
                    },
                    {
                        "name": "duck",
                        "expiration_date": datetime.date(2022, 2, 1),
                        "price": 160
                    }
                ],
                [
                    "duck"
                ],
                [
                    datetime.date(2022, 2, 2)
                ]
            )
        ]
    )
    @mock.patch("app.main.datetime")
    def test_outdated_products(
            self,
            mocked_time: callable,
            input_list: list,
            expected_result: list,
            input_time: datetime.date,
    ) -> None:
        mocked_time.date.today.return_value = datetime.date(2022, 2, 2)
        assert outdated_products(input_list) == expected_result

    @mock.patch("app.main.datetime.date")
    def test_called_datetime(
            self,
            mocked_time: callable,
    ) -> None:
        mocked_time.today.return_value = datetime.date(2022, 2, 2)
        outdated_products([])
        mocked_time.assert_called_once()
