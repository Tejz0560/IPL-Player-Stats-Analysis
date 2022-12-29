import streamlit as st
import pandas as pd
import requests

matches = pd.read_csv('D:\\temp\\My_Work\\Player Stats Analysis\\IPL-Player-Stats-Analysis\\IPL_Data_cleaned.csv')
balls = pd.read_csv('D:\\temp\\My_Work\\Player Stats Analysis\\IPL-Player-Stats-Analysis\\IPL_Ball_by_Ball_cleaned.csv')


st.set_page_config(layout="wide")

st.sidebar.title('IPL Stats')

option = st.sidebar.selectbox('select one',['All Teams','Team Record','Team Vs Team Record','Batsman Record','Bowler Record'])

if option == 'All Teams':
    st.title('All Teams')
    response = requests.get('http://127.0.0.1:5000/api/allteams')
    teams = response.json()['teams']
    teams.remove('Rising Pune Supergiantss')
    cols = st.columns(5)
    for i in range(len(teams)):
        cols[i%5].image(f'Images\\IPL teams\\{teams[i]}.jpg')
        cols[i%5].subheader(teams[i])
    # st.image('https://www.iplt20.com/teams/chennai-super-kings') 
    

elif option == 'Team Record':
    st.title('Team Record')
    st.sidebar.selectbox('Select Team',sorted(matches['Team1'].unique().tolist()))

elif option == 'Team Vs Team Record':
    st.title('Team Vs Team Records')
    st.sidebar.selectbox('Team1',sorted(matches['Team1'].unique().tolist()))
    st.sidebar.selectbox('Team2',sorted(matches['Team1'].unique().tolist()))

elif option == 'Batsman Record':
    st.title('Batsman Record')
    st.sidebar.selectbox('Select Batsman',sorted(balls['batter'].unique().tolist()))

else:
    st.title('Bowler Record')
    st.sidebar.selectbox('Select Bowler',sorted(balls['bowler'].unique().tolist()))