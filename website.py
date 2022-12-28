import streamlit as st
import pandas as pd

matches = pd.read_csv('D:\\temp\\My_Work\\Player Stats Analysis\\IPL-Player-Stats-Analysis\\IPL_Data.csv')
balls = pd.read_csv('D:\\temp\\My_Work\\Player Stats Analysis\\IPL-Player-Stats-Analysis\\IPL_Ball_by_Ball.csv')

st.sidebar.title('IPL Stats')

option = st.sidebar.selectbox('select one',['All Teams','Team Record','Team Vs Team Record','Batsman Record','Bowler Record'])

if option == 'All Teams':
    st.title('All Teams')

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