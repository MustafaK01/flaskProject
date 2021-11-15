from Imports import *
#Doktor Kayıt Alanı
class RegistrationFormDoctor(Form):
    name = StringField("İsim Soyisim : ",validators=[validators.Length(min=3,max=26),validators.DataRequired("Lütfen İsim Giriniz")])
    doctorTitle=SelectField("Ünvanınızı Seçiniz : ",choices=(["Pratisyen Doktor","Uzman Doktor","Operatör Doktor","Yardımcı Doçent","Doçent","Profesör"]),validators=[validators.DataRequired("Lütfen Ünvanınızı Seçiniz")])
    doctorBranch=SelectField("Branşınızı Seçiniz : ",choices=(["Nöroloji","Kardiyoloji","Ortopedi","Dahiliye","Psikiyatri"]),validators=[validators.DataRequired("Lütfen Branşınızı Seçiniz")])
    IdentityNumber = StringField("Kimlik No : ",validators=[validators.Length(min=11,max=11),validators.Regexp("^[1-9]{1}[0-9]{9}[02468]{1}$",message="Lütfen TC'nizi Doğru Giriniz")])
    recordNo = StringField("Sicil No : ",validators=[validators.Length(min=11,max=11),validators.Regexp("^[1-9]{1}[0-9]{9}[02468]{1}$",message="Lütfen Sicil Numaranızı Doğru Giriniz")])
    password=PasswordField("Parola : ",validators=[
        validators.DataRequired("Lütfen Bir Parola Belirleyiniz"),
        validators.EqualTo('confirm',"Parolanız Uyuşmuyor!")
    ])
    confirm=PasswordField("Parola Doğrula")