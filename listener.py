from flask import Flask, request
import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables from the .env file
load_dotenv()

# Initialize the Supabase client with an admin user
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

app = Flask(__name__)

@app.route('/cal-com-webhook', methods=['POST'])
def handle_cal_com_webhook():
    """This function will be called whenever a webhook event is received from Cal.com. It will use the Supabase API to populate a table in Supabase."""
    # Extract relevant information from the webhook payload
    data = request.get_json()
    trigger_event = data["triggerEvent"]
    payload = data["payload"]

    # Use the Supabase API to insert the event data into a table
    response_str, count = supabase.table("events").insert({
        "event_type": payload["type"],
        "title": payload["title"],
        "organizer_name": payload["organizer"]["name"],
        "attendee_name": payload["attendees"][0]["name"],
        "start_time": payload["startTime"],
        "end_time": payload["endTime"]
    }).execute()

    if '"code":' in response_str:
        print(f"Error inserting event data: {response_str}")
    else:
        print(f"Inserted {count} event(s) into Supabase table.")

    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)