# Evaluation Report: Knowledge-Based Restaurant Recommender System

## 1. Objective
To evaluate the usability, effectiveness, and user satisfaction of the knowledge-based restaurant recommender system built using Streamlit and the Zomato dataset.

---

## 2. Evaluation Methods

### 2.1 Qualitative Evaluation
After receiving recommendations, users were prompted to complete a short survey embedded in the application. The survey included:

- **Satisfaction Rating**: Likert scale from "Very Unsatisfied" to "Very Satisfied"
- **Relevance Feedback**: Yes/No on whether the recommendations matched user preferences
- **Usability Feedback**: Likert scale from "Very Difficult" to "Very Easy"

### 2.2 A/B Testing (Planned)
Although not yet implemented, the system can support A/B testing by:
- Varying the scoring formula (e.g., weight of rating vs. votes)
- Testing default `top_n` values (e.g., 3 vs. 5 vs. 10)
- Using exact vs. partial matches on cities or cuisines

---

## 3. Collected Metrics (as of current iteration)

From the responses stored in `data/feedback.csv`, we tracked:

| Metric              | Summary                                           |
|---------------------|---------------------------------------------------|
| Satisfaction Score  | Majority responses between *Satisfied* and *Very Satisfied* |
| Relevance           | 80%+ users reported recommendations were relevant |
| Usability Feedback  | Mostly rated as *Easy* or *Very Easy*            |

---

## 4. User Feedback Summary

- 🔍 **Users appreciated** the clear UI and fast response.
- ⚠️ **Issues reported**:
  - Recommendations disappearing after interacting with survey buttons.
  - Filtered cities/cuisines not always behaving as expected.
- 💡 **Suggestions**:
  - Allow sorting/filtering by distance or rating.
  - Add more cuisine options per city.

---

## 5. Proposed Improvements

- ✅ Fix state handling so that recommendations persist after feedback.
- 🔄 Add ability to reset/clear previous recommendations.
- 📍 Consider integrating geolocation or distance filtering.
- 📊 Use separate logs for A/B testing results in future evaluations.

---

## 6. Conclusion

The initial version of the restaurant recommender performs well in relevance and usability. Continued feedback collection and controlled testing will guide iterative improvements to filtering logic, user interaction, and recommendation explanations.
