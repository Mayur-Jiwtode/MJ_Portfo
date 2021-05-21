from flask import Flask,render_template,request,redirect
import csv 
app = Flask(__name__)

@app.route('/')
def py():
    return render_template("index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)



@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
	if request.method == "POST":
		data = request.form.to_dict()
		write_in_csv(data)
		return redirect("/Thank_you.html")
	else:
		return "somthing went wrong.Try again"

def write_in_file(data):
	with open("database.txt", mode = 'a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f"\nemail {email}, subject {subject},message {message}")
  
def write_in_csv(data):
	with open("database1.csv" ,'a',newline = "") as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer =csv.writer(database2, delimiter = "," , quotechar= '"',quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])


#@app.route('/index.html')
#def py0():
    #return render_template("index.html")

#@app.route('/about.html')
#def py1():
 #   return render_template("about.html")


#@app.route('/works.html')
#def py2():
   # return render_template("works.html")


#@app.route('/contact.html')
#def py3():
  #  return render_template("contact.html")

#@app.route('/components.html')
#def py4():
 #   return render_template("components.html")