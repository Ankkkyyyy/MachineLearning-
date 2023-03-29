
# EDA,Data analysis sbh part ka Logic yaha likhenge !
import pandas as pd
import numpy as np

ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQG9rp1Zzv4WcMBI1M9tAE_qJWKz2MCfH8UPTni2WMTjJqC7ew1gHnDjoBPHsuV9eF-9ECOZRR3lPFA/pub?gid=1361615103&single=true&output=csv"
ball_by_ball = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQRLWYXE_vdPnPKe7LplgYx5qLt0rb1T1oh0zZqbaapMfYrCqbnl8Nd2OnlHnO_46VJUNvwQv4E8fwe/pub?gid=1894391710&single=true&output=csv')
batsman_run = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRwgITbG6BjnxnNvxkj8YKJem6EIJjaejYK4KHMRbI5eHaYDVDP5RSv5OLd0rN1wWRrTE4EqYuUqb3a/pub?gid=655438454&single=true&output=csv')
deliveries = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQEJnmI-E6FluLo5khJ8JNuO9gYS0d3gZ0F1mY7zNca3ozajy26OTKAsoHjvyVdyI1CJHKGdrVidtrI/pub?gid=586204712&single=true&output=csv')
matches = pd.read_csv(ipl_matches)

print(matches.head())

def teamsAPI():
    teams = list(set(list(matches['Team1']) + list(matches['Team2'])))
    team_dict = {
        'teams':teams,
    }
    return team_dict

def teamVteamAPI(team1,team2):
    valid_teams = list(set(list(matches['Team1']) + list(matches['Team2'])))
    if team1 in valid_teams and team2 in valid_teams:
       tempdf=matches[(matches['Team1']==team1) & (matches['Team2']==team2) | (matches['Team1']==team2) &(matches['Team2']==team1)]
       total_matches=tempdf.shape[0]
       matcheswon_team1=tempdf['WinningTeam'].value_counts()[team1]
       matcheswon_team2=tempdf['WinningTeam'].value_counts()[team2]
       draws = total_matches-(matcheswon_team1+matcheswon_team2)

       response = {
         'total_matches':str(total_matches),
         team1:str(matcheswon_team1),
         team2:str(matcheswon_team2),
         'draw':str(draws)
        }
       return response
    else:
        return{"Message":'Invalid Team Name...'}


def teamRecord(team):
    valid_teams = list(set(list(matches['Team1']) + list(matches['Team2'])))
    if team in valid_teams:
       df = matches[(matches['Team1'] == team) | (matches['Team2'] == team)]
       matches_played = df.shape[0]
       matches_w = df['WinningTeam'] == team
       matches_won = matches_w.sum()
       nr = df[df.WinningTeam.isnull()].shape[0]
       loss = matches_played - (matches_won + nr)
       title = df[(df.MatchNumber == 'Final') & (df.WinningTeam == team)].shape[0]
       # TEAMS = list(set(list(matches['Team1']) + list(matches['Team2'])))
       # against = {team2: teamVteamAPI(team, team2) for team2 in TEAMS}
       response = {

        'total matches played':str(matches_played),
        'total matches won':str(matches_won),
        'No result':str(nr),
        'Total matches Lost':str(loss),
        'Title Won ': str(title),

       }
       return str(response)
    else:
        return{"Message":'Invalid Team Name...'}


def batsmanrecord(batter):
    valid_batter_name = set(list(ball_by_ball['batter']))
    if batter in valid_batter_name:
        balldf = ball_by_ball.copy()
        batsman = balldf[(balldf['batter'] == batter)]
        batsman_total_runs = batsman['batsman_run'].sum()
        batsman_total_ball_faced = batsman[~(batsman['extra_type'] == 'wides')].shape[0]
        batsman_strike_rate = batsman_total_runs / batsman_total_ball_faced * 100
        fours = batsman[batsman['batsman_run'] == 4].shape[0]
        six = batsman[batsman['batsman_run'] == 6].shape[0]
        innings = batsman['ID'].unique().shape[0]
        gb = batsman.groupby('ID').sum()
        fifties = gb[(gb['batsman_run'] >= 50) & (gb['batsman_run'] < 100)].shape[0]
        hundred = gb[gb['batsman_run'] >= 100].shape[0]
        highestscore = gb['batsman_run'].sort_values(ascending=False).head(1).values[0]
        outs = batsman[batsman['player_out'] == batter].shape[0]
        average = batsman_total_runs / outs

        response = {
          'Batsman ':str(batter),
          'Innings':str(innings),
          'Total Runs Scored':str(batsman_total_runs),
          'Strike Rate':str(batsman_strike_rate),
          'Fours':str(fours),
          'Sixes':str(six),
          'Fifty':str(fifties),
          'Hundreds':str(hundred),
          'Highest Score':str(highestscore),
          'Average':str(average)
        }

        return str(response)
    else:
        return {"Message": 'Invalid Batsman Name...'}

def seasonwinner():
    winningteamseasom = matches[matches["MatchNumber"] == "Final"][['Season', 'WinningTeam']]
    SeasonWinner = winningteamseasom.set_index('Season')
    SeasonWinner= SeasonWinner.to_dict()
    return SeasonWinner


def venues():
    venues = matches[['City', 'Venue']].astype('str')
    venues = venues.drop_duplicates()
    venues = venues.set_index('City')
    venues = venues.to_dict()
    return venues

def teamatvenue(team,venue):
    # if team in matches[matches['Team1']] | team in matches[matches['Team2']]:
     try:
                played2 = matches[(matches['City'] == venue) & (matches['Team1'] == team)]
                t1 = played2.shape[0]
                played1 = matches[(matches['City'] == venue) & (matches['Team2'] == team)]
                t2 = played1.shape[0]
                venuematch_played = t1 + t2

                won = played2[played2.append(played1)['WinningTeam'] == team].shape[0]
                loss = venuematch_played - won
                winpercentage = won / venuematch_played * 100
                response = {
                     'Match Played At this Venue': venuematch_played,
                       'Match Won':won,
                     'Loss':loss,
                      'Win Percentage':winpercentage
                     }

                return response
     except:
             response ={
                 'Inalid Data ':'Enter Correct Input Check Spellings also '
             }
             return response

def allbatsmanstats():
    batsman_run.rank()
    batsman_run['batting_rank'] = batsman_run['batsman_run'].rank(ascending=False)
    # batsman_run.sort_values('batting_rank')
    batsmanruns= batsman_run.sort_values('batting_rank')
    batsmanruns=batsmanruns[['batter', 'batsman_run']].set_index('batter').to_dict()
    # batsmanruns={key: val for key, val in sorted(batsmanruns.items(), key=lambda ele: ele[1], reverse=True)}
    return str(batsmanruns)


def noofsix():
    six = ball_by_ball[ball_by_ball['batsman_run'] == 6]
    noofsixes = six.groupby('batter')['batter'].count().sort_values(ascending=False).to_dict()
    return str(noofsixes)
def powerhitters():
    from16over = ball_by_ball[ball_by_ball['overs'] > 15]
    from16over = from16over[(from16over['batsman_run'] == 4) | (from16over['batsman_run'] == 6)]

    powerhitter=from16over.groupby('batter')['batter'].count().sort_values(ascending=False).to_dict()
    return str(powerhitter)

def batsmanvsall(batsman):
    filtered_batsman = deliveries[deliveries['batsman'] == batsman]
    batsman =filtered_batsman.groupby('bowling_team')['batsman_runs'].sum().to_dict()
    return batsman