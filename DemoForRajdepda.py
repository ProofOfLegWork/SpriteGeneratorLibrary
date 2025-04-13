import pandas as pd
import matplotlib.pyplot as plt

# Mock dataset (replace this with real data from a CSV or API)
data = {
    "Age Group": ["18-29", "30-39", "40-49", "50-59", "60+"],
    "Heart Disease Cases": [500, 1200, 3000, 4500, 7000],
    "Total Population": [10000, 15000, 20000, 25000, 30000],
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Calculate the percentage of heart disease cases in each age group
df["Percentage"] = (df["Heart Disease Cases"] / df["Total Population"]) * 100

# Function to plot a pie chart
def plot_pie_chart(data, labels, title):
    """
    Plot a pie chart.

    Args:
        data (list): The data values for the pie chart.
        labels (list): The labels for each slice of the pie chart.
        title (str): The title of the pie chart.
    """
    plt.figure(figsize=(8, 8))
    plt.pie(data, labels=labels, autopct="%1.1f%%", startangle=140, colors=plt.cm.Paired.colors)
    plt.title(title)
    plt.axis("equal")  # Equal aspect ratio ensures the pie chart is circular.
    plt.show()

# Plot pie chart for heart disease cases by age group
plot_pie_chart(
    data=df["Heart Disease Cases"],
    labels=df["Age Group"],
    title="Heart Disease Cases by Age Group"
)

# Plot pie chart for percentage of heart disease cases by age group
plot_pie_chart(
    data=df["Percentage"],
    labels=df["Age Group"],
    title="Percentage of Heart Disease Cases by Age Group"
)