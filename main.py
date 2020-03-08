from flask import Flask, request, render_template, url_for, redirect, send_file, Response, Markup, abort, jsonify
app = Flask(__name__,static_folder='static')


virusDatabase=[]

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/dashboard")
def dashboard():
	return render_template("dashboard.html")

@app.route("/addVirus",methods=['POST'])
def addVirus():
	virusName=request.form["virusName"]
	virusDatabase.append({"virusName":virusName,stat:"processing",percentComplete:0})
	return redirect(url_for("treatements"))





@app.route("/treatments")
def treatements():
	return render_template("treatments.html")
@app.route("/treatmentDetail")
def treatementDetail():
	treatementID = request.args.get('ID')
	return render_template("treatmentDetail.html",mmdbid=treatementID)



app.run(host="0.0.0.0",port=80,threaded=True,debug=True)
