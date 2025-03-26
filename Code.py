import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import community as community_louvain  # For Louvain clustering

def main():
    # Read the CSV file containing transaction records
    transactions = pd.read_csv('data/transactions.csv')

    # Build a directed graph from transaction data (each edge carries an 'Amount' attribute)
    graph = nx.from_pandas_edgelist(
        transactions, 
        source='Sender', 
        target='Receiver', 
        edge_attr='Amount', 
        create_using=nx.DiGraph()
    )

    # Calculate centrality metrics
    pr_scores = nx.pagerank(graph, alpha=0.85)
    degree_cent = nx.degree_centrality(graph)
    betweenness = nx.betweenness_centrality(graph)

    # Convert the directed graph to undirected for community detection
    undirected_graph = graph.to_undirected()
    communities = community_louvain.best_partition(undirected_graph)

    # Visualize the network using a circular layout
    plt.figure(figsize=(10, 8))
    pos = nx.circular_layout(graph)  # Alternative layout for a different look

    # Scale node sizes based on degree centrality (with a base size added)
    node_sizes = [degree_cent[node] * 3000 + 300 for node in graph.nodes()]
    node_colors = [communities[node] for node in graph.nodes()]
    
    nx.draw_networkx(
        graph, 
        pos, 
        with_labels=True, 
        node_size=node_sizes, 
        node_color=node_colors, 
        cmap=plt.cm.coolwarm, 
        edge_color='gray'
    )
    
    plt.title("Modified Transaction Network")
    plt.show()

    # Print the top 5 key entities by PageRank
    print("Top 5 Entities by PageRank:")
    for node, score in sorted(pr_scores.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"{node}: {score:.4f}")

    # Save processed data with PageRank scores (mapping Sender to its PageRank)
    transactions['PageRank'] = transactions['Sender'].map(pr_scores)
    transactions.to_csv('data/transactions_with_pagerank.csv', index=False)
    print("Processed data saved to 'data/transactions_with_pagerank.csv'.")
