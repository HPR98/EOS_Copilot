from flask import Flask, render_template, request, jsonify
from util import initial_showfile_data, channels_in_use
########################################################################
##########################Flask Server##################################

# Create a Flask web application
app = Flask(__name__)

def run_flask():
    app.run()

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

#################################################################################
##########################Initial Showfile Data##################################

#POST in patch count
@app.route('/update_channel_count', methods=["POST"])
def update_patch_count():
    data = request.get_json()
    initial_showfile_data["patch_count"] = data["patch_count"]
    print(initial_showfile_data["patch_count"])
    return jsonify("Successfully received Data")

#POST in preset count
@app.route('/update_preset_count', methods=["POST"])
def update_preset_count():
    data = request.get_json()
    initial_showfile_data["preset_count"] = data["preset_count"]
    print(initial_showfile_data["preset_count"])
    return jsonify("Successfully received Data")

#POST in cp count
@app.route('/update_cp_count', methods=["POST"])
def update_cp_count():
    data = request.get_json()
    initial_showfile_data["cp_count"] = data["cp_count"]
    print(initial_showfile_data["cp_count"])
    return jsonify("Successfully received Data")

#POST in group count
@app.route('/update_group_count', methods=["POST"])
def update_group_count():
    data = request.get_json()
    initial_showfile_data["group_count"] = data["group_count"]
    print(initial_showfile_data["group_count"])
    return jsonify("Successfully received Data")

#################################################################################
##########################Get Channels in use ###################################
@app.route("/update_channels_in_use", methods=["POST"])
def update_channels_in_use():
    data = request.get_json()
    channels_in_use = data["channels_in_use"]
    print(channels_in_use)
    return jsonify("Successfully received Data")

#################################################################################
##########################Frontend communication#################################

#Get initial showfile data
@app.route("/get_initial_showfile_data", methods=["GET"])
def get_showfile_data():
    data_from_server = initial_showfile_data
    return jsonify(data_from_server)

#Get Channels in use
@app.route("/get_channels_in_use", methods=["GET"])
def get_channels_in_use():
    data_from_server = channels_in_use
    return jsonify(data_from_server)

if __name__ == "__main__":
    app.run(debug=True)

