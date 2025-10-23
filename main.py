from flask import Flask, request, render_template_string, redirect, url_for, flash,get_flashed_messages


app = Flask(__name__)
app.secret_key = "replace-this-with-a-secure-random-value"  # set a secure value in Render env vars in production

FORM_HTML = """
<!doctype html>
<title>Voter Registration</title>
<h1>United States Registration Office</h1>
<p>Welcome to the Python Voter Registration Application.</p>
<form method="post" action="{{ url_for('register') }}">
  <label>First name:<br><input name="fname" required></label><br><br>
  <label>Last name:<br><input name="lname" required></label><br><br>
  <label>Age:<br><input name="age" required></label><br><br>
  <label>Are you a U.S. Citizen?<br>
    <select name="citizen" required>
      <option value="">-- choose --</option>
      <option value="yes">Yes</option>
      <option value="no">No</option>
    </select>
  </label><br><br>
  <label>State (2-letter code):<br><input name="state" maxlength="2" required></label><br><br>
  <label>Zipcode:<br><input name="zipcode" required></label><br><br>
  <button type="submit">Register</button>
</form>

{% with messages = get_flashed_messages() %}
  {% if messages %}
    <ul style="color:red;">
      {% for m in messages %}<li>{{m}}</li>{% endfor %}
    </ul>
  {% endif %}
{% endwith %}
"""

RESULT_HTML = """
<!doctype html>
<title>Registration Result</title>
<h1>Thanks for registering to vote</h1>
<p>Here is the information we received:</p>
<ul>
  <li><strong>Name:</strong> {{ fname }} {{ lname }}</li>
  <li><strong>Age:</strong> {{ age }}</li>
  <li><strong>U.S. Citizen:</strong> {{ citizen }}</li>
  <li><strong>State:</strong> {{ state }}</li>
  <li><strong>Zipcode:</strong> {{ zipcode }}</li>
</ul>
<p>Your voter registration card should be shipped within 15 business days.</p>
<p><em>YOUR VOTE IS YOUR VOICE!</em></p>
<p><a href="{{ url_for('index') }}">Return to form</a></p>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(FORM_HTML)

def valid_age(value):
    try:
        a = int(value)
    except (TypeError, ValueError):
        return False, "Age must be an integer."
    if not (25 < a < 120):
        return False, "Age should be >25 and <120."
    return True, a

def valid_state(value):
    if not value or len(value.strip()) != 2 or not value.isalpha():
        return False
    return True

@app.route("/register", methods=["POST"])
def register():
    fname = request.form.get("fname", "").strip()
    lname = request.form.get("lname", "").strip()
    age_raw = request.form.get("age", "").strip()
    citizen = request.form.get("citizen", "").strip().lower()
    state = request.form.get("state", "").strip().upper()
    zipcode = request.form.get("zipcode", "").strip()

    # basic validations
    if not fname:
        flash("First name is required.")
    if not lname:
        flash("Last name is required.")
    ok_age, age_or_msg = valid_age(age_raw)
    if not ok_age:
        flash(age_or_msg)
    if citizen not in ("yes", "no"):
        flash("Citizen must be yes or no.")
    if not valid_state(state):
        flash("State must be two alphabetic letters (e.g., NY).")
    if not zipcode:
        flash("Zipcode is required.")

    if len(get_flashed_messages()) > 0:
        # there were validation errors
        return redirect(url_for("index"))

    # All good — render a result page
    return render_template_string(RESULT_HTML,
                                  fname=fname,
                                  lname=lname,
                                  age=age_or_msg,
                                  citizen=citizen,
                                  state=state,
                                  zipcode=zipcode)

# allow direct local running for dev/testing
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5015, debug=True)
