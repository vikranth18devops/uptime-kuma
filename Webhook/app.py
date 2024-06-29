from flask import Flask
from twilio.rest import Client

app = Flask(__name__)

@app.route('/trigger-call', methods=['GET', 'POST'])
def trigger_call():
    account_sid = 'AC2abfc9c9a1c60b9ac8d86f55594802fa'
    auth_token = '7088971bc5cc90115d86533bdb390a04'
    client = Client(account_sid, auth_token)

    # List of numbers to call
    numbers_to_call = ['+919052113411', '<number>']
    call_sids = []  # To store Call SIDs

    for number in numbers_to_call:
        call = client.calls.create(
                            twiml='<Response><Say>"change Alert message here"</Say></Response>',
                            to=number,
                            from_='+13203728367'
                        )
        call_sids.append(call.sid)

    # Joining all the Call SIDs to return in response
    call_sids_str = ', '.join(call_sids)
    return f"Call initiated with SIDs: {call_sids_str}", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
