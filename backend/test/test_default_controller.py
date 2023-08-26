from __future__ import absolute_import

from flask import json
from six import BytesIO

from backend.models import Account  # noqa: E501
from backend.models import ArrayOfTransactions  # noqa: E501
from backend.models import Transaction  # noqa: E501
from backend.models import TransactionRequest  # noqa: E501
from backend.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_ping(self):
        """Test case for ping

        Healhcheck to make sure the service is up.
        """
        response = self.client.open("/ping", method="GET")
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_post_transactions(self):
        """Test case for post_transactions

        Creates a new transaction.
        """
        body = {"account_id": "5ae0ef78-e902-4c40-9f53-8cf910587312", "amount": -9}
        response = self.client.open(
            "/transactions",
            method="POST",
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert500(response, "Response body is : " + response.data.decode("utf-8"))

    def test_get_accounts_by_id(self):
        """Test case for get_accounts_by_id

        Returns the account data.
        """
        response = self.client.open(
            "/accounts/{account_id}".format(
                account_id="5ae0ef78-e902-4c40-9f53-8cf910587312"
            ),
            method="GET",
        )
        self.assert500(response, "Response body is : " + response.data.decode("utf-8"))

    def test_get_transactions(self):
        """Test case for get_transactions

        Get transactions
        """
        response = self.client.open("/transactions", method="GET")
        self.assert500(response, "Response body is : " + response.data.decode("utf-8"))

    def test_get_transactions_by_id(self):
        """Test case for get_transactions_by_id

        Returns the transaction by id.
        """
        response = self.client.open(
            "/transactions/{transaction_id}".format(
                transaction_id="38400000-8cf0-11bd-b23e-10b96e4ef00d"
            ),
            method="GET",
        )
        self.assert500(response, "Response body is : " + response.data.decode("utf-8"))


if __name__ == "__main__":
    import unittest

    unittest.main()
