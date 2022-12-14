def failure_function(pattern):
    n = len(pattern) 
    h = [0]*n 
    j,i = 0,1 
    h[0] = 0 
    while (i < n):
        if (pattern[i] == pattern[j]):
            h[i] = j + 1 
            i += 1 
            j += 1 
            continue 
        else:
            while (pattern[i] != pattern[j]):
                if (j > 0):j = h[j-1]
                else: j = -1 ; break 
            h[i] = j + 1 
            i += 1 
            j += 1
    return h 



# pattern = "abaababaabaab" # h = [0,0,1,1,2,3,2,3,4,5,6,4,5] 

# print(failure_function(pattern))


def pattern_matching(text,pattern): # returns an array of indices which represents the starting indices of all occurences of pattern in text

    h = failure_function(pattern) 
    i,j = 0,0 
    answers = [] 
    m,n = len(pattern),len(text) 
    while ( i < len(text)):
        while ( text[i] == pattern[j]): 
            if (j == m - 1):
                answers.append(i - m + 1)
                j = h[j] - 1 
            i,j = i+1,j+1 
            if (i == n):return answers 
            

        while (text[i] != pattern[j]):
            
            if (j > 0):
                j = h[j-1] 
            else: j -= 1;break 
        i,j = i+1,j+1 
    return answers  
    
text = "abaababaabacabaababaabaab" 
text = "abaababaabaababaababaabaab"
pattern = "aa" 

print(pattern_matching(text,pattern)) 


        




