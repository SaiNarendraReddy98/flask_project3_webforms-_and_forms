from flask import Flask,render_template,request
from flask_wtf import Form
from wtforms import StringField,SubmitField,PasswordField


FAI = Flask(__name__)


@FAI.route('/htmlform',methods=['GET','POST'])
def htmlform():

    return render_template('htmlform.html')




class WebForm(Form):
    name = StringField()
    password = PasswordField()
    submit = SubmitField()




@FAI.route('/webform',methods=['GET','POST'])
def webform():
    WFO = WebForm()
    if request.method == 'POST':
        WFD = WebForm(request.form)
        if WFD.validate():
            return WFD.data
        
    return render_template('webform.html',WFO=WFO)









if __name__ == '__main__':
    FAI.run(debug=True)