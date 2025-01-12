# Research Idea Summary

This research aims to explore the behaviors of participants in social event betting, particularly during a major election, by analyzing user profiles, emotional fluctuations, and betting patterns, and comparing them with traditional polling methods. Additionally, the study examines the potential of using a Large Language Model (LLM) to simulate and model social event betting.

User Profiling: One key question is whether the top bettors are "Loyal supporter"or "speculators." By applying machine learning techniques such as classification methods, the research will categorize users based on betting frequency, wager amounts, and historical patterns. The study will also investigate whether bettors who stake real money are more rational than those who use virtual currency, offering insights into decision-making processes in betting markets.

Emotion Analysis and Time Series: Sentiment analysis will be applied to Polymarket comments and different polls, with time series analysis used to track emotional fluctuations throughout the election. This will help determine if emotional changes correlate with investment behaviors, providing insight into whether sentiment in betting markets mirrors or diverges from public opinion polls.

LLM Simulation: The research will also explore the use of an LLM API to simulate user behavior based on comments and user data related to betting. By leveraging the ElectionSim-like platform(Large Language Model-driven simulation tool for massive population election simulations)the study aims to model how users might behave under varying conditions, simulating betting strategies and emotional responses to election events.

This multi-faceted approach provides a comprehensive understanding of the dynamics in social event betting and the potential for using AI models to simulate and predict future trends.


# 1. Research Questions

- **RQ1**: How did individuals' emotions fluctuate throughout the election, and how are these fluctuations correlated with polling data? (Time Series Analysis)
- **RQ2**: What are the user profiles of participants in this event?
- **RQ3**: Can social event betting be effectively simulated and modeled using a Large Language Model (LLM)? (LLM Simulation)

# 2. Research Methods

- Analyze bettors' comments on Polymarket at various time intervals, alongside their betting behavior on the event.
- Simulate user behavior based on social media and Polymarket comments using an LLM API.
- Analyze transactions related to Polygon (for context on event betting).


# Project Structure
## Code Directory
The main scripts and relevant files are organized under the Code/ directory:

- `spider.py`:The crawler for polymarket comments.
main.py:
- `pre.py`: Preprocesses datasets for training.

## Data Directory      
- `Crwaler`:
- `Raw Data`: raw_comments.json
- `Preprocessed Data`:     
  ____
- ### introduction of Users' Betting Data on Polymarket


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
