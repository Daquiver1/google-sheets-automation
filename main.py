"""Main file."""
from emails import send_single_email
from sheets import add_otp_to_sheet, read_emails

print("Extracting emails from google sheet...")
list_of_emails = read_emails()
print(list_of_emails)
print("Done extracting emails.")

print("Sending bulk email...")
# student_code = send_email_via_send_in_blue(list_of_emails)
# student_code = send_bulk_email(list_of_emails)
student_code = send_single_email("temp@gmail.com")
print("Done sending bulk email.")

print("Adding student Code to google sheet...")
add_otp_to_sheet(student_code)
print("Done adding student code to otp sheet.")

print("Update complete. Terminating program...")
