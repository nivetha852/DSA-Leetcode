class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        properties.sort(key=lambda x: (-x[0], x[1]))
        maxdefense = 0
        weak = 0
        for attack, defense in properties:
            if defense < maxdefense:
                weak += 1
            else:
                maxdefense = defense
        
        return weak
        