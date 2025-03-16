from datetime import datetime

appointments = []

aptmnts = int(input("Enter number of appointments: "))

for i in range(aptmnts):
    date, time = "", ""

    # Date Validation
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("❌ Invalid date format. Please use YYYY-MM-DD.")

    # Time Validation
    while True:
        time = input("Enter time (24-hour format | HH:MM): ").strip()
        try:
            datetime.strptime(time, "%H:%M")
            break
        except ValueError:
            print("❌ Invalid time format. Please use HH:MM.")

    desc = input("Enter description: ").strip()

    # Check for duplicate appointment
    if any(appt["date"] == date and appt["time"] == time for appt in appointments):
        print("⚠️ Duplicate date and time! Please reschedule!")
    else:
        appointments.append({"date": date, "time": time, "desc": desc})
        print("✅ Appointment added!")

    print(appointments)

appointments.sort(key=lambda x: (x["date"], x["time"]))

print("Summary")
for appt in appointments:
    print("-", appt["date"], appt["time"], "-", appt["desc"])