from Imports import *
class muayeneBasvurusuForm(Form):
    hastalik=SelectField("Hastalığınızı Seçiniz : ",choices=(["Baş Ağrısı","Göğüs Ağrısı","Kemik Ağrısı","Mide Ağrısı","Uyku Sorunu"]),validators=[validators.DataRequired("Lütfen Hastalığınızı Seçiniz")])
    #secmekIstediginizDoktor=SelectField("Doktorunuzu Seçiniz : ",choices=([]),validators=[validators.DataRequired("Lütfen Doktorunuzu Seçiniz")])