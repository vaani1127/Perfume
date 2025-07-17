import streamlit as st

# Title
st.title("🌸 What's Your Perfect Perfume Match?")

# Quiz Questions (based on images)
questions = {
    "1➜ What's your ideal vibe for a night out?": [
        "Elegant and Romantic",
        "Calm and Grounded",
        "Warm and Cozy",
        "Fun and Energetic"
    ],
    "2➜ Choose a season you love the most?": [
        "Spring",
        "Autumn",
        "Summer",  # corrected from "Sumemr"
        "Winter"
    ],
    "3➜ Which scent note appeals to you the most?": [
        "Jasmine or Rose",
        "Sandalwood or Cedar",
        "Vanilla or Caramel",
        "Lemon or Orange"
    ],
    "4➜ Pick a word that best describes your personality:": [
        "Graceful",
        "Grounded",
        "Warm",
        "Lively"
    ],
    "5➜ If you could be anywhere right now, where would you be?": [
        "A blossoming garden",
        "Cozy cabin in the woods",
        "Comfy fire side lounge",
        "Tropical beach"
    ]
}

# Collect user answers
user_answers = []

# Render questions dynamically
for q, options in questions.items():
    answer = st.radio(q, options, key=q)
    user_answers.append(answer)

# Result logic based on majority selected letter (A, B, C, D)
def calculate_result(answers):
    # Index mapping (0=A, 1=B, etc.)
    choice_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    for i, answer in enumerate(answers):
        if answer in questions[list(questions.keys())[i]]:
            index = questions[list(questions.keys())[i]].index(answer)
            key = list('ABCD')[index]
            choice_counts[key] += 1

    top_choice = max(choice_counts, key=choice_counts.get)

    scent_map = {
        'A': "🌌 Your scent is **Celestial Veil**",
        'B': "🌿 Your scent is **Amber Drift**",
        'C': "🌑 Your scent is **Noir Mirage**",
        'D': "🍦 Your scent is **Velvet Vanilla**"
    }

    return scent_map.get(top_choice, "🔍 Still exploring your perfect match!")

# Show result
if st.button("Reveal My Perfume Match"):
    result = calculate_result(user_answers)
    st.markdown(f"### 💫 Quiz Result:\n{result}")
    st.markdown("[🔗 Visit our Instagram](https://www.instagram.com/perfectumes.in)")
