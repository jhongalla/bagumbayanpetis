from flask import *
from db.db import *

reg=Blueprint('reg',__name__,template_folder='../templates/registration',url_prefix='/registration')

@reg.route('/',methods=['get','post'])
def entry():
    if request.method=='POST':
        no=request.values.get('no')
        name=request.values.get('name')
        type=request.values.get('type')
        sex=request.values.get('sex')
        age=request.values.get('age')
        breed=request.values.get('breed')
        color=request.values.get('color')
        birthday=request.values.get('birthday')
        owner=request.values.get('owner')
        address=request.values.get('address')
        brgy=request.values.get('brgy')
        contact_no=request.values.get('contact_no')
        try:
            db=connection()
            cur=db.cursor()
            cur.execute("""INSERT INTO PETS(PET_NO,PET_NAME,PET_TYPE,PET_SEX,PET_AGE,PET_BREED,PET_COLOR,PET_BIRTHDAY,PET_OWNER,PET_ADDRESS,PET_BARANGAY,PET_CONTACT_NO)
                    VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
                    """,(no,name,type,sex,age,breed,color,birthday,owner,address,brgy,contact_no))
            db.commit()
            msg=f'Successfully Save!'
            return jsonify({'msg':msg})
        except Exception as e:
            return jsonify({'msg': e})
        except sqlite3.IntegrityError as e:
            return jsonify({'msg': e})
    else:
        return render_template('entry.html')