from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)
app.config["SECRET_KEY"] = "askjhgdahsvq8722ty3gu23gh1og232^*!#&$!Hda123&^$$$$"

friends_dict = [
    {"name": "Test", "flavor": "swirl", "read": "yes", "activities": "reading"}
]
# Handling error 404 and displaying relevant web page
@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404

# Handling error 500 and displaying relevant web page
@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template(
        "index.html", pageTitle="Web form template", friends=friends_dict
    )

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/add", methods=["POST"])
def add():
    print("inside add function")
    if request.method == "POST":

        form = request.form

        tname = form["tname"]
        aname = form["aname"]
        pname = form["pname"]
        classification = form["read"]
        activities = form.getlist("activities")  # this is a PYthon list
        acquisition = form["Acquisition"]

        print(tname)
        print(aname)
        print(pname)
        print(classification)
        print(activities)
        print(acquisition)

        activities_string = ", ".join(activities)  # make the Python list into a string

        friend_dict = {
            "tname": tname,
            "aname": aname,
            "pname": pname,
            "classification": classification,
            "activities": activities_string,
            "acquisition": acquisition,
        }

        print(friend_dict)
        friends_dict.append(
            friend_dict
        )  # append this dictionary entry to the larger friends dictionary
        print(friends_dict)

        flash('Record successfully added.', 'success')
        
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))
    

if __name__ == "__main__":
    app.run(debug=True)
