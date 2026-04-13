class Solution(object):
    def lengthOfLongestSubstring(self, s):
        st = set()
        left=0
        max_length=0

        for right in range(len(s)):
            st.add(s[right])

            if len(st)<right-left+1:
                while s[left]!=s[right]:
                    st.remove(s[left])
                    left+=1
                left+=1

            max_length=max(max_length,right-left+1)

        return max_length
        """
        :type s: str
        :rtype: int
        """
        