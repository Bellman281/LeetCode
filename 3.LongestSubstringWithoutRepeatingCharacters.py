class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0 :
            return 0
        visited=list(s[0])
        mx=1
        for i in range(1,len(s)):
                if( s[i] in visited):
                    visited=visited[visited.index(s[i])+1:]
                    visited.append(s[i]) 
                else:
                        visited.append(s[i])
                        mx=max(len(visited),mx)
        return(mx)
    
