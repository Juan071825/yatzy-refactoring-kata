from src.pips import Pips

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
    def yatzy(dices_points): 
        return 50 if dices_points[0] * 5 == sum(dices_points) else 0 

    @staticmethod
    def ones(*dices):
        return sum(face_dice for face_dice in dices if face_dice == Pips.ONE.value)

    @staticmethod
    def twos(*dices):
        return sum(face_dice for face_dice in dices if face_dice == Pips.TWO.value)

    @staticmethod
    def threes(*dices):
        return sum(face_dice for face_dice in dices if face_dice == Pips.THREE.value)
    
    '''In ones, twos, threes:
    Code smell -> don't repeat your self
    Refactoring -> using a for loop and an if'''

    def fours(*dices):
        return sum(face_dice for face_dice in dices if face_dice == Pips.FOUR.value)
    
    '''Code smell -> Mysterious name: at, sum
    Refactoring -> Rename variables: face_value, total_score_fours
    Code smell -> 
    Refactoring -> Introduce parameter object: *dice'''

    def fives(dices):
        return sum(face_dice for face_dice in dices if face_dice == Pips.FIVE.value)

    def sixes(dices):
        return sum(face_dice for face_dice in dices if face_dice == Pips.SIX.value)

    '''
    lo hice por que era literalmente lo mismo 
    '''

    def score_pair(self, *dices):
        pips= (pip.value for pip in Pips)
        pip_count = {pip: dices.count(pip) for pip in pips}
        
        pairs = [pip for pip, count in pip_count.items() if count >= 2]

        return max(pairs) * 2 if pairs else 0



    @staticmethod
    def two_pair(*dices):
        pips= (pip.value for pip in Pips)
        pip_count = {pip: dices.count(pip) for pip in pips}
        
        pairs_value = [pip for pip, count in pip_count.items() if count >= 2]
            
        if len(pairs_value) < 2:
            return 0
        
        two_biggest_pairs = sorted(pairs_value)[-2:]
        return sum(two_biggest_pairs) * 2



    @staticmethod
    def four_of_a_kind(*dices):
        pips= (pip.value for pip in Pips)
        pip_count = {pip: dices.count(pip) for pip in pips}

        for pip,count in pip_count.items():
            if count >= 4:
                return pip * 4
        
        return 0



    @staticmethod
    def three_of_a_kind(*dices):
        pips= (pip.value for pip in Pips)
        pip_count = {pip: dices.count(pip) for pip in pips}

        for pip,count in pip_count.items():
            if count >= 3:
                return pip * 3
        
        return 0



    @staticmethod
    def smallStraight(*dices):
        pips= (pip.value for pip in Pips)
        pip_count = {pip: dices.count(pip) for pip in pips}

        sequence_sum = sum(pip * count for pip, count in pip_count.items())
        
        if sequence_sum == 15:
            return sequence_sum
        return 0
        



    @staticmethod
    def largeStraight(*dices):
        pips= (pip.value for pip in Pips)
        pip_count = {pip: dices.count(pip) for pip in pips}

        sequence_sum = sum(pip * count for pip, count in pip_count.items())
        
        if sequence_sum == 20:
            return sequence_sum
        return 0



    @staticmethod
    def fullHouse(*dices):
        pips= (pip.value for pip in Pips)
        pip_count = {pip: dices.count(pip) for pip in pips}
    
        full_house = [count for pip, count in pip_count.items() if count == 3 or count == 2]

        if sum(full_house) == 5:
            return sum(pip * count for pip, count in pip_count.items())
        return 0
                

