### introduction of Users' Betting Data on Polymarket

After extracting users' `proxy_wallets` from Polymarket, we can leverage these wallets to analyze the following aspects:
- Users' betting events
- Betting targets
- Betting amounts

Below are the key fields associated with users' bets:

---

### **Field Descriptions**

| **Field**            | **Description**                                                                                     |
|-----------------------|-----------------------------------------------------------------------------------------------------|
| `wallet`             | The user's wallet address.                                                                          |
| `size`               | The number of yes/no binary tokens purchased for the Polymarket event.                              |
| `avgPrice`           | The price of yes/no tokens for the event (in cents, ¢).                                             |
| `initialValue`       | The token price of the event at the time of purchase.                                               |
| `currentValue`       | The value of tokens held by the user at the time of settlement.                                     |
| `title`              | The name of the Polymarket event.                                                                   |
| `cashPnl`            | Profit or loss in monetary terms.                                                                   |
| `percentPnl`         | Profit or loss as a percentage.                                                                     |
| `bettingPosition`    | The betting direction (yes/no) chosen by the user for the event.                                    |

---


