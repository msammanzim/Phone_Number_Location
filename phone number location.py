import phonenumbers
from phonenumbers import timezone,geocoder,carrier

number=input("Enter Your Phone Number: ")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
sim_detect=carrier.name_for_number(phone,"en")
register=geocoder.description_for_number(phone,"en")

print(number)
print(phone)
print(time)
print(sim_detect)
print(register)