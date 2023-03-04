#########################################ZAD 1 Fibonacci ##################################################

def fibonacci(n):     #time complexity is O(2^n) bo n razy wywołuje 2 kolejne rozgałęzienia 2^3 = 2 * 2 * 2
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_memo(n, memo = [1,1]):  #Here I use recursion with passing list to funcion so i have all values previously calculated in my list
    if n <= len(memo):        #then my complexity would be O(2n) = O(n)   this is dynamic programming - recursion with memorization!
        return memo[n-1]
    else:
        memo.append(fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo))
    return memo[n-1]



'''
print(fibonacci(50))   #waiting forever
print(fibonacci_memo(9))
'''


###########################################ZAD 2 -- GRID traveler ################################################

def grid_Traveler(m, n):      #time complexity O(2^n+m)
    if m == 1 and n == 1:
        return 1
    elif m == 0 or n == 0:
        return 0
    else:
        return grid_Traveler(m - 1, n) + grid_Traveler(m, n - 1)

def grid_Traveler_memo(m, n, memo):
    key = f'{m},{n}'
    key_rev = f'{n},{m}'
    if key in memo:
        return memo[key]
    elif key_rev in memo:
        return memo[key_rev]
    if m == 0 or n == 0:
        return 0
    memo[key] = grid_Traveler_memo(m - 1, n, memo) + grid_Traveler_memo(m, n - 1, memo)
    return memo[key]

'''
print(grid_Traveler_memo(44, 14, {'0,0': 0, '1,1': 1}))
print(grid_Traveler(44, 14))
'''


#########################################ZAD3 - CANSum ######################################################

def canSum(sum, tab):                                 #brute forcowe podejście brałoby pod uwage powtórzeń. Ja usuwam raz użyte wartości
    if sum == 0:                                      #dlatego to działa szybciej.
        return True
    for elem in tab:
        if sum - elem < 0:
            break
        tab.remove(elem)
        if canSum(sum - elem, tab) == True:
            return True
        tab.append(elem)
    return False


#print(canSum(350, [7, 14, 10, 6, 17, 10]))

def canSum_brute(sum, tab):                              #Tu jest brute force  O(n^m)    n-dlugosc tab  i m-sum
    if sum == 0:
        return True
    if sum < 0:
        return False
    for elem in tab:
        if canSum_brute(sum - elem, tab) == True:
            return True
    return False

#print(canSum_brute(300, [7, 14]))


def canSum_memo(sum, tab, memo = {}):                              #Tu jest użycie memo obiektu który zapisuje czy dane wywołanie funkcji z dana sumą może dać poztywny wynik
    if sum in memo:                                                # O(n*m)
        return memo[sum]
    if sum == 0:
        return True
    if sum < 0:
        return False
    for elem in tab:
        if canSum_memo(sum - elem, tab, memo) == True:
            memo[sum] = True
            return True
    memo[sum] = False
    return False

#print(canSum_memo(300, [7, 14]))




#########################################ZAD4 - HOWSum ######################################################

def HowSum_brute(sum, tab):                              #Tu jest brute force  O(n^m * m) * m ponieważ dodatkowym krokiem jest kopiowanie tablicy   n-dlugosc tab  i m-sum
    if sum == 0:
        return []
    if sum < 0:
        return None
    for elem in tab:
        result = HowSum_brute(sum - elem, tab)
        if result != None:
            result.append(elem)
            return result
    return None

#print(HowSum_brute(300, [7, 14]))


def HowSum(sum, tab, memo={}):                    #A tu time to O(n*m^2)
    if sum in memo:
        return memo[sum]
    if sum == 0:
        return []
    if sum < 0:
        return None
    for elem in tab:
        result = HowSum(sum - elem, tab, memo)
        if result != None:
            result.append(elem)
            memo[sum] = result
            return result
    memo[sum] = None
    return None

#print(HowSum(300, [7, 14]))


######################################ZAD5 - BESTSum ########################################################

def BestSum_brute(sum, tab):                              #Tu jest brute force O(n^m * m)
    if sum == 0:
        return []
    if sum < 0:
        return None
    shortestCombo = None
    for elem in tab:
        result = BestSum_brute(sum - elem, tab)
        if result != None:
            result.append(elem)
            if shortestCombo == None:
                shortestCombo = result
            if len(result) < len(shortestCombo):
                shortestCombo = result
    return shortestCombo

#print(BestSum_brute(7, [5,3,4,7]))



def BestSum(sum, tab, memo = {}):    ###               A tu time to O(n*m^2)
    if sum in memo:
        return memo[sum]
    if sum == 0:
        return []
    if sum < 0:
        return None
    shortestCombo = None
    for elem in tab:
        result = BestSum(sum - elem, tab, memo)
        if result is not None:
            result.append(elem)
            if shortestCombo is None or len(result) < len(shortestCombo):
                shortestCombo = result.copy()
    memo[sum] = shortestCombo
    return shortestCombo

#print(BestSum(100, [1, 2, 5, 25]))
#print(BestSum(100, [1, 2, 5, 25]))




##################################################CAN CONSTRUCT ##################################################

def canConstruct_brute(target, tab):                    #this one is actually working well without memo object in python

    #if any(t in target for t in tab):  #to by brało pod uwagę wyrazy w środku
        #return True
    if target == '':
        return True
    elif not any(target.startswith(t) or target.endswith(t) for t in tab):
        return False
    for substring in tab:
        if target.endswith(substring):
            if canConstruct_brute(target.rstrip(substring), tab):
                return True
        elif target.startswith(substring):
            if canConstruct_brute(target.lstrip(substring), tab):
                return True
    return False



print(canConstruct_brute('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(canConstruct_brute('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(canConstruct_brute('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(canConstruct_brute('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeee', 'feeeee', 'feee', 'fe', 'fff', 'eeeeefff', 'eeeeeeeeff', 'eeff', 'eeefffffff']))
