###################fibonacci tabluation:

def fibonacciv2(n):   #time complexity is O(n)
    if n <= 2:        #this is dynamic programming with tabluation
        return 1
    seq = [1, 1]
    while n != 2:
        n -= 1
        new = seq[-1] + seq[-2]
        seq.append(new)
    return seq[-1]

#print(fibonacciv2(50))



################## grid traveler tabulation

def grid_traveler_tab(m, n):
    tab = [[0 for i in range(n+1)] for j in range(m+1)]
    tab[1][1] = 1
    for i, row in enumerate(tab):
        for j, elem in enumerate(row):                    #lub zamiast try moge zrobic inne zabezpieczenia przed przekroczeniem rozmiaru
            try:                                          #O(n) time and space
               tab[i+1][j] += elem
            except:
                pass
            try:
                tab[i][j + 1] += elem
            except:
                continue
    # for l in tab:
    #     print(f'{l}')
    return tab[-1][-1]


#print(grid_traveler_tab(3,3))



##################CanSum tabluation

def canSum_tab(sum, list):     #O(m*n)
     tab = [0] * (sum + 1)
     tab[0] = 1
     for i in list:
         tab[i] = 1
     for i in range(len(tab)):
         if tab[i] == 0 or i == 0:
             continue
         for elem in list:
             try:
                 tab[i+elem] = 1
             except:
                 continue
     if tab[-1] == 1:
         return True
     else:
         return False

#print(canSum_tab(300, [7, 14]))




##############HOW SUM tabulation    O(m^2 * n)  where m = targetSum n = tab.length

def how_sum_tab(sum, list):
    tab = [0] * (sum + 1)
    tab[0] = []
    for i in list:
        tab[i] = [i]
    for i in range(len(tab)):
        if tab[i] == 0 or i == 0:
            continue
        for elem in list:
            try:
                tab[i + elem] = tab[i].copy()
                tab[i + elem].append(elem)
            except:
                continue
    if tab[-1] != 0:
        return tab[-1]
    else:
        return False

#print(how_sum_tab(7, [2, 3]))




##########################BEST SUM TABULATION################################
def best_sum_tab(sum, list):  #time complexity is the same
    tab = [0] * (sum + 1)
    tab[0] = []
    for i in list:
        tab[i] = [i]
    for i in range(len(tab)):
        if tab[i] == 0 or i == 0:
            continue
        for elem in list:
            try:
                potential_array = tab[i].copy()
                potential_array.append(elem)
                if tab[i + elem] != 0 and len(tab[i + elem]) < len(potential_array):
                    continue
                else:
                    tab[i + elem] = potential_array
            except:
                continue
    if tab[-1] != 0:
        return tab[-1]
    else:
        return False

print(best_sum_tab(8, [1, 4, 5]))


