from flask import *
from db.db import connection



report=Blueprint('report',__name__,url_prefix='/reports')

@report.route('/')
def home():
    return render_template('reports/reports.html')


@report.route('/brgy_figures')
def brgy_figures():
    db=connection()
    cur=db.cursor()
    cur.execute("""Select PET_BARANGAY,PET_TYPE,count(pet_no) as figure
                ,count(CASE WHEN PET_SEX='MALE' THEN PET_SEX END) as MALE 
                ,count(CASE WHEN PET_SEX='FEMALE' THEN PET_SEX END) as FEMALE 
                from PETs GROUP by PET_BARANGAY,PET_TYPE""")
    rw=cur.fetchall()
    return render_template('reports/brgy_figures.html',rw=rw)