from flask import Flask, render_template, request
import requests
import smtplib

MY_EMAIL = "pythoncoursea@gmail.com"
PASSWORD = "zftadfdvngefnegr"

app = Flask(__name__)

blog_api = requests.get(url="https://api.npoint.io/201d12b842fb5ca38c03").json()


@app.route('/')
def home():
    return render_template("index.html", posts=blog_api)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/posts/<int:post_id>')
def posts(post_id):
    return render_template("post.html", posts=blog_api, id=post_id)

@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", request_type=request.method)
    else:
        data = request.form
        user_details = f"Name: {data['name']}\n" \
                       f"Email: {data['email']}\n" \
                       f"Phone number: {data['phone']}\n" \
                       f"Message: {data['message']}\n"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="omrip500@gmail.com",
                                msg=f"Subject: User Deatils\n\n{user_details}")

        return render_template("contact.html", request_type=request.method)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9865, debug=True)
