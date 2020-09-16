
from app import db

from app.models import \
    BchWalletTest, \
    TransactionsBchTest, \
    BchWalletAddressesTest


def getnewaddress(user_id):
    """
    THIS function gets a new address for the user
    :param user_id:
    :return:
    """
    userswallet = db.session.query(BchWalletTest).filter_by(user_id=user_id).first()
    x = db.session.query(BchWalletAddressesTest).filter(BchWalletAddressesTest.status == 0).first()

    # Test to see if user doesnt have any current incomming transactions..get new one if not
    incdeposit = db.session.query(TransactionsBchTest)
    incdeposit = incdeposit.filter(TransactionsBchTest.category == 3,
                                   TransactionsBchTest.confirmed == 0,
                                   TransactionsBchTest.user_id == user_id,
                                   )
    incdeposit = incdeposit.first()
    if incdeposit is None:
        # status 0 = not used
        # status 1 = current main
        # status 2 = used
        if userswallet.address1status == 1:
            userswallet.address1status = 2
            userswallet.address2 = x.bchaddress
            userswallet.address2status = 1
            userswallet.address3status = 0

            x.user_id = user_id
            x.status = 1

            db.session.add(x)
            db.session.add(userswallet)
            db.session.commit()

        elif userswallet.address2status == 1:
            userswallet.address2status = 2
            userswallet.address3 = x.bchaddress
            userswallet.address3status = 1
            userswallet.address1status = 0

            x.user_id = user_id
            x.status = 1

            db.session.add(x)
            db.session.add(userswallet)
            db.session.commit()

        elif userswallet.address3status == 1:
            userswallet.address3status = 2
            userswallet.address1 = x.bchaddress
            userswallet.address1status = 1
            userswallet.address2status = 0

            x.user_id = user_id
            x.status = 1

            db.session.add(userswallet)
            db.session.add(x)
            db.session.commit()
        elif userswallet.address3status == 0 \
                and userswallet.address2status == 0 \
                and userswallet.address1status == 0:
            userswallet.address3status = 2
            userswallet.address1 = x.bchaddress
            userswallet.address1status = 1
            userswallet.address2status = 0

            x.user_id = user_id
            x.status = 1

            db.session.add(userswallet)
            db.session.add(x)
            db.session.commit()
        elif userswallet.address3status == 1 \
                and userswallet.address2status == 1 \
                and userswallet.address1status == 1:
            userswallet.address3status = 2
            userswallet.address1 = x.bchaddress
            userswallet.address1status = 1
            userswallet.address1status = 1
            userswallet.address2status = 0

            x.user_id = user_id
            x.status = 1

            db.session.add(userswallet)
            db.session.add(x)
            db.session.commit()
        elif userswallet.address3status == 2 \
                and userswallet.address2status == 2 \
                and userswallet.address1status == 2:
            userswallet.address3status = 2
            userswallet.address1 = x.bchaddress
            userswallet.address1status = 1
            userswallet.address2status = 0

            x.user_id = user_id
            x.status = 1

            db.session.add(userswallet)
            db.session.add(x)
            db.session.commit()
        elif userswallet.address3status == 3 \
                and userswallet.address2status == 3 \
                and userswallet.address1status == 3:
            userswallet.address3status = 2
            userswallet.address1 = x.bchaddress
            userswallet.address1status = 1
            userswallet.address2status = 0

            x.user_id = user_id
            x.status = 1

            db.session.add(userswallet)
            db.session.add(x)
            db.session.commit()
        else:
            pass

