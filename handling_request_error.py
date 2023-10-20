import requests
import logging

logging.basicConfig(filename="example.log", format="%(asctime)s %(message)s", encoding="utf-8", level=logging.WARNING)

#http error
r = requests.get("https://httpbin.org/status/420")

try:
    r.raise_for_status()
except requests.exceptions.HTTPError:
    print("ERROR")

print(r)



#connection error

try:
    r = requests.get("https://dffshrg/status/500")
    r.raise_for_status()
# except requests.exceptions.ConnectionError:
#     print("No connection")

except requests.exceptions.RequestException as e:
    logging.warning(e)
print(r)