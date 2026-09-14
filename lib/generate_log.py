"""Automation tool.

Writes a timestamped log file from a list of entries and can optionally
fetch external data from a public API. Run directly from the command line:

    python generate_log.py
"""

from datetime import datetime
import os

def generate_log(data):
    # TODO: Implement log generation logic

    # STEP 1: Validate input
    # Hint: Check if data is a list
def generate_log(entries):
    # the input must be a list; reject anything else (str, int, dict, None...)
    if not isinstance(entries, list):
        raise ValueError("entries must be a list")

    # build a timestamped filename in the pattern log_YYYYMMDD.txt
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # write each entry on its own line
    # an empty list writes nothing, leaving a valid empty file
    with open(filename, "w") as file:
        for entry in entries:
            file.write(f"{entry}\n")

    # confirm the file was written, including the filename
    print(f"Log written to {filename}")

    return filename


def fetch_data():
    # imported here so the module still loads even if requests isn't installed
    import requests

    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    # Hint: Use datetime.now().strftime("%Y%m%d")
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

    # STEP 3: Write the log entries to a file using File I/O
    # Use a with open() block and write each line from the data list
    # Example: file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename
if __name__ == "__main__":
    # sample run: write a log file, then fetch a sample post
    log_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(log_data)

    pass
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))

