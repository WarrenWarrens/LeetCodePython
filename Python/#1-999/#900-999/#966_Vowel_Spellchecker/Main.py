class Solution(object):
    def spellchecker(self, wordlist, queries):
        def to_lower(s):
            return s.lower()

        def mask_vowels(s):
            mv = "".join('*' if c in "aeiou" else c for c in s.lower())
            return mv

        exact = set(wordlist)
        case_map = {}
        for w in wordlist:
            lw = to_lower(w)
            if lw not in case_map:
                case_map[lw] = w

        vowel_map = {}
        for w in wordlist:
            mw = mask_vowels(w)
            if mw not in vowel_map:
                vowel_map[mw] = w

        ans = []
        for q in queries:
            if q in exact:
                ans.append(q)
            elif to_lower(q) in case_map:
                ans.append(case_map[to_lower(q)])
            elif mask_vowels(q) in vowel_map:
                ans.append(vowel_map[mask_vowels(q)])
            else:
                ans.append("")
        return ans