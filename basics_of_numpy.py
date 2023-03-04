import numpy as np

########################TOWRZENIE TABLIC I MACEIRZY##########################

#tworzenie tablic i macierzy ręcznie
a = np.array([1, 2, 3, 4, 5, 6])   #mozna dodac dtype='f' np. czyli floaty
m = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
#Axes to liczba wymiarów np 2D ma 2 axes - 1 ozaczający liczbę wierszy i 2 oznaczający liczbę kolumn

np.ones((2,2))   #tworzy tablice wypelnioną 0 lub 1
np.zeros(2)
np.zeros(2,3)
np.empty(2)

b = np.arange(4)
np.arange(2, 9, 2) #pierwsza ostatnia interwał
zzz = np.array([np.arange(0,5), np.arange(5,10)])

x = np.ones(2, dtype=np.int64)  #domyslnie float64

A = np.random.randint(10, size=(3,3))
B = np.random.randint(10, size=10)

arr1 = a[3:8]
np.vstack((a1, a2)) #stackowanie 2 tablic wertykalnie
np.hstack((a1, a2)) #horyzontalnie

x = np.arange(1, 25).reshape(2, 12)
a.reshape(2, 3)
arr = np.arange(6).reshape((2, 3))
arr.transpose()  #zmienia wymiary z 2x3 na 3x2

np.hsplit(x, 3)  #splituje na 3 tablice (macierze) o tym samym rozmiarze
np.hsplit(x, (3, 4)) #splituje na różne rozmiary po danych kolumnach 3 i 4

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b1 = a[0, :]  # zerowy wiersz i wszystkie kolumny
b1[0] = 99  #TWORZYMY SHALLOW KOPIE więc to też zmodyfikuje tablicę A - niejawna metoda view.
#jeśli nie chcemy zmieniać a to metoda copy:
b2 = a.copy()

a[1:4, 1:4] = z #w srodek jednej macierzy wstawiam inna macierz, edytując ta pierwszą

###########################INDEKSOWANIE#############################
'''
Takie jak normalnie w listach w python, ale możliwy dodatkowy zabieg:
'''
print(a[[0, 1, -2]])  #indeksowanie poprzez podanie indeksów w formie listy
#mozna tez indeksowac poprzez liste boolean [True, True, False]
a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[a < 5])   #[1 2 3 4], poniewaz to tak naprawde zwraca tablice bool
#mozna tez zwracac tablice bool np:
print(a<5) #zwraca bool wszystkich elementów

five_up = (a >= 5)
print(a[five_up])  # [ 5  6  7  8  9 10 11 12]  #tu też boole

'''
Czyli jeśli nie dam [] zwracam bool, jeśli dodam [] to znaczy ze operuje na elementach tablicy
'''

divisible_by_2 = a[a%2==0]
print(divisible_by_2)

c = a[(a > 2) & (a < 11)]
print(c)


if a[1][0] == a[1, 0]:  #indeksowanie macierzy - najpierw wiersz pozniej kolumna
    pass

a[0:2] #2 pierwsze wiersze i wszytskie kolumny
a[:, :2] #każdy wiersz ale z kolumny tyko do 2 elementu



###########################DODAWANIE, USUWANIE, SORTOWANIE#############
np.sort(a)
np.concatenate((a, b))
'''
a.size
a.ndim
a.shape
'''

y = np.arange(6)   #[0 1 2 3 4 5]
b = a.reshape(3, 2) #[[0 1][2 3][4 5]]

a = np.array([1, 2, 3, 4, 5, 6])
a.shape  #(6,)
row_vector = a[np.newaxis, :]  #dodawanie axis
row_vector.shape   #(1, 6)

col_vector = a[:, np.newaxis]
col_vector.shape  #(6, 1)


#############################OPERACJE NA TABLICY LUB MACIEZRY########################
'''
Są mutowalne jeśli dodamu = !!!!!!!!! patrz nizej:
a * 10 -> niemutowalne
a =+ 10 -> mutowalne

Są tez juz gotowe funckje do operacji na macierzach
'''
b = np.array([[1, 1], [2, 2]])
b.sum()
b.sum(axis=0)  #array([3, 3]) #wiersze
b.sum(axis=1)  #array([2, 4]) #kolumny

a.max()
a.min()
a.min(axis=0)

unique_values = np.unique(a)
unique_values, indices_list = np.unique(a, return_index=True)  #zwraca też indeksy
unique_values, occurrence_count = np.unique(a, return_counts=True)
unique_rows = np.unique(a_2d, axis=0)
unique_rows, indices, occurrence_count = np.unique(
     a_2d, axis=0, return_counts=True, return_index=True)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
arr ** 2
reversed_arr = np.flip(arr)  #Reversed Array:  [8 7 6 5 4 3 2 1]
reversed_arr_rows = np.flip(arr_2d, axis=0)  #domyślnie odwraca kolumny i wiersze, axis=0 to tylko wiersze
arr_2d[1] = np.flip(arr_2d[1]) #odwrocenie tylko wiersza o indeksie 1
arr_2d[:,1] = np.flip(arr_2d[:,1]) #odwrocenie kolumny o indeksie 1

#do splaszczania
'''
flatten spłaszcza tablicę i wykonuje kopię więc nie zmienia macierzy rodzicielskiej
ravel to tak jak view, zmiany z ravel także zmieniają ordzicielską macierz - shallow copy
'''

#operacje matematyczne -> onenote



############################ZAPISYWANIE I WCZYTAYWANIE#####################################
'''
save i load dla plikow npy
np.save('filename', a)

savetxt i loadtxt dla plikow txt lub csv
np.savetxt('new_file.csv', csv_arr)
np.loadtxt('new_file.csv')
'''

#Wczytywanie x csv najlepiej z użyciem pandas
x = pd.read_csv('music.csv', header=0).values #jesli wszystkie kolumny tego samego typu
x = pd.read_csv('music.csv', usecols=['Artist', 'Plays']).values

#aby zapisac najpierw konwersja z tablicy numpy do dataframe pandas
df = pd.DataFrame(a)
df.to_csv('pd.csv')
np.savetxt('np.csv', a, fmt='%.2f', delimiter=',', header='1,  2,  3,  4') #mozna tez tak zapisac



################################ WIZUALIZACJA #####################################
'''
z użyciem matplotlib
'''

a = np.array([2, 1, 5, 7, 4, 6, 8, 14, 10, 9, 18, 20, 22])
plt.plot(a)


x = np.linspace(0, 5, 20)
y = np.linspace(0, 10, 20)
plt.plot(x, y, 'purple') # line
plt.plot(x, y, 'o')      # dots