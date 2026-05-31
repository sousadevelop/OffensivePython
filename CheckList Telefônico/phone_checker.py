import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

# Use somente numeros ficticios ou autorizados.
phone = input(
    "Informe somente um numero ficticio ou autorizado no formato "
    "internacional: ex.: +5500000000000\n-> "
)

phone_number = phonenumbers.parse(phone)

state = geocoder.description_for_number(phone_number, "pt")
time_zone = timezone.time_zones_for_number(phone_number)
phone_carrier = carrier.name_for_number(phone_number, "pt")
region = geocoder.description_for_number(phone_number, "pt")
valid = phonenumbers.is_valid_number(phone_number)
possible = phonenumbers.is_possible_number(phone_number)

print(f"\nEstado ou regiao: {state}.")
print(f"Fuso horario: {time_zone}.")
print(f"Operadora telefonica: {phone_carrier}.")
print(f"Regiao geografica: {region}.")
print(f"Numero valido: {valid}.")
print(f"Numero possivel: {possible}.")
