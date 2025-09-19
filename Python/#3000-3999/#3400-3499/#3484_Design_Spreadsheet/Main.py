class Spreadsheet(object):

    def __init__(self, rows):
        """
        :type rows: int
        """
        self.mp = {}

    def setCell(self, cell, value):
        """
        :type cell: str
        :type value: int
        :rtype: None
        """
        self.mp[cell] = value

    def resetCell(self, cell):
        """
        :type cell: str
        :rtype: None
        """
        self.mp[cell] = 0

    def getValue(self, formula):
        """
        :type formula: str
        :rtype: int
        """
        s = formula[1:]  # remove leading "="
        parts = s.split('+')
        total = 0
        for term in parts:
            term = term.strip()
            if term[0].isalpha():
                total += self.mp.get(term, 0)
            else:
                total += int(term)
        return total
# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)