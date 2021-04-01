# 1888 ms
# Hash Table, Two Pointers, String, Sliding Window

def lengthOfLongestSubstring(self, s):
    ans = dict()
    for n in range(s.__len__()):
        temp = ""
        temp_dict = []
        for val in range(n, s.__len__()):
            if(s[val] in temp_dict):
                ans[temp] = temp.__len__()
                break
            temp += s[val]
            temp_dict.append(s[val])
        else:
            ans[temp] = temp.__len__()

    ans = sorted(ans.items(), key=lambda num:num[1], reverse=True)
    
    if(bool(ans)):
        return ans[0][1]
    elif(s.__len__() > 0):
        return 1
    else:
        return 0