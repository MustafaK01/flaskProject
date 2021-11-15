from RegistrationFormPatient import *
from RegistrationFormDoctor import *
from PatientLoginForm import *
from DoctorLoginForm import *
from MuayeneBasvuruForm import *
def login_required(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        if "logged_in" in session:
            return f(*args,**kwargs)
        else:
            flash("Bu Sayfayı Görüntülemek İçin Giriş Yapın!!")
            return redirect(url_for("login"))

    return decorated_function
app=Flask(__name__)
#MYSQL konfigürasyonu
app.config["MYSQL_HOST"]="127.0.0.1"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="hastane"
app.config["MYSQL_CURSORCLASS"]="DictCursor"

mysql=MySQL(app)

#flash mesajları için secret key
app.secret_key="hastaneProjesi"

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/doctors")
def doctors():
    list1 = [{"id":1,"title":"Doktor1"},
            {"id":2,"title":"Doktor2"},
            {"id":3,"title":"Doktor3"}]
    return render_template("doctors.html",list1=list1)

@app.route("/register",methods=["GET","POST"])
def register():
    return render_template("register.html")

@app.route("/dRegistration",methods=["GET","POST"])
def doctorRegistration():
    form = RegistrationFormDoctor(request.form)
    if (request.method == 'POST' and form.validate()):
        name=form.name.data
        doctorTitle=form.doctorTitle.data
        doctorBranch=form.doctorBranch.data
        identityNumber=form.IdentityNumber.data
        recordNo=form.recordNo.data
        password=sha256_crypt.encrypt(form.password.data)
        cursor = mysql.connection.cursor()
        sorgu="INSERT INTO doctors(name,doctortitle,doctorbranch,recordno,identitynumber,password) VALUES(%s,%s,%s,%s,%s,%s)"
        cursor.execute(sorgu,(name,doctorTitle,doctorBranch,recordNo,identityNumber,password))
        mysql.connection.commit()
        cursor.close()

        flash("Başarıyla Kayıt Oldunuz . . .","success")
        return redirect(url_for("login"))
    else:
        pass
    return render_template("dRegistration.html",form=form)
@app.route("/login",methods=["GET","POST"])
def login():
    return render_template("login.html")
@app.route("/pRegistration",methods=["GET","POST"])
def patientRegistration():
    form = RegistrationFormPatient(request.form)
    if (request.method == 'POST' and form.validate()):
        name=form.name.data
        identityNumber=form.IdentityNumber.data
        phoneNumber=form.phoneNumber.data
        email=form.email.data
        password=sha256_crypt.encrypt(form.password.data)
        cursor = mysql.connection.cursor()
        sorgu="INSERT INTO hastalar(name,email,phonenumber,identitynumber,password) VALUES(%s,%s,%s,%s,%s)"
        cursor.execute(sorgu,(name,email,phoneNumber,identityNumber,password))
        mysql.connection.commit()
        cursor.close()

        flash("Başarıyla Kayıt Oldunuz . . .","success")
        return redirect(url_for("login"))
    else:
        pass
    return render_template("pRegistration.html",form=form)


@app.route("/PatientLogin",methods=["GET","POST"])
def PatientLogin():
    form=PatientLoginForm(request.form)
    if(request.method=="POST"):
        identityNumber=form.IdentityNumber.data
        name=form.name.data
        entered_password=form.password.data
        cursor=mysql.connection.cursor()
        sorgu="SELECT * FROM hastalar where identitynumber = %s and name = %s"
        concl = cursor.execute(sorgu,(identityNumber,name))
        if(concl>0):
            x=cursor.fetchone()
            pass_from_db=x["password"]
            if(sha256_crypt.verify(entered_password,pass_from_db)):
                flash("Başarıyla Giriş Yaptınız..")
                session['number']=3
                session["logged_in"]=True
                session["username"]=name
                return redirect(url_for("index"))
            else:
                flash("Parolanızı Yanlış Girdiniz!!")
                return redirect(url_for("login"))
        else:
            flash("Böyle Bir Kullanıcı Bulunmuyor..")
            return redirect(url_for("login"))

    else:
        return render_template("PatientLogin.html",form=form)

@app.route("/DoctorLogin",methods=["GET","POST"])
def DoctorLogin():
    form=DoctorLoginForm(request.form)
    if(request.method=="POST"):
        identityNumber=form.IdentityNumber.data
        entered_name=form.name.data
        entered_password=form.password.data
        entered_recordNo=form.recordNo.data
        cursor=mysql.connection.cursor()
        sorgu="SELECT * FROM doctors where identitynumber = %s and name = %s and recordno = %s"
        concl = cursor.execute(sorgu,(identityNumber,entered_name,entered_recordNo))
        if(concl>0):
            x=cursor.fetchone()
            pass_from_db=x["password"]
            if(sha256_crypt.verify(entered_password,pass_from_db)):
                flash("Başarıyla Giriş Yaptınız..")
                session['number']=4
                session["logged_in"]=True
                session["username"]=entered_name
                return redirect(url_for("index"))
            else:
                flash("Parolanızı Yanlış Girdiniz!!")
                return redirect(url_for("login"))
        else:
            flash("Böyle Bir Kullanıcı Bulunmuyor..")
            return redirect(url_for("login"))
    else:
        return render_template("DoctorLogin.html",form=form)

@app.route("/logout")
def logout():
    session.clear()
    flash("Başarıyla Çıkış Yaptınız...")
    return redirect(url_for("index"))

@app.route("/muayeneler")
@login_required
def muayeneler():
    
    return render_template("muayeneler.html")

@app.route("/muayeneBasvurusu")
@login_required
def muayeneBasvurusu():

    return render_template("muayeneBasvurusu.html")

@app.route("/basvuruYap",methods=["GET","POST"])
def basvuruYap():
    hastalıklar=["Baş Ağrısı","Göğüs Ağrısı","Kemik Ağrısı","Mide Ağrısı","Uyku Sorunu"]
    poliklinikler=["Nöroloji","Kardiyoloji","Ortopedi","Dahiliye","Psikiyatri"]
    form=muayeneBasvurusuForm(request.form)
    if(request.method=="POST"):
        hastalikTuru=form.hastalik.data
        name=session["username"]
        cursor = mysql.connection.cursor()
        for i in range(0,5):
            if(hastalikTuru==hastalıklar[i]):
                sorgu="INSERT INTO basvurular(name,hastalik,basvurulacak_pol) VALUES(%s,%s,%s)"
                cursor.execute(sorgu,(name,hastalikTuru,poliklinikler[i]))
        flash("Başvurunuz Yapıldı")
        if(hastalikTuru==None):
            flash("Lütfen Seçiminizi Yapınız")
            redirect(url_for("muayeneBasvurusu"))

        mysql.connection.commit()
        cursor.close()
    return render_template("basvuruYap.html",form=form)

@app.route("/muayeneleriGor")
def muayeneleriGor():
    cursor=mysql.connection.cursor()
    cursor2=mysql.connection.cursor()
    cursor3=mysql.connect.cursor()
    sorgu1="SELECT doctorbranch FROM `doctors` WHERE name=%s"
    cursor.execute(sorgu1,(session["username"],))
    a=cursor.fetchall()
    
    if(a==({'doctorbranch': 'Psikiyatri'},) ):
        sorgu2="SELECT name,hastalik FROM `basvurular` WHERE basvurulacak_pol=%s"
        sorgu3="SELECT COUNT(hastalik) FROM basvurular WHERE basvurulacak_pol=%s"
        cursor3.execute(sorgu3,("Psikiyatri",))
        cursor2.execute(sorgu2,("Psikiyatri",))
        q=cursor2.fetchall()
        numberOfPatient=cursor3.fetchall()[0]['COUNT(hastalik)']
        xHastalik=[]
        yName=[] 
        for i in range(0,numberOfPatient):
            xHastalik.append(q[i]['hastalik'])
            yName.append(q[i]['name'])
        return render_template("muayeneleriGor.html",xHastalik=xHastalik,yName=yName)
    elif(a==({'doctorbranch': 'Nöroloji'},) ):
        sorgu2="SELECT name,hastalik FROM `basvurular` WHERE basvurulacak_pol=%s"
        sorgu3="SELECT COUNT(hastalik) FROM basvurular WHERE basvurulacak_pol=%s"
        cursor3.execute(sorgu3,("Nöroloji",))
        cursor2.execute(sorgu2,("Nöroloji",))
        q=cursor2.fetchall()
        numberOfPatient=cursor3.fetchall()[0]['COUNT(hastalik)']
        xHastalik=[]
        yName=[] 
        for i in range(0,numberOfPatient):
            xHastalik.append(q[i]['hastalik'])
            yName.append(q[i]['name'])
        return render_template("muayeneleriGor.html",xHastalik=xHastalik,yName=yName)
    elif(a==({'doctorbranch': 'Ortopedi'},) ):
        sorgu2="SELECT name,hastalik FROM `basvurular` WHERE basvurulacak_pol=%s"
        sorgu3="SELECT COUNT(hastalik) FROM basvurular WHERE basvurulacak_pol=%s"
        cursor3.execute(sorgu3,("Ortopedi",))
        cursor2.execute(sorgu2,("Ortopedi",))
        q=cursor2.fetchall()
        numberOfPatient=cursor3.fetchall()[0]['COUNT(hastalik)']
        xHastalik=[]
        yName=[] 
        for i in range(0,numberOfPatient):
            xHastalik.append(q[i]['hastalik'])
            yName.append(q[i]['name'])
        return render_template("muayeneleriGor.html",xHastalik=xHastalik,yName=yName)
    elif(a==({'doctorbranch': 'Kardiyoloji'},) ):
        sorgu2="SELECT name,hastalik FROM `basvurular` WHERE basvurulacak_pol=%s"
        sorgu3="SELECT COUNT(hastalik) FROM basvurular WHERE basvurulacak_pol=%s"
        cursor3.execute(sorgu3,("Kardiyoloji",))
        cursor2.execute(sorgu2,("Kardiyoloji",))
        q=cursor2.fetchall()
        numberOfPatient=cursor3.fetchall()[0]['COUNT(hastalik)']
        xHastalik=[]
        yName=[] 
        for i in range(0,numberOfPatient):
            xHastalik.append(q[i]['hastalik'])
            yName.append(q[i]['name'])
        return render_template("muayeneleriGor.html",xHastalik=xHastalik,yName=yName)
    elif(a==({'doctorbranch': 'Dahiliye'},) ):
        sorgu2="SELECT name,hastalik FROM `basvurular` WHERE basvurulacak_pol=%s"
        sorgu3="SELECT COUNT(hastalik) FROM basvurular WHERE basvurulacak_pol=%s"
        cursor3.execute(sorgu3,("Dahiliye",))
        cursor2.execute(sorgu2,("Dahiliye",))
        q=cursor2.fetchall()
        numberOfPatient=cursor3.fetchall()[0]['COUNT(hastalik)']
        xHastalik=[]
        yName=[] 
        for i in range(0,numberOfPatient):
            xHastalik.append(q[i]['hastalik'])
            yName.append(q[i]['name'])
        return render_template("muayeneleriGor.html",xHastalik=xHastalik,yName=yName)
    else:
        flash("Muayeneniz Bulunmuyor.!.!")
if __name__=="__main__":
    app.run(debug=True)
