from flask import Flask, render_template, request
import joblib

app = Flask(__name__)



# routes
@app.route("/", methods=['GET', 'POST'])
def kuch_bhi():
	return render_template("home.html")

@app.route("/about")
def about_page():
	return "About You..!!!"




# with open("model.pkl", "rb") as f:
#     model = pickle.load(f)


model = joblib.load("model.pkl")




@app.route("/submit", methods = ['GET', 'POST'])
def get_hours():
	if request.method == 'POST':
		x1 = float(request.form['youtube'])
		x2 = float(request.form['facebook'])
		x2 = float(request.form['newspaper'])

		sales = model.predict([[x1,x2,x3]])
		
	return render_template("home.html", marks = sales[0])





if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)
