#Server Side
from pyexpat import model
from urllib import response
from flask import Flask
from flask_restful import Api,Resource,abort
from flask import Flask, request,jsonify,json
from flask_cors import CORS, cross_origin
from flask import send_file
#from flask_mail import Mail, message
import smtplib
import os
import uuid
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#from grpc import server

# Model
# import 


from zmq import Message
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api= Api(app)
UPLOAD_FOLDER = "backend/img"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}},CORS_SUPPORTS_CREDENTIALS = True)
app.config['CORS_HEADERS'] = 'Content-Type'
#model = load_model(os.path.join(os.getcwd(),"deep_keratitis.h5"))

#Test function
@app.route("/test") # Define route of the function
def Hi():
    return "Test"

#Upload function
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    print("uploading...")
    if request.method == 'POST':
        # if 'dropzonefile' not in request.files:
        #     print ('there is no file from "dropzonefile"')
        #     return
        file1 = request.files["image"]
        path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        file1.save(path)
        print(path)
        # res = ModelFunction(path)
        # return res
        # return path # If model file finish plz uncomment this and delete both of the line above
        return ""

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        print("sending an email...")
        data = request.json


        #d = request.form.to_dict()
        # email = request.data.email
        # message = request.data.message
        print(data)
        name = data["name"]
        email = data["email"]
        message = data["message"]


        mail_content = message
        #The mail addresses and password
        sender_address = 'powerpufffy@gmail.com'
        sender_pass = 'cpjlcidxhdvxeysc'
        receiver_address = str(email)
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Response email to '+ str(name)   #The subject line
        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')

        res = {"message" : "success"}
        # print(res.data.message)
        print(res)
        return  jsonify(res)

# @app.route('/test', methods=['POST'])
# def contact():
#     # name = "gutjung"
#     # email = "chojaokun@gmail.com"
#     # message = "test"

#     reply_message = "Your contact have been sent"
#     server = smtplib.SMTP("smtp.gmai.com", 5000)
#     server.starttls()
#     server.login("powerpufffy@gmail.com", "pufffypowerhds2")
#     server.sendmail("powerpufffy@gmail.com", email, reply_message)
#     print ("email sent")
#Sending an email
# configuration of mail
# app.config['MAIL_SERVER']='sirakis.ng.gmail.com'
# app.config['MAIL_PORT'] = 5000
# #app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
# app.config['MAIL_PASSWORD'] = '*****'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# mail = Mail(app)

# @app.route('/contact', methods=['GET', 'POST'])
# def upload_file():
#     print("Email sending...")
#     if request.method == 'POST':
#         msg = Message("Hi", sender = "", recipients = ['aasdasda@gmail.com'])
#         msg.body = "njkzndfjhgdsjkhfghsdjkf"
#         mail.send(msg)
#         return

#     return 

# #send result back
# @app.route("/upload", methods=["POST","GET"])
# def uploadImage():
#     response_object = {'status':'success'}
#     if response.method == "POST":
#         post_data = request.get_json()
#         meResult = post_data.get('meResult'),
#         file = post_data.get('file'),
#         print(meResult)
#         print(file)
#         response_object['message'] = 'Image added!'
#     return jsonify(response_object)


# api model
# @app.route("/dkmodel", methods=['Post']) #post date mean send data, get some value back, GET is get data without sending any request
# def DK_prediction(): #data will be send to this end point/DK_prediction
#     content = request.json #get data that send to DK_prediction
#     errors = []
#     for name in content: # name = data in content
#         if name in DK_model: #model = name of the data in model
#           predict_DK = DK_model[name]['pathogen'] #from the name, want to get pathogen
#           value = content[name]
#      #if len(errors)<1:   
#         prediction = model.predict(x) #x is the variable of the content data # will be define
#         DK_patho = float(prediction[0])
#         response = {"result": str(uuid.uuid4()), "DK_result" :DK_patho, "errors": errors } #if model work
#     else: 
#         response = {"result": str(uuid.uuid4()), "errors": errors } #if model doesnt work
#     #response in 2 possibility
#     return jsonify(response) #reponse in json file to send back to the person who send the request 


# Main
if __name__ == "__main__":
    app.run()



          
# @app.route("/dkmodel", methods= ["GET"])
# def predDK():

#     if request.method == 'GET':

#         return (str(prediction[0]))


#vaidate request
#def notFoundDK(...check with exist data...)
    #if .... not in ....:
        #abort(404, message = "not found")
#design
#class Deep_keratitis(Resource):
    #def get(self):
        #notFoundDK(..name..)
        #return.....
   
    #def post(self):
        #return......

#call
#api.add_resource(....,"/")
#api.add_resource(Deep_keratits,"/.../<string>")