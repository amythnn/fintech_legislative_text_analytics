#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 19:07:37 2026

@author: an
"""


"""
Data & Attribution: Legislative metadata is retrieved through the LegiScan API and remains
 subject to LegiScan's applicable terms of service, 
licensing requirements, and usage restrictions.
"""

import requests
import json

legiscan_key = "YOUR_API_KEY"
    """Get your API key by registering first."""

# ------------

STATE = "CA" # Can be updated to search for other states


def get_current_session(state):
    """Get the current legislative session for a state."""

    # Build the LegiScan API URL for session data
    url = (
        f"https://api.legiscan.com/"
        f"?key={legiscan_key}&op=getSessionList&state={state}"
    )

    # Call the API
    response = requests.get(url)

    # Check whether the API call worked
    if response.status_code != 200:
        print("Failed to retrieve sessions.")
        return None

    # Convert the JSON response into a Python dictionary
    data = response.json()

    # Stop if the response does not contain session data
    if "sessions" not in data:
        print("No session data found.")
        print(json.dumps(data, indent=2)[:1000])
        return None

    # Find sessions that are not marked as prior
    current_sessions = [
        session
        for session in data["sessions"]
        if session["prior"] == 0
    ]

    # Stop if no current session is found
    if not current_sessions:
        print("No active session found.")
        return None

    # Use the first current session
    session = current_sessions[0]

    # Print session info so we can confirm it is correct
    print("Current session found:")
    print(f"State: {session['state_abbr']}")
    print(f"Session: {session['name']}")
    print(f"Session ID: {session['session_id']}")

    # Return the session ID
    return session["session_id"]


def get_latest_bills(session_id):
    """Fetch bills from a LegiScan session."""

    # Build the LegiScan API URL for the master bill list
    url = (
        f"https://api.legiscan.com/"
        f"?key={legiscan_key}&op=getMasterList&id={session_id}"
    )

    # Print the URL so we can confirm the request looks right
    print(f"Calling API: {url}")

    # Send the request to LegiScan
    response = requests.get(url)

    # Print the HTTP status code
    print(f"HTTP Status: {response.status_code}")

    # Stop if the request failed
    if response.status_code != 200:
        print("Request failed.")
        return []

    # Convert the API response from JSON into a Python dictionary
    data = response.json()

    # Print the top-level keys to confirm the response structure
    print("Top-level keys:")
    print(data.keys())

    # Print a short preview of the JSON response for debugging
    print("Response preview:")
    print(json.dumps(data, indent=2)[:1000])

    # Stop if the expected masterlist data is missing
    if "masterlist" not in data:
        print("No masterlist found.")
        return []

    # Convert the masterlist dictionary into a list of bills
    # The first item is metadata, so we skip it with [1:]
    bills = list(data["masterlist"].values())[1:]

    # Return the list of bills
    return bills


def find_fintech_bills(bills):
    """Find bills related to BNPL, fintech, and consumer lending."""

    # Define keywords that may signal BNPL, fintech, or consumer credit bills
    keywords = [
        "buy now pay later",
        "bnpl",
        "installment",
        "consumer credit",
        "consumer loan",
        "deferred payment",
        "earned wage access",
        "wage access",
        "fintech"
    ]

    # Create an empty list to store matched bills
    matches = []

    # Loop through each bill
    for bill in bills:

        # Get the bill title
        title = bill.get("title", "")

        # Convert the title to lowercase for easier matching
        title_lower = title.lower()

        # Loop through each keyword
        for keyword in keywords:

            # Check whether the keyword appears in the bill title
            if keyword in title_lower:

                # Add the bill and the matched keyword to the results
                matches.append({
                    "bill": bill,
                    "matched_keyword": keyword
                })

                # Print which keyword triggered the match
                print(f"Matched keyword: {keyword}")
                print(f"Matched title: {title}")
                print("-" * 60)

                # Stop checking other keywords after the first match
                break

    # Return the matched bills
    return matches


def main():
    """Run the full script."""

    # Get the current session ID for the selected state
    session_id = get_current_session(STATE)

    # Stop if no session ID was found
    if session_id is None:
        print("No session ID found.")
        return

    # Print which state and session we are using
    print(f"Fetching bills for {STATE} Session {session_id}")

    # Get all bills from the selected session
    bills = get_latest_bills(session_id)

    # Stop if no bills were returned
    if not bills:
        print("No bills found.")
        return

    # Print the total number of bills retrieved
    print(f"Retrieved {len(bills)} bills")

    # Print the first 10 bills as a quick sanity check
    print("First 10 bills:")

    # Loop through the first 10 bills
    for bill in bills[:10]:

        # Get the bill number
        bill_number = bill.get("number", "N/A")

        # Get the bill title
        bill_title = bill.get("title", "N/A")

        # Get the last action date
        last_action = bill.get("last_action_date", "N/A")

        # Print the bill details
        print("-" * 60)
        print(f"Bill Number: {bill_number}")
        print(f"Title: {bill_title}")
        print(f"Last Action Date: {last_action}")
        print(
            f"URL: https://legiscan.com/{STATE}/bill/{bill_number}/{session_id}"
        )

    # Search for BNPL, fintech, and consumer credit bills
    fintech_bills = find_fintech_bills(bills)

    # Print the number of matched bills
    print("Potential BNPL / FinTech Bills")
    print(f"Found {len(fintech_bills)} matches")

    # Loop through the matched bills
    for match in fintech_bills:

        # Get the bill from the match dictionary
        bill = match["bill"]

        # Get the keyword that triggered the match
        matched_keyword = match["matched_keyword"]

        # Get the bill number
        bill_number = bill.get("number", "N/A")

        # Get the bill title
        bill_title = bill.get("title", "N/A")

        # Get the last action date
        last_action = bill.get("last_action_date", "N/A")

        # Print the matched bill details
        print("-" * 60)
        print(f"Matched Keyword: {matched_keyword}")
        print(f"Bill Number: {bill_number}")
        print(f"Title: {bill_title}")
        print(f"Last Action Date: {last_action}")
        print(
            f"URL: https://legiscan.com/{STATE}/bill/{bill_number}/{session_id}"
        )


if __name__ == "__main__":
    main()