### Uncomment to send a text
# from twilio.rest import Client
import os
import requests
import logging as log

log.basicConfig(level=log.INFO)

### the following line needs your Twilio Account SID and Auth Token
### Uncomment to use
# client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number

ETH_THRESHOLD = 100
ETHERSCAN_API_SUFFIX = "&tag=latest&"

BASE_ETHERSCAN_API = (
    os.getenv("BASE_ETHERSCAN_API")
    or "https://api.etherscan.io/api?module=account&action=balance&address="
)
ETH_NODE_ADDRESS = os.getenv("MAINNET_ETH_NODE_ADDRESS")

try:
    headers = {"Set-Cookie": "check-script"}
    url = (
        BASE_ETHERSCAN_API
        + ETH_NODE_ADDRESS
        + ETHERSCAN_API_SUFFIX
        + "apikey="
        + os.getenv("ETHERSCAN_API_KEY")
    )
    response = requests.get(url).json()

    current_balance = float(response["result"]) / 1000000000000000000

    log.info(
        "Current balance for node {} is {}".format(ETH_NODE_ADDRESS, current_balance)
    )
    if ETH_THRESHOLD > current_balance:
        log.error(
            "Balance of {} is less than threshold of {}".format(
                current_balance, ETH_THRESHOLD
            )
        )
        ### Uncomment for twilio use
        # client.messages.create(
        #     to=os.getenv("CELL_PHONE"),
        #     from_=os.getenv("TWILIO_CELL"),
        #     body=str(current_balance)
        #     + " ETH is your current balance for address "
        #     + ETH_NODE_ADDRESS
        #     + " please add ETH asap",
        # )
except Exception as err:
    log.error(err)
#     client.messages.create(
#         to=os.getenv("CELL_PHONE"),
#         from_=os.getenv("TWILIO_CELL"),
#         body=str(current_balance)
#         + " ETH is your current balance for address "
#         + ETH_NODE_ADDRESS
#         + " please add ETH asap",
#     )
