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
- `Raw Data`: .json
- `Preprocessed Data`: .json
