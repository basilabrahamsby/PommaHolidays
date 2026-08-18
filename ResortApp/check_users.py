from app.database import SessionLocal
from app.models.user import User

def check_users():
    db = SessionLocal()
    try:
        users = db.query(User).all()
        print(f"Total users in DB: {len(users)}")
        for u in users:
            role_name = u.role.name if u.role else "No Role"
            print(f"ID: {u.id} | Email: {u.email} | Name: {u.name} | Role: {role_name} | Active: {u.is_active}")
    except Exception as e:
        print(f"Error querying users: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    check_users()
