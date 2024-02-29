import streamlit as st
import pandas as pd


def UpdateTable():
    st.write("updating table")

def GenTeams():
    """

team1,team2 = st.columns(2)

players = {"andrew": 1, "sam": 2, "micheal": 3}



st.selectbox("Players for tonight",tuple(players.keys()))

team1.write("Team 1")
team2.write("Team 2")

players = {}

team1_count = {1,4,7,9,10}

count = 1
for player in players:
    if count in team1_count:
        team1.write(player["name"])
    else:
        team2.write(player["name"])
    count += 1
"""


    st.write("gen teams")

st.title("Monday Fives")
"""

flow = st.radio("What do you want to do?", ["Update table", "Generate teams"])
state = 1
if st.button("Next"):
    if flow == "Update table":
        state = 1
    else:
        state = 0
if state == 0:
    """
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Display the uploaded file as a DataFrame
if uploaded_file is not None:
# Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

# Display the DataFrame
    st.write("### Uploaded CSV file as DataFrame")
    st.write(df)
    st.write("ERRRR")




