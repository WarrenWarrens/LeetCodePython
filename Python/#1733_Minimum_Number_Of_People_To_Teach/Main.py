class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        broken = set()
        plang = [set(langs) for langs in languages]
        mintoteach = float("inf")

        langknow = defaultdict(set)
        for p, langs in enumerate(plang):
            for l in langs:
                langknow[l].add(p)

        for u, v in friendships:
            if plang[u - 1].isdisjoint(plang[v - 1]):
                broken.add(u - 1)
                broken.add(v - 1)

        for i in range(1, n + 1):
            brokenknowlang = langknow[i] & broken
            toteach = len(broken) - len(brokenknowlang)
            mintoteach = min(mintoteach, toteach)

        return (mintoteach)

