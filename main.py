from algorithms import TournamentWinner


def run_script():
    result = TournamentWinner.tournament_winner(
        competitions=[["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]],
        results=[0, 0, 1]
    )
    print(result)


if __name__ == '__main__':
    run_script()
