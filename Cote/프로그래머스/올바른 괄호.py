def solution(s):
    answer = True
    n_list = []
    
    for i in s:
        if i == '(':
            n_list.append('(')
        
        else:
            if n_list == []:
                return False
        
            else:
                n_list.pop()
        
    if n_list != []:
        return False
    return True
