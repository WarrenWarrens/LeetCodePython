class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        moves.upper()
        posx = 0
        posy = 0
        if len(moves) % 2 != 0:
            return False
        else:
            for j in range(len(moves)):
                if moves[j] in 'RULD':
                    if moves[j] in 'U':
                        posy += 1
                    elif moves[j] in 'L':
                        posx -= 1
                    elif moves[j] in 'D':
                        posy -= 1
                    else:
                        posx += 1
        if posx == 0 and posy == 0:
            return True
        else:
            return False




