# Research for 2024 President Election Based on polygon transactions and Polymarket data

----

# Research Idea Summary             

This research aims to explore the behaviors of participants in social event betting, particularly during a major election, by analyzing user profiles, emotional fluctuations, and betting patterns, and comparing them with traditional polling methods. Additionally, the study examines the potential of using a Large Language Model (LLM) to simulate and model social event betting.

User Profiling: One key question is whether the top bettors are "Loyal supporter"or "speculators." By applying machine learning techniques such as classification methods, the research will categorize users based on betting frequency, wager amounts, and historical patterns. The study will also investigate whether bettors who stake real money are more rational than those who use virtual currency, offering insights into decision-making processes in betting markets.

Emotion Analysis and Time Series: Sentiment analysis will be applied to Polymarket comments and different polls, with time series analysis used to track emotional fluctuations throughout the election. This will help determine if emotional changes correlate with investment behaviors, providing insight into whether sentiment in betting markets mirrors or diverges from public opinion polls.

LLM Simulation: The research will also explore the use of an LLM API to simulate user behavior based on comments and user data related to betting. By leveraging the ElectionSim-like platform(Large Language Model-driven simulation tool for massive population election simulations)the study aims to model how users might behave under varying conditions, simulating betting strategies and emotional responses to election events.

This multi-faceted approach provides a comprehensive understanding of the dynamics in social event betting and the potential for using AI models to simulate and predict future trends.


## Table of Contents
1. [Research Questions](#1-research-questions)
2. [Research Methods](#2-research-methods)
3. [Gaps and Research Goals](#3-gaps-and-research-goals)
4. [Project Structure](#4-project-structure)


# 1. Research Questions

- **RQ1**: How did individuals' emotions fluctuate throughout the election, and how are these fluctuations correlated with polling data? (Time Series Analysis)
- **RQ2**: What are the user profiles of participants in this event?
- **RQ3**: Can social event betting be effectively simulated and modeled using a Large Language Model (LLM)? (LLM Simulation)

# 2. Research Methods

- Analyze bettors' comments on Polymarket at various time intervals, alongside their betting behavior on the event.
- Simulate user behavior based on social media and Polymarket comments using an LLM API.
- Analyze transactions related to Polygon (for context on event betting).

# 3. Gaps and Research Goals    

 
Based on an analysis of traditional polling methods for the 2024 U.S. presidential election, we found significant biases in predictions derived from conventional online and offline surveys and telephone interviews. These biases often stem from factors such as respondents' political affiliations and the prevailing sociopolitical atmosphere in their regions, which can result in discrepancies between the polling outcomes and actual voting behavior. This gap highlights the limitations of traditional polling approaches in capturing the true sentiments of the electorate.

To date, major polling institutions have not introduced effective methods to eliminate subjective biases in data collection. However, through our observation of Polymarket, one of the most popular binary options cryptocurrency platforms, and its event dedicated to the 2024 presidential election `https://polymarket.com/event/presidential-election-winner-2024`, we identified its potential to address this gap. On this platform, users make financial investments to back their predictions—whether they are loyal supporters of a particular candidate or market-driven speculators, their monetary commitments are inherently more rational and reflective of true sentiment than verbal declarations.

To scientifically bridge the gap in traditional polling and enhance research in the field of social behavior, we conducted a deeper analysis of Polygon transactions and Polymarket data related to this event.

# 4.Project Structure
## Code Directory
The crawler for the polymarket event is organized under the Crawler/ directory:

- `event_spider.py`:The crawler for polymarket comments to get `raw_comments.json`.
 
## Data Processing Directory
- `get_bettings.py`:Access the Polymarket profiles of all users who commented `user_wallets.json` on the "presidential-election-winner-2024" event to review their betting activity for this event `wallet_betting.json`. 
- `remove_duplicates.py`:Remove duplicates to access `cleaned_wallet_betting.json`  .    
## Data Directory        
- `Raw Comments`: `raw_comments.json`        
- `Preprocessed Data`:  `wallet_betting.json` `cleaned_wallet_betting.json` 
- `wallets`:`user_wallets.json`  
- `Polling data`:  
`270towin/ JSON`  :`Data from pollsters in each state`   
 `realclearpolitics`  :`All incidents reported from 7.27-11.10`

  
  ____
- ### introduction of Users' Betting Data on Polymarket


After extracting users' `proxy_wallets` from `raw_comments.json`, we can leverage these Polymarket wallets to analyze the following aspects:


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
