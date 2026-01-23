class Yatzy:

    @staticmethod
    def chance(*dices):
        sum_all_scores = sum(dices)
        return sum_all_scores
    '''Code smell -> Mysterious name: total
       Refactoring -> Rename variables: sum_all_scores
       Code smell -> Don't repeat your self: repeat of total += d1/d2/d3/d4/d5
       Refactoring -> Using a Built-in Function: sum(dices)
       Code smell -> Long parameter list: (d1, d2, d3, d4, d5)
       Refactoring -> Introduce parameter object: *dices'''

    @staticmethod
    def yatzy(dices_points): 
        return 50 if dices_points[0] * 5 == sum(dices_points) else 0

    @staticmethod
    def ones(d1, d2, d3, d4, d5):
        total_score_ones = 0
        score_based_ones = (d1, d2, d3 ,d4, d5)
        for pip in score_based_ones:
            if pip == 1:
                total_score_ones += 1
        return total_score_ones

    @staticmethod
    def twos(d1, d2, d3, d4, d5):
        total_score_twos = 0
        score_based_ones = (d1, d2, d3 ,d4, d5)
        for pip in score_based_ones:
            if pip == 2:
                total_score_twos += 2
        return total_score_twos

    @staticmethod
    def threes(d1, d2, d3, d4, d5):
        total_score_threes = 0
        score_based_ones = (d1, d2, d3 ,d4, d5)
        for pip in score_based_ones:
            if pip == 3:
                total_score_threes += 3
        return total_score_threes

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
