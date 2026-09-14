
"""Automation tool.

Writes a timestamped log file from a list of entries and can optionally
fetch external data from a public API. Run directly from the command line:

    python generate_log.py
"""

from datetime import datetime


def generate_log(entries):
    # STEP 1: Validate input
    # The input must be a list
    if not isinstance(entries, list):
        raise ValueError("entries must be a list")

    # STEP 2: Generate a filename with today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write the log entries to a file
    with open(filename, "w") as file:
        for entry in entries:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message
    print(f"Log written to {filename}")

    return filename


def fetch_data():
    # Import requests here so the module can load even if
    # requests is not installed.
    import requests

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    if response.status_code == 200:
        return response.json()

    return {}


if __name__ == "__main__":
    # Sample log entries
    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]

    # Generate the log file
    generate_log(log_data)

    # Fetch sample data from the API
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))

