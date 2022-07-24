#Server Side
from pyexpat import model
from urllib import response
from flask import Flask
from flask_restful import Api,Resource,abort
from flask import Flask, request,jsonify,json
from flask_cors import CORS, cross_origin
from flask import send_file
import uuid
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api= Api(app)
CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}},CORS_SUPPORTS_CREDENTIALS = True)
app.config['CORS_HEADERS'] = 'Content-Type'
#model = load_model(os.path.join(os.getcwd(),"deep_keratitis.h5"))

# @app.route("/". methods = ["GET"])
# @cross_origin()
# def getHello():
#     return "Hello"

#request for image
@app.route('/get_image')
def get_image():
    if request.args.get('type') == '1':
       filename = 'ok.gif'
    else:
       filename = 'error.gif'
    return send_file(filename, mimetype='image/gif')

#send result back
@app.route("/upload", methods=["POST","GET"])
def uploadImage():
    response_object = {'status':'success'}
    if response.method == "POST":
        post_data = request.get_json()
        meResult = post_data.get('meResult'),
        file = post_data.get('file'),
        print(meResult)
        print(file)
        response_object['message'] = 'Image added!'
    return jsonify(response_object)


# api model
@app.route("/dkmodel", methods=['Post']) #post date mean send data, get some value back, GET is get data without sending any request
def DK_prediction(): #data will be send to this end point/DK_prediction
    content = request.json #get data that send to DK_prediction
    errors = []
    for name in content: # name = data in content
        if name in DK_model: #model = name of the data in model
          predict_DK = DK_model[name]['pathogen'] #from the name, want to get pathogen
          value = content[name]
     #if len(errors)<1:   
        prediction = model.predict(x) #x is the variable of the content data # will be define
        DK_patho = float(prediction[0])
        response = {"result": str(uuid.uuid4()), "DK_result" :DK_patho, "errors": errors } #if model work
    else: 
        response = {"result": str(uuid.uuid4()), "errors": errors } #if model doesnt work
    #response in 2 possibility
    return jsonify(response) #reponse in json file to send back to the person who send the request 

if __name__ == "__main__":
    app.run(debug=True, use_reloader =False )



          













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