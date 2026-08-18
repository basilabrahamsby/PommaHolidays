import urllib.request
import json

def test_login():
    url = "http://127.0.0.1:8000/api/auth/login"
    data = json.dumps({"email": "admin@pomma.com", "password": "PommaAdmin#123"}).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})

    try:
        with urllib.request.urlopen(req) as resp:
            print("Status Code:", resp.status)
            print("Response Body:", resp.read().decode('utf-8'))
    except Exception as e:
        if hasattr(e, 'read'):
            print("HTTP Error Body:", e.read().decode('utf-8'))
        else:
            print("Error:", e)

if __name__ == "__main__":
    test_login()
