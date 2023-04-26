from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client
from flask import Flask, request

app = Flask(__name__)

# Replace with your Twilio account SID and auth token
account_sid = "AC9824ef38c2d867f0d8c1c3737a54dd9c"
auth_token = "46f5c99cbf8146d0ada0ee24dd28d23d"
client = Client(account_sid, auth_token)

@app.route("/ivr", methods=["POST"])
def ivr():
    response = VoiceResponse()

    # Create an initial greeting for the caller
    response.say("Welcome to My IVR system!", voice="alice")

    # Provide options for the caller to choose from
    response.gather(
        num_digits=1,  # Number of digits to gather
        timeout=5,  # Timeout for user input
        action="/handle-choice",  # Action URL to handle user input
        method="POST"  # HTTP method to use for the action URL
    )
    response.say("Press 1 for option one. Press 2 for option two.", voice="alice")

    return str(response)

@app.route("/handle-choice", methods=["POST"])
def handle_choice():
    digit_pressed = request.form["Digits"]

    if digit_pressed == "1":
        # Handle option one
        response = VoiceResponse()
        response.say("You chose option one.", voice="alice")
        # Add further instructions for option one
        return str(response)

    elif digit_pressed == "2":
        # Handle option two
        response = VoiceResponse()
        response.say("You chose option two.", voice="alice")
        # Add further instructions for option two
        return str(response)

    else:
        # Handle invalid input
        response = VoiceResponse()
        response.say("Invalid input. Please try again.", voice="alice")
        response.redirect("/ivr")  # Redirect to the main IVR menu
        return str(response)

if __name__ == "__main__":
    app.run(debug=True)