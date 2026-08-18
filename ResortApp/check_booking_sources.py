from app.database import SessionLocal
from app.models.booking import Booking
from app.models.Package import PackageBooking

def check_sources():
    db = SessionLocal()
    try:
        print("=== REGULAR BOOKINGS ===")
        bks = db.query(Booking).all()
        for b in bks:
            print(f"ID: BK-{str(b.id).zfill(6)} | Guest: {b.guest_name} | Source: {b.source} | External ID: {b.external_id}")
            
        print("\n=== PACKAGE BOOKINGS ===")
        pbs = db.query(PackageBooking).all()
        for pb in pbs:
            print(f"ID: PK-{str(pb.id).zfill(6)} | Guest: {pb.guest_name} | Source: getattr({getattr(pb, 'source', None)})")
    finally:
        db.close()

if __name__ == "__main__":
    check_sources()
