from app.database import SessionLocal
from app.models.user import User
from passlib.context import CryptContext

def set_password():
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.email == "admin@pomma.com").first()
        if user:
            user.hashed_password = pwd_context.hash("PommaAdmin#123")
            db.commit()
            print("SUCCESS: Admin password updated to PommaAdmin#123")
        else:
            print("ERROR: admin@pomma.com not found")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    set_password()
