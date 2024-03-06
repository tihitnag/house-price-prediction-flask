from  flask  import Flask,jsonify,request
import utils

app=Flask(__name__)
@app.route('/get_location')
def get_location():
    response=jsonify({"location":utils.get_location()

    })
    response.headers.add('Across-control-Allow-Origin','*')
    return response
@app.route('/get_home_price',methods=['POST'])
def get_home_price():
    total_sqft = float(request.form['total_sqft'])

    location=request.form(['location'])
    bhk=int(request.form['bhk'])
    bath=int(request.form['bath'])
    response=jsonify({"estimated_price":utils.get_estemted_price(location,total_sqft,bhk,bath)

    })
    response.headers.add('Across-control-Allow-Origin','*')
    return response


if __name__=="__main__":
    print(' python sever')

    utils.load_artifacts()
    
    app.run()

# PRACTICE\server\Desktop\django\PRACTICE\server