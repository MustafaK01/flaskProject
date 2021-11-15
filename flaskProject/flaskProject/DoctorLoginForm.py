from Imports import *
class DoctorLoginForm(Form):
    #string input alanları
    IdentityNumber = StringField("Kimlik No : ",validators=[validators.Length(min=11,max=11),validators.Regexp("^[1-9]{1}[0-9]{9}[02468]{1}$",message="Lütfen TC'nizi Doğru Giriniz")])
    name=StringField("İsiminizi Girin : ")
    recordNo = StringField("Sicil No : ",validators=[validators.Length(min=11,max=11),validators.Regexp("^[1-9]{1}[0-9]{9}[02468]{1}$",message="Lütfen Sicil Numaranızı Doğru Giriniz")])
    password=PasswordField("Parolanızı Girin : ")