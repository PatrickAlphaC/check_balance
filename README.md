Python Script for monitoring ETH Balance 

# Required Environment variables:
`MAINNET_ETH_NODE_ADDRESS`: Your mainnet eth node address

`ETHERSCAN_API_KEY`: Your [Etherscan API Key](https://etherscan.io/myapikey)

## Optional Environment variables
If you want to send a text via Twilio when the balance is too low:
`TWILIO_ACCOUNT_SID`: Sign up for a [Twilio account](https://www.twilio.com/docs/iam/keys/api-key)

`TWILIO_AUTH_TOKEN`: Sign up for a [Twilio account](https://www.twilio.com/docs/iam/keys/api-key)

`CELL_PHONE`: An authorized cell number

`TWILIO_CELL`: A phone number from Twilio


# Useage

`python check_eth_balance.py`

# Output

```bash
INFO:root:Current balance for node 0x11111111111111111111E1E48122227a3328A1fc is 25.519349055101745
```
Or
```
INFO:root:Current balance for node 0x165Ff6730D449Af03B4eE1E48122227a3328A1fc is 25.5145926972985
ERROR:root:Balance of 25.5145926972985 is less than threshold of 100
```
