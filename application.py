from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route("/application-form")
def application_form():
    """Show the application form"""

    return render_template("application-form.html")

@app.route("/application-response", methods=['POST'])
def application_response():
    """Show the application form submission confirmation"""

    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    salary = request.form.get("salary")
    jobtype = request.form.get("jobtype")

    return render_template("application-response.html", firstname=firstname, lastname=lastname, salary=salary, jobtype=jobtype)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

