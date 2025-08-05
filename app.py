from flask import *
from routes.registration import reg
from routes.vacination import vac
from routes.reports import report

app=Flask(__name__)
app.register_blueprint(reg)
app.register_blueprint(vac)
app.register_blueprint(report)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login',methods=['get','post'])
def login():
    if request.method=='POST':
        user=request.values.get('usr')
        pas=request.values.get('pas')
        if user=='jhong' and pas=='@jhong16':
            return jsonify({'html':url_for('index')})
        else:
            return jsonify({'html':url_for('home'),'msg':'Username or Password not found! PLease try again!'})
    else:
        return redirect(url_for('home'))
    
@app.route('/index')
def index():
    return render_template('index.html')



if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port='30')