from app.database import SessionLocal
from app.models.Package import PackageBooking, Package

def check_pb():
    db = SessionLocal()
    try:
        pbs = db.query(PackageBooking).all()
        print(f"Total Package Bookings: {len(pbs)}")
        for pb in pbs:
            print(f"PackageBooking Details:")
            for k, v in pb.__dict__.items():
                if not k.startswith('_'):
                    print(f"  {k}: {v}")
            print("=" * 50)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    check_pb()
