from flask import Flask, render_template,request, session, send_file, flash,jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from SamplePDF import create_pdf
from Caption_Creator import generate_captcha
from sqlalchemy import func

# from sqlalchemy import select

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345@localhost/crud_new1'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///friends.db'

# Application Secret Key
app.secret_key = 'Baigan'  # Replace with your secret key

# Initialize The Database
db = SQLAlchemy(app)

# Create a Model
class Friends (db.Model) :
    id = db.Column(db.Integer, primary_key = True)
    sectionCode = db.Column(db.String(200), nullable = False)
    descriptions  = db.Column(db.String(200), nullable = False)
    punishments = db.Column(db.String(200), nullable = False)
    # Method to convert the object to a dictionary
    # def as_dict(self):
    #     return {
    #         'id': self.id,
    #         'username': self.sectionCode
    #     }
    # print (' In the user login')
    
class UserLogin (db.Model) :
    id = db.Column(db.Integer, primary_key = True)
    userName = db.Column(db.String(200), nullable = False)
    password = db.Column(db.String(200), nullable =False)

class BNSSections (db.Model) :
    id = db.Column(db.Integer, primary_key = True)
    IPC_Section = db.Column(db.String(200), nullable = False)
    IPC_Heading = db.Column(db.String(200), nullable = False)
    BNS_Section = db.Column(db.String(200), nullable = False)
    BNS_Heading = db.Column(db.String(200), nullable = False)

   

    # # Create a return function when we add.
    # def __repr__(self):
    #     return '<userName r%>' % self.userName
    
    

subscriber = []
@app.route('/', methods=['POST', 'GET'])


def home():
    userNameInput = request.form.get("userName")
    password = request.form.get("password")
    ipc = request.form.get("IPCCode")

    print ("IPC", ipc)

    print (userNameInput, password)
    title = "Thank you !!"
    if request.method == 'GET':
        # Render the form when accessed via GET request
        return render_template('Error_Handle.html')

    # Checks
    # message = ''
    # if userNameInput == '' and password != '' :
    #     message = 'Please add UserName'
    #     print("In 2")
    #     return render_template("Error_Handle.html", message = message)
    # if userNameInput != '' and password == '' :
    #     message = 'Please add Password mandatory'
    #     print("In 3")
    #     return render_template("Error_Handle.html", message = message)
    # Check username and password
    # if userNameInput != '' and password != '' :
    if userNameInput == '':
        return jsonify({'error' : 'Please add username'}),400
    if userNameInput == '':
        return jsonify({'error' : 'Please add Password'}),400
    if userNameInput != '' and password != '':
        print("UserInput: " , userNameInput)
        message1 = db.session.query(UserLogin.userName).where(UserLogin.userName == userNameInput, UserLogin.password == password).all()
        db.session.commit()
        db.session.close()
        print ('message1 : ', message1)
        if message1:
        # If the username is correct, return success
            print("Inside Condition")
            return jsonify({'message': 'Login Successfully!'})
        else:
            print("Inside Outise")
            # If the username is incorrect, return an error
            return jsonify({'error': 'Incorrect username or password!'}), 400
         

        # if message1 == [] and userNameInput != '' and password != '':
        #     message = 'UserName or Password are Incorrect'
        #     return jsonify({'message': 'Username is correct!'})
        #     return render_template("Error_Handle.html", message = message)
        # if message1 != ''  :
        #     message = 'User is successfully log in', message1
        #     print("Message Inside :",message1)
        #     return jsonify({'message': 'Username is correct!'})
            # return render_template("Error_Handle.html", message = message)
        
    # print ('userName : ', userNameInput)
    # print ('password : ', password)

    # return render_template("Error_Handle.html", title = title,message = message)

@app.route('/addUser', methods=['POST', 'GET'])
def addUser():
    title = 'Please Add User'
    return render_template("addUser.html", title = title)



@app.route('/about', methods=['POST', 'GET'])
def Documents():
    message  = 'Document Creation'
    applicationtemp = request.form.get('application')
    print ('applicationtemp : ', applicationtemp)

    # if applicationtemp == None :
    #     return jsonify({'error' : 'Please add Info'}),400

    if applicationtemp != None :
        create_pdf((request.form.get('judgeName')),(request.form.get('courtName')),(request.form.get('courtLocation')),
                request.form.get('petitionerName'),request.form.get('petitionerAddress'),request.form.get('petitionerRelativeName'),
                request.form.get('accussedName'),request.form.get('accussedAddress'),request.form.get('accussedRelativesName'),
                request.form.get('FIRNumber'),request.form.get('policeStationName'),request.form.get('underSection'),
                request.form.get('NDOH'),request.form.get('Place'),request.form.get('currentDate'),request.form.get('applicantName'),
                request.form.get('councilName'),request.form.get('application'))
    
        return render_template("about.html", message  = message)
    return render_template("about.html", message  = message)
    


    
    

@app.route('/subscribe', methods=['POST', 'GET'])
def subscribe():
    title = "Welcome to Channel"
    return render_template("subscribe.html", title= title)



@app.route('/friends', methods=['POST', 'GET'])
def friends():
    title = "Welcome to Law Enforcement"
    # print (title)

    if request.method == 'GET':
        return render_template('friends.html')
    
    # sectionCode = request.form.get('IPCCode').strip()
    friend_name_IPC = request.form.get('IPCCode')
    friend_name_BNS = request.form.get('BNSCode')
    print (f'friend_name_IPC : {friend_name_IPC}')
    print (f'friend_name_BNS : {friend_name_BNS}')
    # if friend_name_IPC == '' :
    #     friend_name_IPC = None

    # print ("Check : ", friend_name_IPC)
    # print ('Input Text: ', Friends.descriptions)
    # IPC Block 
    # if friend_name_IPC == None:
    #     print("In IPC")
    #     

    
    
    if friend_name_IPC != None :
        IPCCode_Check =  Friends.query.filter_by(sectionCode=f'section {friend_name_IPC}').all()
        if IPCCode_Check == [] :
            print ("Null DB response",IPCCode_Check)
            return jsonify({'error' : 'Input Session not Found'}),400
        IPCCode = db.session.query(Friends.sectionCode,Friends.descriptions,Friends.punishments).where(Friends.sectionCode ==  f'section {friend_name_IPC}' ) 
        if IPCCode:
            result_list = [
                {
                    'BNS_Section': row.sectionCode,
                    'BNS_Heading': row.descriptions,
                    'IPC_Section': row.punishments
                }
                for row in IPCCode
            ]
            return jsonify({'message': 'Data found!', 'data': result_list})   
            
        # print (f"IPCode response {IPCCode}")
        # print (f"Section sectionCode: {Friends.sectionCode}" )
        # friends2 = Friends.query.filter_by(sectionCode=f'section {friend_name_IPC}').all()
        # has_friends=len(friends2)
        # print ("has_friends : " , has_friends)
        # db.session.commit()
        # db.session.close()
        # # return jsonify({'message' : IPCCode})
        # return render_template("friends.html", title= title, friends = IPCCode, has_friends=1)
    # if friend_name_IPC == None and friend_name_BNS == '':
        # return render_template("friends.html", title= title, has_friends=0)

    # # Query the database using SQLAlchemy
    # ipcCode = Friends.query.filter(func.lower(Friends.sectionCode) == func.lower(sectionCode)).first()
    # print("IPC Code in DB : ", ipcCode)

    # if ipcCode:
    #     # Print the user object to the console
    #     print(f"User found: Section={Friends.sectionCode}, Username={Friends.descriptions}, Punishment={Friends.punishments}")
        
    #     # Return success with user details
    #     # return jsonify({'message': 'Section is correct!', 'Section': Friends.sectionCode})
    #     return jsonify({
    #         'message': 'Username is correct!',
    #         'user': Friends.as_dict()  # Convert the user object to a dictionary
    #     })
    # else:
    #     # Print to the console that no user was found
    #     print(f"No Section found in Code: {sectionCode}")
        
    #     # Return error
    #     return jsonify({'error': 'Incorrect Section!'}), 400
    
    if friend_name_BNS != None:
        print(f"BNS is {friend_name_BNS}")
        BNSCode_Check =  BNSSections.query.filter_by(BNS_Section=friend_name_BNS).all()
        # BNSCode = db.session.query(BNSSections.BNS_Section, BNSSections.BNS_Heading,BNSSections.IPC_Section).where(BNSSections.BNS_Section == friend_name_BNS)
        # BNSCode2 = BNSSections.query.filter_by(BNS_Section = friend_name_BNS).all()
        if BNSCode_Check == [] :
            print ("Null DB response",BNSCode_Check)
            return jsonify({'error' : 'Input Session not Found'}),400
        BNSCode = db.session.query(BNSSections.BNS_Section, BNSSections.BNS_Heading,BNSSections.IPC_Section).where(BNSSections.BNS_Section == friend_name_BNS)
        if BNSCode:
            result_list = [
                {
                    'BNS_Section': row.BNS_Section,
                    'BNS_Heading': row.BNS_Heading,
                    'IPC_Section': row.IPC_Section
                }
                for row in BNSCode
            ]
            return jsonify({'message': 'Data found!', 'data': result_list})

        
        # BNSCode_Check =  BNSSections.query.filter_by(BNS_Section=friend_name_BNS).all()
        # if BNSCode_Check == [] :
        #     print ("Null DB response",BNSCode_Check)
        #     return jsonify({'error' : 'Input Session not Found'}),400
        # if BNSCode_Check != [] : 
        #     print("Getting response ",BNSCode_Check)
        # BNSCode = db.session.query(BNSSections.BNS_Section, BNSSections.BNS_Heading,BNSSections.IPC_Section).where(BNSSections.BNS_Section == friend_name_BNS)
        # BNSCode2 = BNSSections.query.filter_by(BNS_Section = friend_name_BNS).all()
        # print (f'BNS Query : { BNSCode}')
        # print (f'BNS Query 2 : { BNSCode2}')
        # has_friends = len(BNSCode2)
        # print ("BNS Has_Friends : ", has_friends)
        # db.session.commit()
        # db.session.close()
        # return render_template("friends.html", title= title, friends = BNSCode, has_friends=2)
    # if friend_name_BNS == None :
    #     return render_template("friends.html", title= title, has_friends=0)

            # return redirect('/friends')

               
        # except:
            # return "There was an error while adding friend name"
        
       

@app.route("/form", methods=['GET','POST'])
def form():
    username = request.form.get("User_Name")
    password = request.form.get("Password")
    confirmPass = request.form.get("Confirm_Password")
    print("Request Method id : - ",request.method)
    # Captcha Handling
    if request.method == 'POST':
            user_captcha = request.form['captcha']
            if user_captcha == session['captcha']:
                flash('CAPTCHA passed, form submitted successfully!', 'success')
                # Process the form here
            else:
                flash('Incorrect CAPTCHA, please try again.', 'error')

        # Generate a new CAPTCHA every time the form is loaded
    captcha_text, captcha_image = generate_captcha()
    print ("Captcha Generator outPut : ", captcha_text, captcha_image)
    session['captcha'] = captcha_text

    if not username or not password or not confirmPass :
        error_statement = "Error : All Fields are required"
        has_error = error_statement
        return render_template("subscribe.html",
                            error_statement = error_statement, has_error = len(has_error),captcha_image=captcha_image)
    
    if confirmPass != password :
            error_statement = "Error : Confirmed password not matched "
            return render_template("subscribe.html",
                            error_statement = error_statement,captcha_image=captcha_image)
    if username != '' and password != '' and confirmPass != '':
        QueryCheckU = db.session.query(UserLogin.userName).where(UserLogin.userName == username, UserLogin.password == password).all()
        print ("QueryCheckU : ", QueryCheckU)
        if QueryCheckU != [] :
            error_statement = ' User already exists Pleae go back to login Page '
            return render_template("subscribe.html", error_statement = error_statement,captcha_image=captcha_image)
        else:
            user = UserLogin(userName=request.form.get("User_Name"), password=request.form.get("Password"))
            db.session.add(user)
            db.session.commit()
            db.session.close()
            subscriber.append(f"{username} ' is added '")
            title = "Thank you !!"
    
    
    print(username, password)
    return render_template("form.html", title = title, subscriber=subscriber,captcha_image=captcha_image)

@app.route('/captcha.png')
def captcha():
    # Serve the CAPTCHA image
    captcha_text, buffer = generate_captcha()
    session['captcha'] = captcha_text
    return send_file(buffer, mimetype='image/png')