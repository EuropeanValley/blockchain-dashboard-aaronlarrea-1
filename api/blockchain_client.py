import requests

url = "https://blockstream.info/api/blocks/tip/hash"
tip = requests.get(url).text.strip()

url = "https://blockstream.info/api/block/" + tip
response = requests.get(url)
data = response.json()

print(f"Height:       {data['height']}")
print(f"Hash:         {data['id']}")
print(f"Difficulty:   {data['difficulty']}")
print(f"Nonce:        {data['nonce']}")
print(f"Transactions: {data['tx_count']}")

# The block hash must be lower than a target value defined by the difficulty established by the network. Valid hashes start with a certain number of zeros.
# The bigger the amount of zeros, the smaller the hash target. This leads to a higher difficulty, requiring more computational power to find a valid hash.
# The difficulty is adjusted every 2016 blocks to keep the average block time close to 600 seconds (10 minutes)
