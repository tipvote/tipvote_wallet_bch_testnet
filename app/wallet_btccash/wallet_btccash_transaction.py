from app import db
from datetime import datetime
from app.models import TransactionsBchTest


def btc_cash_addtransaction(category, amount, userid, comment, shard, orderid, balance):
    """
    #
    :param category:
    :param amount:
    :param userid:
    :param comment:
    :param shard:
    :param orderid:
    :param balance:
    :return:
    """

    now = datetime.utcnow()
    comment = str(comment)
    orderid = int(orderid)

    trans = TransactionsBchTest(
        category=category,
        userid=userid,
        confirmations=0,
        confirmed=1,
        txid='',
        blockhash='',
        timeoft=0,
        timerecieved=0,
        otheraccount=0,
        address='',
        fee=0,
        created=now,
        commentbtc=comment,
        amount=amount,
        shard=shard,
        orderid=orderid,
        balance=balance,
        digital_currency=3

    )
    db.session.add(trans)
    db.session.commit()
