from flask import Flask, render_template, request
import datetime

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main_page():  # put application's code here
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year
    return render_template('index.html', month=current_month, year=current_year)


@app.route('/ew', methods=['POST'])
def elec_water():
    return render_template('elect_water.html')

@app.route('/lo', methods=['POST'])
def land_ownership():
    return render_template('land_ownership.html')

@app.route('/ac', methods=['POST'])
def aadhar_card():
    return render_template('aadhar_card.html')

@app.route('/edu', methods=['POST'])
def education():
    return render_template('education.html')

@app.route('/tickets', methods=['POST'])
def tickets():
    return render_template('tickets.html')

@app.route('/oas', methods=['POST'])
def old_age_services():
    return render_template('old_age_services.html')

@app.route('/hs', methods=['POST'])
def health_services():
    return render_template('health_services.html')

@app.route('/ds', methods=['POST'])
def dom_services():
    return render_template('dom_services.html')

@app.route('/vi', methods=['POST'])
def veh_ins():
    return render_template('veh_ins.html')






if __name__ == '__main__':
    app.run(debug=True)
