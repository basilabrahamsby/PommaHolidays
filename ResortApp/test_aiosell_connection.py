import asyncio
import httpx
from app.database import SessionLocal
from app.utils.aiosell_sync import sync_inventory, sync_rates
from app.core.aiosell_config import (
    AIOSELL_ACTIVE,
    AIOSELL_HOTEL_CODE,
    AIOSELL_PARTNER_ID,
    AIOSELL_USERNAME,
    AIOSELL_PASSWORD,
    get_inventory_url,
    get_rates_url
)

async def test_aiosell():
    print("=== AIOSELL CONNECTION DIAGNOSTIC ===")
    print(f"AIOSELL_ACTIVE: {AIOSELL_ACTIVE}")
    print(f"AIOSELL_HOTEL_CODE: {AIOSELL_HOTEL_CODE}")
    print(f"AIOSELL_PARTNER_ID: {AIOSELL_PARTNER_ID}")
    print(f"AIOSELL_USERNAME: {AIOSELL_USERNAME}")
    print(f"Inventory URL: {get_inventory_url()}")
    print(f"Rates URL: {get_rates_url()}")
    
    # 1. Test pinging live Aiosell endpoint directly
    print("\n--- 1. Testing Direct HTTP Handshake to Aiosell API ---")
    headers = {"Content-Type": "application/json"}
    auth = (AIOSELL_USERNAME, AIOSELL_PASSWORD) if AIOSELL_USERNAME and AIOSELL_PASSWORD else None
    
    dummy_payload = {
        "hotel_code": AIOSELL_HOTEL_CODE,
        "partner_id": AIOSELL_PARTNER_ID,
        "inventory": []
    }
    
    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            resp = await client.post(get_inventory_url(), json=dummy_payload, auth=auth, headers=headers)
            print(f"Direct Response Status Code: {resp.status_code}")
            print(f"Response Body: {resp.text}")
    except Exception as e:
        print(f"Direct Connection Error: {e}")

    # 2. Test full system sync execution
    print("\n--- 2. Executing System Inventory Sync ---")
    db = SessionLocal()
    try:
        res = await sync_inventory(db)
        print(f"Inventory Sync Result: {res}")
    except Exception as e:
        print(f"Inventory Sync Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    asyncio.run(test_aiosell())
