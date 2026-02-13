import requests
import time
import sys

URL = "https://age-verifier.kibty.town/"
CHECK_INTERVAL = 30

def alert():
    sys.stdout.write('\a')
    print(f"UPDATED: Probably a working patch.")

def monitor():
    while True:
        try:
            response = requests.get(URL, timeout=10)
            content = response.text.lower()

            if "patched" not in content:
                alert()
                time.sleep(60) 
            elif "the age verifier is currently patched" in content:
                print(f"the age verifier is currently patched")
            
        except Exception:
            pass

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    try:
        monitor()
    except KeyboardInterrupt:
        print("\nStopped.")
