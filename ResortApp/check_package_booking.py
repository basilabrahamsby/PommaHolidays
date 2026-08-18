from app.database import SessionLocal
from app.models.Package import PackageBooking, Package

def check_pb():
    db = SessionLocal()
    try:
        pbs = db.query(PackageBooking).all()
        print(f"Total Package Bookings: {len(pbs)}")
        for pb in pbs:
            for k, v in pb.__dict__.items():
                if not k.startswith('_'):
                    print(f"  {k}: {v}")
            print("-" * 40)
            
        print("\nAll Packages:")
        pkgs = db.query(Package).all()
        for p in pkgs:
            for k, v in p.__dict__.items():
                if not k.startswith('_'):
                    print(f"  {k}: {v}")
            print("-" * 40)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    check_pb()
