from flask import Flask, render_template, request, jsonify
from functools import wraps
import os

app = Flask(__name__)

API_KEY = "JZapi-Key"


#------------------function for securing api with api key-----------------#

def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = request.headers.get("X-API-KEY")

        if not api_key or api_key != API_KEY:
            return jsonify({"error": "Unauthorized"}), 401

        return f(*args, **kwargs)
    return decorated

#-------------------------------------------------------------#








Aeroplan_First = [{"seat" : [1, "JAHANZABE KHAN", "Book"]} ,
                      {"seat" : [2, "", "Available"]},
                      {"seat" : [3, "", "Available"]},
                      {"seat" : [4, "", "Available"]},
                      {"seat" : [5, "", "Available"]}]




@app.route('/API/A1', methods=['GET'])
def API_A1():


                  return jsonify(Aeroplan_First)
                  #return "<h1>API Page</h1>"




@app.route('/API/A1/add', methods=['GET', 'POST'])      #, methods=['GET', 'POST'])
def API_A1_single():

                  adds = {"seat" : request.json["seat"]}
                  #adds =  {"seat" : request.json[ent_SeatNumber,  ent_CustmrName, "Booked"]}
                  Aeroplan_First.append(adds)
                  return jsonify({ Aeroplan_First})




@app.route('/API/A1/del', methods=['GET', 'DELETE'])
def API_AI_Del():
                  del_data = {"seat" : request.json["seat"]}
                  #aas = Aeroplan_First.remove(Aeroplan_First[0])   # --wORKING
                  ADS = Aeroplan_First.remove(del_data)
                  return jsonify({ ADS})


@app.route('/API/A1/update/<int:ids>', methods=['GET', 'PUT'])  # These line best work     add after----/ this route  /<int:ids>
def API_AI_Update(ids):

                  #int_num = int(mun)
                  update_data={"seat" : request.json["seat"]}  #These three Line perfectly working
                  values = Aeroplan_First[ids] = update_data
                  return jsonify({values})

##############################################################################################################################
####-----------------------Here below this same Api try to secure---Start Here-----------------------------------------#######


@app.route('/sAPI/A1', methods=['GET'])
@require_api_key
def SAPI_A1():


                  return jsonify(Aeroplan_First)
                  #return "<h1>API Page</h1>"




@app.route('/sAPI/A1/add', methods=['GET', 'POST'])      #, methods=['GET', 'POST'])
@require_api_key
def SAPI_A1_single():

                  adds = {"seat" : request.json["seat"]}
                  #adds =  {"seat" : request.json[ent_SeatNumber,  ent_CustmrName, "Booked"]}
                  Aeroplan_First.append(adds)
                  return jsonify({ Aeroplan_First})




@app.route('/sAPI/A1/del', methods=['GET', 'DELETE'])
@require_api_key
def SAPI_AI_Del():
                  del_data = {"seat" : request.json["seat"]}
                  #aas = Aeroplan_First.remove(Aeroplan_First[0])   # --wORKING
                  ADS = Aeroplan_First.remove(del_data)
                  return jsonify({ ADS})


@app.route('/sAPI/A1/update/<int:ids>', methods=['GET', 'PUT'])  
@require_api_key
def SAPI_AI_Update(ids):

                  #int_num = int(mun)
                  update_data={"seat" : request.json["seat"]}  #These three Line perfectly working
                  values = Aeroplan_First[ids] = update_data
                  return jsonify({values})

####-----------------------Here below this same Api try to secure---END Here-------------------------------------------#######
##############################################################################################################################




if __name__ == '__main__':
           app.run()

'''
#app.run()
#print("ok")


'''
