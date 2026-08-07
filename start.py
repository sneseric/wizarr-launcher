import subprocess
import time
import webbrowser
import requests

URL = "http://localhost:5690"


def main():
    print("Launching Wizarr container via Docker Compose...")
    # Execute docker compose up -d in background
    subprocess.run(["docker", "compose", "up", "-d"], check=True)

    print(f"Waiting for Wizarr web server at {URL} to become ready...")
    # Poll until server returns HTTP 200 or 302
    while True:
        try:
            res = requests.get(URL, timeout=2)
            if res.status_code in [200, 302]:
                print("Wizarr is online!")
                break
        except requests.RequestException:
            pass
        time.sleep(1)

    print(f"Opening {URL} in your default browser...")
    webbrowser.open(URL)


if __name__ == "__main__":
    main()