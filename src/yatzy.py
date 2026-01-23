class Yatzy:

    @staticmethod
    def chance(*dices):
        return sum(dices)
    '''Code smell -> Mysterious name: total
       Refactoring -> Rename variables: sum_all_scores
       Code smell -> Don't repeat your self: repeat of total += d1/d2/d3/d4/d5
       Refactoring -> Using a Built-in Function: sum(dices)
       Code smell -> Long parameter list: (d1, d2, d3, d4, d5)
       Refactoring -> Introduce parameter object: *dices'''

    @staticmethod
    def yatzy(*dices_points):
        for face_dice in dices_points:
            if dices_points[0] * 5 != sum(dices_points):
                return 0
            else:
                return 50 

    @staticmethod
    def ones(*dices):
        return sum(face_dice for face_dice in dices if face_dice == 1)

    @staticmethod
    def twos(*dices):
        return sum(face_dice for face_dice in dices if face_dice == 2)

    @staticmethod
    def threes(*dices):
        return sum(face_dice for face_dice in dices if face_dice == 3)
    
    '''In ones, twos, threes:
    Code smell -> don't repeat your self
    Refactoring -> using a for loop and an if'''

    def __init__(self, d1=0, d2=0, d3=0, d4=0, _5=0):
        self.dice = [0] * 5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5

    def fours(*dices):
        return sum(face_dice for face_dice in dices if face_dice == 4)
    
    '''Code smell -> Mysterious name: at, sum
    Refactoring -> Rename variables: face_value, total_score_fours
    Code smell -> 
    Refactoring -> Introduce parameter object: *dice'''

    def fives(*dices):
        return sum(face_dice for face_dice in dices if face_dice == 5)

    def sixes(*dices):
        return sum(face_dice for face_dice in dices if face_dice == 6)

    '''
    lo hice por que era literalmente lo mismo 
    '''

    def score_pair(self, d1, d2, d3, d4, d5):
        counts = [0] * 6
        counts[d1 - 1] += 1
        counts[d2 - 1] += 1
        counts[d3 - 1] += 1
        counts[d4 - 1] += 1
        counts[d5 - 1] += 1
        at = 0
        for at in range(6):
            if (counts[6 - at - 1] == 2):
                return (6 - at) * 2
        return 0



    @staticmethod
    def two_pair(d1, d2, d3, d4, d5):
        counts = [0] * 6
        counts[d1 - 1] += 1
        counts[d2 - 1] += 1
        counts[d3 - 1] += 1
        counts[d4 - 1] += 1
        counts[d5 - 1] += 1
        n = 0
        score = 0
        for i in range(6):
            if (counts[6 - i - 1] >= 2):
                n = n + 1
                score += (6 - i)

        if (n == 2):
            return score * 2
        else:
            return 0

    @staticmethod
    def four_of_a_kind(_1, _2, d3, d4, d5):
        tallies = [0] * 6
        tallies[_1 - 1] += 1
        tallies[_2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i + 1) * 4
        return 0

    @staticmethod
    def three_of_a_kind(d1, d2, d3, d4, d5):
        t = [0] * 6
        t[d1 - 1] += 1
        t[d2 - 1] += 1
        t[d3 - 1] += 1
        t[d4 - 1] += 1
        t[d5 - 1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i + 1) * 3
        return 0

    @staticmethod
    def smallStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[0] == 1 and
                tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1):
            return 15
        return 0

    @staticmethod
    def largeStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1
                and tallies[5] == 1):
            return 20
        return 0

    @staticmethod
    def fullHouse(d1, d2, d3, d4, d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i + 1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i + 1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
