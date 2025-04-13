import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from collections import defaultdict

def fetch_cricket_news(url):
    """
    Fetch cricket news from the given URL.

    Args:
        url (str): The URL of the cricket news website.

    Returns:
        list: A list of news headlines related to cricket.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract headlines (modify the tag and class based on the website's structure)
        headlines = []
        for item in soup.find_all('h2', class_='headline'):  # Example: Replace 'h2' and 'headline' with actual tags
            headlines.append(item.text.strip())

        return headlines

    except Exception as e:
        print(f"Error fetching cricket news: {e}")
        return []

def analyze_team_performance(headlines):
    """
    Analyze team performance based on cricket news headlines.

    Args:
        headlines (list): A list of cricket news headlines.

    Returns:
        dict: A dictionary with team names as keys and their performance scores as values.
    """
    teams = ['India', 'Australia', 'England', 'Pakistan', 'South Africa', 'New Zealand', 'Sri Lanka', 'West Indies']
    performance = defaultdict(int)

    for headline in headlines:
        for team in teams:
            if team in headline:
                performance[team] += 1

    return performance

def plot_team_performance(performance):
    """
    Plot the performance of teams based on the analysis.

    Args:
        performance (dict): A dictionary with team names as keys and their performance scores as values.
    """
    teams = list(performance.keys())
    scores = list(performance.values())

    plt.figure(figsize=(10, 6))
    plt.bar(teams, scores, color='skyblue')
    plt.xlabel('Teams')
    plt.ylabel('Performance Score')
    plt.title('Cricket Team Performance Based on News Headlines')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # URL of the cricket news website (replace with an actual URL)
    url = "https://cricinfo.com"  # Replace with a real cricket news website

    # Fetch cricket news
    headlines = fetch_cricket_news(url)
    print("Fetched Headlines:")
    for headline in headlines:
        print(f"- {headline}")

    # Analyze team performance
    performance = analyze_team_performance(headlines)
    print("\nTeam Performance:")
    for team, score in performance.items():
        print(f"{team}: {score}")

    # Plot team performance
    plot_team_performance(performance)