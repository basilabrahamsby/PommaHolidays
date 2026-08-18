from app.database import SessionLocal
from app.models.Package import PackageBooking
from app.utils.billing import calculate_booking_bill

def check():
    db = SessionLocal()
    try:
        pb = db.query(PackageBooking).first()
        if pb:
            res = calculate_booking_bill(db, pb)
            print(f"Guest: {pb.guest_name}")
            print(f"Check-In: {pb.check_in} | Check-Out: {pb.check_out} | Status: {pb.status}")
            print(f"Calculated Stay Nights: {res['stay_nights']}")
            print(f"Total Charges Due: ₹{res['charges'].total_due:,.2f}")
            print(f"Total GST: ₹{res['charges'].total_gst:,.2f}")
            print(f"Grand Total: ₹{res['grand_total']:,.2f}")
    finally:
        db.close()

if __name__ == "__main__":
    check()
