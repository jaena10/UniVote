from flask import Flask, render_template

app = Flask(__name__)

# =====================================================================
# Student Voting Portal (Home Route)
# =====================================================================
@app.route('/')
def student_portal():
    return render_template('studentweb.html')

# =====================================================================
# Admin Management Console Route
# =====================================================================
@app.route('/admin')
def admin_portal():
    return render_template('adminweb.html')

if __name__ == '__main__':
    print("==================================================")
    print("UniVote System - University of the Assumption")
    print("Student Portal: http://127.0.0.1:5000/")
    print("Admin Console:  http://127.0.0.1:5000/admin")
    print("==================================================")
    app.run(debug=True, port=5000)
