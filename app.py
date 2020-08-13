
from flask import Flask,render_template,request
import pickle
from sklearn.ensemble import GradientBoostingRegressor


app = Flask(__name__)
#model = pickle.load(open('model.pkl','rb'))
lr = pickle.load(open('lr.pkl','rb'))

@app.route("/")
def hello():
    return render_template('index.html')



@app.route("/predict",methods=["POST"])
def predict():
    
    """
    iput = [x for x in request.form.values()]
    X_test = [np.array(iput)]
    """
    
    area_type = int(request.form.get('area_type'))
    total_sqft = float(request.form.get('total_sqft'))
    bath = float(request.form.get('bath'))
    bhk = int(request.form.get('bhk'))
    price_per_sqft = float(request.form.get('price_per_sqft'))
    X_test = [[area_type,total_sqft,bath,bhk,price_per_sqft]]


    
    #gbr_pred = model.predict(X_test)
    lr_pred = lr.predict(X_test)

    #gbr_op = round(gbr_pred[0], 2)
    lr_op = round(lr_pred[0], 2)

    return render_template('index.html',out_put="Price in linear model will be Rs. {}".format(lr_op))



if __name__=="__main__":
    app.run(debug=True)