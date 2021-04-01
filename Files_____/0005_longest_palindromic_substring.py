# 8196 ms
# String, Dynamic Programing


def longestPalindrome(self, s: str) -> str:
    reverse = list(s).__reversed__()
    reverse = "".join(reverse)

    ans = []
    for main_index in range(s.__len__()):

        reverse_index = 0
        string_index = main_index
        flag = True

        while(flag):
            start_flag = None
            while(reverse_index <= s.__len__() - main_index - 1):
                if(s[string_index] == reverse[reverse_index]):
                    if(start_flag is None):
                        start_flag = string_index
                    string_index += 1
                else:
                    string_index = main_index
                    reverse_index += 1
                    flag = True
                    break
                reverse_index += 1
            else:
                flag = False
                ans.append([start_flag,string_index-1])

    temp_ans = [(j-i+1) for i,j in ans]

    if(temp_ans != []):
        temp = ans[temp_ans.index(max(temp_ans))]

        temp = s[temp[0] : temp[1]+1]

    else:
        temp = ""
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    s = reverse

    reverse = list(s).__reversed__()
    reverse = "".join(reverse)

    for main_index in range(s.__len__()):

        reverse_index = 0
        string_index = main_index
        flag = True

        while(flag):
            start_flag = None
            while(reverse_index <= s.__len__() - main_index - 1):
                if(s[string_index] == reverse[reverse_index]):
                    if(start_flag is None):
                        start_flag = string_index
                    string_index += 1
                else:
                    string_index = main_index
                    reverse_index += 1
                    flag = True
                    break
                reverse_index += 1
            else:
                flag = False
                ans.append([start_flag,string_index-1])

    temp_ans = [(j-i+1) for i,j in ans]

    if(temp_ans != []):
        temp_1 = ans[temp_ans.index(max(temp_ans))]

        temp_1 = s[temp_1[0] : temp_1[1]+1]
    else:
        temp_1 = ""

    if(temp.__len__() >= temp_1.__len__()):
        return temp
    else:
        return temp_1