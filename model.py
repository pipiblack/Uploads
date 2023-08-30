import requests
import time

# Define the voting website's URL.
voting_url = "https://www.example.com/vote"

# Define the username and password for the voting account.
username = "username"
password = "password"

# Define the candidate ID of the candidate you want to vote for.
candidate_id = 1

# Start a loop that will vote for the candidate repeatedly.
while True:
    # Make a request to the voting website.
    response = requests.post(voting_url, auth=(username, password))

    # Check the response status code.
    if response.status_code == 200:
        # If the response status code is 200, then the vote was successful.
        print("Voted successfully!")
    else:
        # If the response status code is not 200, then something went wrong.
        print("Error voting:", response.status_code)

    # Sleep for a few seconds before making the next request.
    time.sleep(5)

    break