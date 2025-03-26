# AML Transaction Network Analysis

This project performs network analysis on transaction data to uncover suspicious activities, key entities, and community structures. By leveraging graph-based methodologies, the project provides insights into financial transaction patterns that may indicate money laundering or other fraudulent activities.

## Project Overview

The project ingests transaction data from a CSV file, builds a network graph, computes centrality metrics, detects communities, and visualizes the network. The analysis helps in identifying:
- **Key Entities:** Using centrality measures like PageRank.
- **Community Structures:** Using community detection methods to spot clusters of related transactions.
- **Transaction Patterns:** Visualizing the relationships between senders and receivers.

## Features

- **Data Loading:** Efficiently reads transaction data from a CSV file.
- **Graph Construction:** Builds a directed network graph using transaction records.
- **Centrality Metrics:** Computes key metrics such as PageRank and degree centrality.
- **Community Detection:** Applies the Louvain method to detect communities within the network.
- **Visualization:** Generates a network visualization using various layout techniques.
- **Data Export:** Saves processed data with computed metrics for further analysis.
