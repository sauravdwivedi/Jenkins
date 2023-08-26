from backend import db
import datetime


class Accounts(db.Model):
    __tablename__ = "accounts"
    account_id = db.Column(db.String(64), primary_key=True)
    balance = db.Column(db.Integer, default=0)

    transaction = db.relationship("Transactions", back_populates="account")

    def update(self, **kwargs) -> None:
        for item in kwargs.items():
            setattr(self, item[0], item[1])


class Transactions(db.Model):
    __tablename__ = "transactions"
    transaction_id = db.Column(db.String(64), primary_key=True)
    account_id = db.Column(
        db.String(64),
        db.ForeignKey("accounts.account_id"),
    )
    created_at = db.Column(
        db.String(64),
        default=datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f"),
    )
    amount = db.Column(db.Integer, default=0)

    account = db.relationship("Accounts", back_populates="transaction")
