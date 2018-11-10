from database import db
from flask import Blueprint
from database.models import URLList, ScrapedData

import url_master
ragnarok_bp = Blueprint('ragnarok', __name__)

# url_master_list = {'abingdon+herald': 'www.heraldseries.co.uk',
#                    'accrington+observer': 'www.accringtonobserver.co.uk'}


@ragnarok_bp.route('/ragnarok/', methods=['GET'])
def ragnarok():

    db.session.close()
    db.drop_all()
    db.create_all()


    for name, url in url_master.url_master_list.items():
        print(name)

        new_url = URLList(
            name = name,
            url = url
        )


        db.session.add(new_url)


    db.session.commit()




    return "NUKED!! ☢ (and rebuilt database)"
