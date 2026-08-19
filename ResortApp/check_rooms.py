from app.database import SessionLocal
from app.models.room import Room

def check_rooms():
    db = SessionLocal()
    try:
        rooms = db.query(Room).all()
        print(f"Total Rooms Count: {len(rooms)}")
        for r in rooms:
            print(f"ID: {r.id} | Number: {r.number} | Type: {r.type} | Channel Manager ID: {r.channel_manager_id}")
    finally:
        db.close()

if __name__ == "__main__":
    check_rooms()
