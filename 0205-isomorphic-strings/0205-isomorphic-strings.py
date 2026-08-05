class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        map_s_to_t = {}
        map_t_to_s = {}

        for cs, ct in zip(s, t):
            if cs in map_s_to_t:
                if map_s_to_t[cs] != ct:
                    return False
            else:
                map_s_to_t[cs] = ct

            if ct in map_t_to_s:
                if map_t_to_s[ct] != cs:
                    return False
            else:
                map_t_to_s[ct] = cs

        return True