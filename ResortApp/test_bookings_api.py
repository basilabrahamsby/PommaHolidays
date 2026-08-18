import urllib.request
import json

def test_api():
    url = "http://127.0.0.1:8000/api/packages/bookingsall"
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print("Items count:", len(data.get('items', [])))
            for item in data.get('items', []):
                print(f"ID: {item.get('id')} | Guest: {item.get('guest_name')} | Check-In: {item.get('check_in')} | Check-Out: {item.get('check_out')} | Total Amount: {item.get('total_amount')}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    test_api()
