import pandas as pd

def filter_and_rank(cuisine, budget, city, top_n=5):
    # Load cleaned data
    df = pd.read_csv('data/zomato_clean.csv')

    # Build filter mask (case-insensitive, substring match for city)
    mask = (
        df['Cuisines'].str.contains(cuisine.lower(), na=False) &
        (df['CostBucket'] == budget) &
        df['City'].str.lower().str.contains(city.lower(), na=False)
    )
    sub = df[mask].copy()

    # If no matches, return empty DataFrame
    if sub.empty:
        return sub

    # Compute composite score: 70% rating, 30% normalized votes
    sub['Score'] = sub['Rating'] * 0.7 + (sub['Votes'] / sub['Votes'].max()) * 0.3

    # Select top N
    sub = sub.sort_values('Score', ascending=False).head(top_n)

    # Generate explanations
    sub['Explanation'] = sub.apply(
        lambda r: f"Matched on {r['Cuisines']} cuisine, {r['CostBucket']} budget, and '{r['City']}' location with rating {r['Rating']}",
        axis=1
    )

    # Return core info including coordinates for mapping
    return sub[['Restaurant Name', 'Cuisines', 'Average Cost for two', 'Rating', 'Latitude', 'Longitude', 'Explanation']]

# Test stub
if __name__ == '__main__':
    print(filter_and_rank('indian', 'medium', 'New', top_n=3))