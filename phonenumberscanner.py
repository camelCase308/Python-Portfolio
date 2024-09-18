import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier


number = input("Enter phone number with country code: ")

phoneNumber = phonenumbers.parse(number)

print(f"You entered {number} of digits which is incorrect.")

timeZone = timezone.time_zones_for_number(phoneNumber)
print(f"timezone: {timeZone}")

geolocation = geocoder.description_for_number(phoneNumber,"en")
print(f"location: {geolocation}")

service = carrier.name_for_number(phoneNumber,"en")
print(f"service provider: {service}")