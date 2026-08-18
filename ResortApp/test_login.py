import requests

def test_login():
    url = "http://127.0.0.1:8000/api/auth/login"
    payload = {"email": "admin@pomma.com", "password": "PommaAdmin#123"}
    r = requests.post(url, json=payload)
    print("Status Code:", r.status_code)
    print("Response Body:", r.text)

if __name__ == "__main__":
    test_login()
