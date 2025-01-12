import json
import re

input_file = "raw_comments.json"  
output_file = "user_wallets.json"


with open(input_file, "r", encoding="utf-8") as file:
    data = file.read()

# Use regular expressions to extract all proxyWallet values
proxy_wallets = re.findall(r'"proxyWallet":\s*"(0x[a-fA-F0-9]{40})"', data)


with open(output_file, "w", encoding="utf-8") as file:
    json.dump(proxy_wallets, file, indent=4)

print(f"Extraction completed. Found {len(proxy_wallets)} proxyWallet(s). Results saved to {output_file}.")
