# Phase 6 — Project Testing

## Test Cases

| ID | Test | Expected Result |
|---|---|---|
| TC01 | Enter valid height and weight | BMI is calculated and displayed |
| TC02 | Change activity days | Prediction/recommendations update |
| TC03 | Enter low sleep value | Lifestyle/sleep tip can appear |
| TC04 | Enter low water value | Hydration tip can appear |
| TC05 | Enter a complete valid profile | Goal, confidence and plan are displayed |
| TC06 | Refresh the application | Application loads again without external API |
| TC07 | Open project with requirements installed | Streamlit app starts successfully |

## Manual Acceptance Criteria

- App starts with `streamlit run app.py`.
- No API key is required.
- User can change all profile inputs.
- BMI is visible.
- ML goal is visible.
- Recommendations are visible.
- 7-day plan is visible.
