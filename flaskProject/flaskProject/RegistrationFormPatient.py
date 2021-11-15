from Imports import *
#Hasta Kayıt Alanı
class RegistrationFormPatient(Form):
    name = StringField("İsim Soyisim : ",validators=[validators.Length(min=3,max=26),validators.DataRequired("Lütfen İsim Giriniz")])
    phoneNumber= StringField("Telefon Numarası : ",validators=[validators.Length(min=11,max=11 ),validators.Regexp("(05|5)[0-9][0-9][1-9]([0-9]){6}",message="Lütfen Telefon Numaranızı Doğru Giriniz")])
    IdentityNumber = StringField("Kimlik No : ",validators=[validators.Length(min=11,max=11),validators.Regexp("^[1-9]{1}[0-9]{9}[02468]{1}$",message="Lütfen TC'nizi Doğru Giriniz")])
    email = EmailField("E-Mail Adresi : ",validators=[validators.Email("Lütfen Geçerli Bir Email Adresi Giriniz.")])
    password=PasswordField("Parola : ",validators=[
        validators.DataRequired("Lütfen Bir Parola Belirleyiniz"),
        validators.EqualTo('confirm',"Parolanız Uyuşmuyor!")
    ])
    confirm=PasswordField("Parola Doğrula")
