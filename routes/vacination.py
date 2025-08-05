from flask import *
from db.db import connection

vac=Blueprint('vac',__name__,url_prefix='/vaccination')

@vac.route('/')
def vaccination():
    return render_template('vaccination/vaccination.html')

@vac.route('/addvaccination/<code>')
def add_vaccination(code):
        return render_template('vaccination/vaccination.html',code=code)

@vac.route('/new_vaccination',methods=['get','post'])
def new_vaccination():
        if request.method=='POST':
              pet=request.values.get('pet')
              date_vax=request.values.get('date_vax')
              vax=request.values.get('vax')
              lotno=request.values.get('lotno')
              date_next_vax=request.values.get('date_next_vax')
              vet_lic_no=request.values.get('vet_lic_no')
              db=connection()
              cur=db.cursor()
              cur.execute("""INSERT INTO VACCINE(PET,DATE_VACCINE,VACCINE,LOTNO,DATE_NEXT_VACCINE,VET_LIC_NO)
                          VALUES(?,?,?,?,?,?)""",
                          (pet,date_vax,vax,lotno,date_next_vax,vet_lic_no))
              db.commit()
              cur.execute("Select * from vaccine order by id desc")
              rw=cur.fetchall()
              return jsonify({'msg':'Data successfully Added!','html':url_for('vac.vax_display_all')})
        else:
            return render_template('vaccination/vaccination.html')
        
@vac.route('/Vax_delete/<i>')
def vax_delete(i):
              db=connection()
              cur=db.cursor()
              cur.execute("DELETE from vaccine where id='" + i + "'")
              db.commit()
              return redirect(url_for('vac.vax_display_all'))

@vac.route('/vax_display_all')
def vax_display_all():
    db=connection()
    cur=db.cursor()
    cur.execute("Select * from vaccine order by id desc")
    rw=cur.fetchall()
    return render_template("vaccination/vax_list_all.html",rw=rw)

@vac.route('/vax_find',methods=['get','post'])
def vax_find():
    cri=request.form["txtsearch"]
    db=connection()
    cur=db.cursor()
    cur.execute("Select * from vaccine where pet like '%"+cri+"%' or lotno like '%"+cri+"%'  order by id desc")
    rw=cur.fetchall()
    return render_template("vaccination/vax_list_all.html",rw=rw)

@vac.route('/update_vaccination',methods=['get','post'])
def update_vaccination():
        if request.method=='POST':
              id=request.values.get('id')
              pet=request.values.get('pet')
              date_vax=request.values.get('date_vax')
              vax=request.values.get('vax')
              lotno=request.values.get('lotno')
              date_next_vax=request.values.get('date_next_vax')
              vet_lic_no=request.values.get('vet_lic_no')
              db=connection()
              cur=db.cursor()
              cur.execute("""UPDATE VACCINE SET PET=?,DATE_VACCINE=?,VACCINE=?,LOTNO=?,DATE_NEXT_VACCINE=?,VET_LIC_NO=? WHERE ID=?""",
                          (pet,date_vax,vax,lotno,date_next_vax,vet_lic_no))
              db.commit()
              cur.execute("Select * from vaccine order by id desc")
              rw=cur.fetchall()
              return jsonify({'msg':'Data successfully Added!','html':url_for('vac.vax_display_all')})
        else:
            return render_template('vaccination/vaccination.html')