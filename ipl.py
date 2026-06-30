import pandas as pd
import numpy as np
import json

matches = pd.read_csv("data\IPL_Matches_2008_2022 (1).csv")

def teamsAPI():
    teams =  list(set(list(matches['Team1']) + list(matches['Team2'])))
    team_dict = {
        'teams': teams
    }
    return team_dict

def teamVteamAPI(team1, team2):
  temp_df = matches[(matches['Team1'] == team1) & (matches['Team2'] == team2) | (matches['Team1'] == team2) & (matches['Team2'] == team1)]
  total_matches = temp_df.shape[0]

  wins = temp_df['WinningTeam'].value_counts()

  matches_won_team1 = wins.get(team1, 0)
  matches_won_team2 = wins.get(team2, 0)

  draws = total_matches - (matches_won_team1 + matches_won_team2)

  response = {
      'total_matches': str(total_matches),
      team1: str(matches_won_team1),
      team2: str(matches_won_team2),
      'draws': str(draws)
  }
  return response

def teamRecordAPI(team):
  temp_df = matches[(matches['Team1'] == team) | (matches['Team2'] == team)]
  matches_played = temp_df.shape[0]

  won = temp_df[temp_df['WinningTeam'] == team].shape[0]

  no_result = temp_df[temp_df['WinningTeam'].isna()].shape[0]

  lost = matches_played - won - no_result

  if matches_played != 0:
    win_pct = round((won / matches_played)*100,2)
  else:
    win_pct = 0

  response = {
      "team": team,
      "matches_played": matches_played,
      "won": won,
      "lost": lost,
      "no_result": no_result,
      "win_percentage": win_pct

  }
  return response

def matchesAPI(team):
    
    temp_df = matches[(matches['Team1'] == team) | (matches['Team2'] == team)]
    
    response = []
    
    for _,row in temp_df.iterrows():
        
        response.append({
            "match_id": int(row['ID']),
            "match_number": row['MatchNumber'],
            "date": row['Date'],
            "season": row['Season'],
            "team1": row['Team1'],
            "team2": row['Team2'],
            "winner": row["WinningTeam"],
            "venue": row['Venue']
        })
        
    return response 

def matchDetailsAPI(id):
  try:
    row = matches[matches["ID"] == id].iloc[0]
  except IndexError:
    return {"error": "Match not found"}

  response = {
      "match_id": int(row['ID']),
      "city": row['City'],
      "date": row['Date'],
      "season": int(row['Season']),
      "match_number": row['MatchNumber'],
      "team1": row['Team1'],
      "team2": row['Team2'],
      "venue": row['Venue'],
      "toss_winner": row['TossWinner'],
      "toss_decision": row['TossDecision'],
      "super_over": row['SuperOver'],
      "winning_team": row['WinningTeam'],
      "won_by": row['WonBy'],
      "margin": int(row['Margin']) if pd.notna(row['Margin']) else None,
      "method": row['method'],
      "player_of_match": row['Player_of_Match'],
      "team_1_players": row['Team1Players'],
      "team_2_players": row['Team2Players'],
      "umpire1": row['Umpire1'],
      "umpire2": row['Umpire2']
  }
  return response

def seasonAPI():
    
    seasons = sorted(matches['Season'].unique())
    
    response = {
        "seasons": list(seasons)
    }
    
    return response

def pointsTable(season):

  temp_df = matches[matches["Season"] == season]

  teams = pd.unique(pd.concat([temp_df['Team1'], temp_df['Team2']]))

  response = []

  for team in teams:
    team_df = temp_df[(temp_df['Team1'] == team) | (temp_df['Team2'] == team)]
    matches_played = team_df.shape[0]
    won = team_df[team_df['WinningTeam'] == team].shape[0]
    draw = team_df[team_df['WinningTeam'].isna()].shape[0]
    lost = matches_played - won - draw
    points = (won*2) + draw
    win_pct = round((won/matches_played)*100,2) if matches_played else 0

    response.append({
        "team": team,
        "played": matches_played,
        "won": won,
        "no_result": draw,
        "lost": lost,
        "points": points,
        "win_percentage": win_pct
    })

  response.sort(key=lambda x:(x['points'],x['win_percentage']), reverse=True)
  return response