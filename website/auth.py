from flask import Blueprint,render_template,request,flash

auth=Blueprint('auth',__name__)

@auth.route('/login',methods=['POST'])
def login():
    data=request.form
    print(data)
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<p>Logout</>"

@auth.route('/sign-up',methods=['POST'])
def sign_up():
    email=request.form.get('email')
    fname=request.form.get('fname')
    password=request.form.get('password')
    password2=request.form.get('password2')



    if len(email)<4:
        flash('Email must be greater than 3 character',category="error")
    elif len(fname)<2:
        flash('Email must be greater than 1 character',category="error")
        
    elif (password != password2):
        flash('Password don\'t match',category="error")
        
    elif len(password)<8:
        flash('Passwod must be greater than 8 character',category="error")
        
    else:
        #add user to database
        flash('Account created',category="success")


    return render_template("sign-up.html")


