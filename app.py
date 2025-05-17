import streamlit as st
import pandas as pd
import os
from recommend import filter_and_rank

# Page configuration
st.set_page_config(page_title='Restaurant Recommender', layout='wide')
st.title('Knowledge-Based Restaurant Recommender')

# Load cleaned data
data_path = os.path.join('data', 'zomato_clean.csv')
try:
    clean_df = pd.read_csv(data_path)
except FileNotFoundError:
    st.error('Cleaned data file not found. Please run data_processing.py first.')
    st.stop()

# Sidebar: Preferences
with st.sidebar:
    st.header('Preferences')
    city = st.selectbox('City', sorted(clean_df['City'].str.title().unique()))
    cuisine = st.selectbox(
        'Cuisine',
        sorted(clean_df[clean_df['City'].str.title() == city]['Cuisines'].str.title().unique())
    )
    budget = st.selectbox(
        'Budget',
        sorted(
            clean_df[
                (clean_df['City'].str.title() == city) &
                (clean_df['Cuisines'].str.title() == cuisine)
            ]['CostBucket'].str.title().unique()
        )
    )
    top_n = st.slider('Number of suggestions', 1, 10, 5)
    if st.button('Recommend'):
        st.session_state.results = filter_and_rank(
            cuisine.lower(), budget.lower(), city, top_n
        )

# Main panel: Display results if available
results = st.session_state.get('results')
if results is not None:
    if results.empty:
        st.warning('No matching restaurants found. Try adjusting your preferences.')
    else:
        st.subheader('Top Recommendations')
        for _, row in results.iterrows():
            st.markdown(f"**{row['Restaurant Name']}**")
            st.write(f"Cuisine: {row['Cuisines'].title()} | Cost: ₹{row['Average Cost for two']} | Rating: {row['Rating']}")
            st.write(row['Explanation'])
            st.map(pd.DataFrame({'lat': [row['Latitude']], 'lon': [row['Longitude']]}))

        # Feedback form (preserves displayed recommendations)
        st.markdown('---')
        st.subheader('Feedback Survey')
        with st.form('survey_form'):
            satisfaction = st.select_slider(
                'How satisfied are you with these recommendations?',
                ['Very Unsatisfied', 'Unsatisfied', 'Neutral', 'Satisfied', 'Very Satisfied']
            )
            relevance = st.radio(
                'Did you find the recommendations relevant?', ('Yes', 'No')
            )
            usability = st.select_slider(
                'How would you rate the usability of this app?',
                ['Very Difficult', 'Difficult', 'Neutral', 'Easy', 'Very Easy']
            )
            submitted = st.form_submit_button('Submit Feedback')
            if submitted:
                feedback_df = pd.DataFrame([{  
                    'City': city, 'Cuisine': cuisine,
                    'Budget': budget, 'Satisfaction': satisfaction,
                    'Relevance': relevance, 'Usability': usability
                }])
                feedback_path = os.path.join('data', 'feedback.csv')
                if os.path.exists(feedback_path):
                    feedback_df.to_csv(feedback_path, mode='a', header=False, index=False)
                else:
                    feedback_df.to_csv(feedback_path, index=False)
                st.success('Thank you for your feedback!')