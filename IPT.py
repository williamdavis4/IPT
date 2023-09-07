import requests
import socket
from colorama import Fore, Style
import time

api_key = "ENTER YOUR API KEY HERE"
ip_address = input("Enter the IP address: ")

url = f"http://api.ipapi.com/{ip_address}?access_key={api_key}"

response = requests.get(url)
data = response.json()

country_code = data["country_code"]
country_name = data["country_name"]
region_name = data["region_name"]
city = data["city"]
zip_code = data["zip"]

isp_url = f"http://ip-api.com/json/{ip_address}"
isp_response = requests.get(isp_url)
isp_data = isp_response.json()
isp_full_name = isp_data.get("isp", "N/A")

# Extract only the common name from the full ISP name
isp_common_name = isp_full_name.split(",")[0]

# Perform a reverse DNS lookup to get the hostname
try:
    hostname = socket.gethostbyaddr(ip_address)[0]
except socket.herror:
    hostname = "N/A"

def color_print(message, color=Fore.WHITE):
    print(f"{color}{message}{Style.RESET_ALL}")

color_print("[*** TRACE ENGAGED ***]", Fore.RED)
color_print("[... Initiating data retrieval ...]", Fore.YELLOW)
time.sleep(0.25)
color_print("[... IP LOCATION DATA OBTAINED ...]", Fore.YELLOW)
time.sleep(0.25)
color_print(f"> CC: {country_code}", Fore.RED)
color_print(f"> Country: {country_name}", Fore.RED)
color_print(f"> Region: {region_name}", Fore.RED)
color_print(f"> City: {city}", Fore.RED)
color_print(f"> ZIP Code: {zip_code}", Fore.RED)
color_print("[... IDENTIFYING INTERNET SERVICE PROVIDER ...]", Fore.YELLOW)
time.sleep(0.25)
color_print(f"> ISP: {isp_common_name}", Fore.RED)
color_print("[*** DATA EXTRACTION COMPLETE ***]", Fore.YELLOW)
color_print("[*** INITIATING HOSTNAME SEARCH ***]", Fore.YELLOW)
time.sleep(0.25)
color_print(f"> Hostname: {hostname}", Fore.RED)
color_print("[*** HOSTNAME IDENTIFIED ***]", Fore.YELLOW)
