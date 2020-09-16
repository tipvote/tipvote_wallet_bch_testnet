from app import db
from decimal import Decimal

from app.models import BchWalletTest


def checkbalance(user_id, amount):
    userwallet = BchWalletTest.query.filter(BchWalletTest.user_id == user_id).first()
    curbal = Decimal(userwallet.currentbalance) + Decimal(amount)
    amounttocheck = Decimal(amount)

    if Decimal(amounttocheck) <= Decimal(curbal):
        return 1
    else:
        return 0

