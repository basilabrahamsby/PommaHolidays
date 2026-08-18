from app.database import SessionLocal
from sqlalchemy import text

def add_columns():
    db = SessionLocal()
    try:
        print("Adding missing columns to PostgreSQL DB...")
        db.execute(text("ALTER TABLE bookings ADD COLUMN IF NOT EXISTS advance_amount FLOAT DEFAULT 0.0;"))
        db.execute(text("ALTER TABLE package_bookings ADD COLUMN IF NOT EXISTS advance_amount FLOAT DEFAULT 0.0;"))
        db.commit()
        print("SUCCESS: Added advance_amount column to bookings and package_bookings tables!")
    except Exception as e:
        db.rollback()
        print(f"Error adding columns: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    add_columns()
