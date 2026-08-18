from app.database import SessionLocal
from app.models.package import PackageBooking, Package
from app.models.room import Room

def check_pb():
    db = SessionLocal()
    try:
        pbs = db.query(PackageBooking).all()
        print(f"Total Package Bookings: {len(pbs)}")
        for pb in pbs:
            pkg = db.query(Package).filter(Package.id == pb.package_id).first() if pb.package_id else None
            pkg_name = pkg.title if pkg else "Unknown Package"
            pkg_price = pkg.price if pkg else None
            print(f"ID: {pb.id} | Booking No: {pb.booking_number} | Guest: {pb.guest_name} | Package: {pkg_name} (ID: {pb.package_id}, Price: {pkg_price}) | Room ID: {pb.room_id} | Amount Paid: {pb.amount_paid} | Total Amount: {getattr(pb, 'total_amount', 'N/A')}")
            
        print("\nAll Packages:")
        pkgs = db.query(Package).all()
        for p in pkgs:
            print(f"Package ID: {p.id} | Title: {p.title} | Price: {p.price}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    check_pb()
