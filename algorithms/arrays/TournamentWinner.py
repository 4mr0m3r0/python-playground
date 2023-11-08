# O(n) time | O(k) space
def tournament_winner(competitions, results):
    top_winners: dict = {}
    winner = ""
    top_score = 0
    for i, competition in enumerate(competitions):
        result = results[i]
        home_team, away_team = competition
        winning_team = home_team if result == 1 else away_team
        if winning_team not in top_winners:
            top_winners[winning_team] = 0
        top_winners[winning_team] += 3
        if top_winners[winning_team] > top_score:
            top_score = top_winners[winning_team]
            winner = winning_team
    return winner
