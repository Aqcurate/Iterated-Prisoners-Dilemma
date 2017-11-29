from tournament import Tournament
from ipd import PrisonersDilemma as PD
from prisonerfactory import PrisonerFactory as PF
from graph import TimelineGif as TG

def test_pd():
    p1 = PF.get_prisoner('Spiteful')
    p2 = PF.get_prisoner('Greedy')
    c = PD(p1, p2)
    c.iterative_play(100, 200)

    print(p1.avg_score)
    print(p2.avg_score)


def test_tourny():
    p = {
        'Nice': 25,
        'Tit for Tat': 25,
        'Greedy': 25,
        'Spiteful': 25,
    }

    t = Tournament(p, 15)
    g = TG(t.run_tourny())
    g.generate('test.gif')

if __name__ == '__main__':
    test_pd()
    test_tourny()
