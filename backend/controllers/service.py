import connexion
import datetime
import uuid
import logging
from werkzeug.exceptions import NotFound, InternalServerError, BadRequest
from flask import jsonify

from backend.models.account import Account  # noqa: E501
from backend.models.array_of_transactions import ArrayOfTransactions  # noqa: E501
from backend.models.transaction import Transaction  # noqa: E501
from backend.models.transaction_request import TransactionRequest  # noqa: E501
from backend.models.database import Accounts
from backend.models.database import Transactions
from backend import db


logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)


def get_accounts_by_id(account_id):
    """Returns the account data by account_id

    Args:
        account_id (String(UUID)): _description_

    Raises:
        NotFound: No account found with account_id
        InternalServerError: Unable to find record in database

    Returns:
        Account: Response schema consists of account_id and balance
    """
    try:
        account_entry = (
            db.session.query(Accounts)
            .filter(Accounts.account_id.like(account_id))
            .first()
        )

        if not account_entry:
            raise NotFound(f"No account found with account_id={account_id}")

        response = {
            "account_id": account_entry.account_id,
            "balance": account_entry.balance,
        }
    except NotFound:
        raise
    except Exception as e:
        logging.error("An error ocurred with database connection: %s", e)
        raise InternalServerError("Unable to find record in database")

    return Account(**response), 200


def get_transactions():
    """Get all transactions

    Returns:
        ArrayOfTransactions: List of all transactions with account_id, amount, created_at and transaction_id
    """
    query = db.session.query(Transactions).all()
    response = [
        {
            "account_id": transaction_entry.account_id,
            "amount": transaction_entry.amount,
            "created_at": transaction_entry.created_at,
            "transaction_id": transaction_entry.transaction_id,
        }
        for transaction_entry in query
    ]

    return [Transaction(**res) for res in response], 200


def get_transactions_by_id(transaction_id):  # noqa: E501
    """Get transaction by transaction_id

    Args:
        transaction_id (String(UUID)): Transaction ID

    Raises:
        NotFound: No transaction found with transaction_id

    Returns:
        Transaction: Response schema consists of account_id, amount, created_at, transaction_id
    """
    try:
        transaction_entry = (
            db.session.query(Transactions)
            .filter(Transactions.transaction_id.like(transaction_id))
            .first()
        )

        if not transaction_entry:
            raise NotFound(f"No transaction found with transaction_id={transaction_id}")

        response = {
            "account_id": transaction_entry.account_id,
            "amount": transaction_entry.amount,
            "created_at": transaction_entry.created_at,
            "transaction_id": transaction_entry.transaction_id,
        }
    except NotFound:
        raise
    except Exception as e:
        logging.error("An error ocurred with database connection: %s", e)
        raise InternalServerError("Unable to find record in database")

    return Transaction(**response), 200


def ping():  # noqa: E501
    """Healhcheck to make sure the service is up.

    Returns:
        String: The service is up and running.
    """
    return "The service is up and running.", 200


def post_transactions(payload=None):  # noqa: E501
    """Creates a new transaction.

    Args:
        payload (Dictionary, optional): Consists of account_id and amount. Defaults to None.

    Raises:
        InternalServerError: Unable to find/update record in database

    Returns:
        Transaction: Response schema consists of account_id, amount, created_at, transaction_id
    """
    if connexion.request.is_json:
        payload = TransactionRequest.from_dict(
            connexion.request.get_json()
        )  # noqa: E501

    try:
        uuid_account_id = uuid.UUID(payload.account_id)
    except Exception as e:
        logging.error("Account id is not a valid uuid: %s", e)
        raise BadRequest("Account id is not a valid uuid")

    payload_dict = payload.to_dict()
    account_id = payload_dict["account_id"]
    amount = payload_dict["amount"]
    transaction_id = str(uuid.uuid4())
    created_at = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")

    try:
        account_entry = (
            db.session.query(Accounts)
            .filter(Accounts.account_id.like(account_id))
            .first()
        )

        if account_entry:
            account_entry_dict = {
                "balance": account_entry.balance + amount,
            }
            account_entry.update(**account_entry_dict)
            logging.info("Account record already exists. Updating the record")
        else:
            account_entry_dict = {
                "account_id": account_id,
                "balance": amount,
            }
            account_entry = Accounts(**account_entry_dict)
            logging.info("Account record does not exist. Creating the record")

        response = {
            "account_id": account_id,
            "amount": amount,
            "created_at": created_at,
            "transaction_id": transaction_id,
        }
        trans_entry = Transactions(**response)
        logging.info("New transaction created")
        db.session.add(account_entry)
        db.session.add(trans_entry)
        db.session.commit()
    except Exception as e:
        logging.error("An error ocurred with database connection: %s", e)
        raise InternalServerError("Unable to find/update record in database")

    return Transaction(**response), 201
