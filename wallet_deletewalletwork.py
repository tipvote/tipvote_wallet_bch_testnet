from app import db
from app.models import BchWalletWorkTest


# run once every ten minutes


# run once every day
def deleteoldorder():

    getwork = BchWalletWorkTest.query.filter_by(type=0).all()
    if getwork:
        for f in getwork:
            db.session.delete(f)
        db.session.commit()
    else:
        print("no work!")


if __name__ == '__main__':
    deleteoldorder()