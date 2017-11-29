from ipd.prisonersdilemma import PrisonersDilemma as PD
from ipd.tournament import Tournament
from ipd.graph import TimelineGif as TG

def test_pd():
    c = PD('Spiteful', 'Greedy')
    c.iterative_play(100, 200)

    p1, p2 = c.get_prisoners()

    print(p1.avg_score)
    print(p2.avg_score)


def test_tourny():
    p = {
        'Nice': 25,
        'Tit for Tat': 25,
        'Greedy': 25,
        'Spiteful': 25,
    }

    t = Tournament(p, 25)
    g = TG(t.run_tourny())
    g.generate('graphs/sample.gif')

if __name__ == '__main__':
    test_pd()
    test_tourny()
