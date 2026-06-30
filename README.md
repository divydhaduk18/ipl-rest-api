# IPL REST API using Flask

A REST API built using Flask and Pandas to analyze IPL match data.

## Features

- Get all IPL teams
- Team vs Team statistics
- Team record
- Team match history
- Match details
- IPL seasons
- Points table by season

## Tech Stack

- Python
- Flask
- Pandas
- NumPy

## APIs

### Get Teams

GET

```
/api/teams
```

### Team vs Team

```
/api/teamvteam?team1=Mumbai+Indians&team2=Chennai+Super+Kings
```

### Team Record

```
/api/team-record?team=Mumbai+Indians
```

### Matches

```
/api/matches?team=Mumbai+Indians
```

### Match Details

```
/api/match?id=1304115
```

### Seasons

```
/api/seasons
```

### Points Table

```
/api/points-table?season=2022
```

## Run

```bash
pip install -r requirements.txt

python app.py
```