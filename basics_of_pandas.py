import pandas as pd
import numpy as np
#mamy series i dataframe -> one note


##################### TWORZENIE OBIEKTÓW ################################
s = pd.Series([1, 3, 5, np.nan, 6, 8])

dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)




################################ WYSWIETLANIE DANYCH ##########################
df.head()
df.tail(3)
df.describe() #basic statistics
df.T #transpozycja
df.sort_index(axis=1, ascending=False) #sortuje malejąco po indeksach kolumn
df.sort_values(by="B")
medical_data.sort_values('wiek')

df.index
df.columns
medical_data['grupa']
medical_data[['grupa', 'wiek']]

#selekcja kolumn
df['A'] == df.A

#selekcja wierszy:
df[0:3]
df["20130102":"20130104"]

#selekcja obu
medical_data[0:1]['grupa']
medical_data.loc[0:0, 'grupa'] #0:1 daje 0 i 1 wiersz

#selekcja po label'u/indexie
df.loc[dates[0]]
df.loc[:, ["A", "B"]]
df.loc["20130102":"20130104", ["A", "B"]]

#selekcja po pozycji
df.iloc[3]   #3wiersz wszystkie kolumny
df.iloc[3:5, 0:2]
df.iloc[[1, 2, 4], [0, 2]]
df.iloc[1:3, :] #3 wiersz nie wchodzi
df.iloc[:, 1:3] #3 kolumna tu też nie

#selekcja po Boolach
df[df["A"] > 0]
df[df > 0]   #to zwraca fragment dataframe
print(df['Age'] > 100) #zwraca boole
df[df['Age'] > 100] #zwraca dataframe -> jeden wiersz nawet np.
print(df.loc[df['Age'] > 100, 'Age']) 
medical_data['wiek'] > 35 #boole
medical_data[medical_data['wiek'] > 35] #dataframe
medical_data.loc[medical_data['wiek'] > 35, 'grupa']
df['A'] > 0 #to zwraca serie booli
metoda between jeśli mam dwa warunki - mniejszy i wiekszy

for index, row in medical_data.iterrows():         #drukuje wiersze z indeksem wiersza
    print(index, row)

for name, col in medical_data.items():   #drukuje kolumny z nazwami
    print(name, col)

#wyswietlanie różnych typów danych i ich manipulacja
fifa.weight = [int(x.strip('lbs')) if type(x) == str else x for x in fifa.weight]

unique, value_counts

############################ FILTORWANIE ##############################################
f2 = df.copy()

df2["E"] = ["one", "one", "two", "three", "four", "three"]

df2
'''
                   A         B         C         D      E
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632    one
2013-01-02  1.212112 -0.173215  0.119209 -1.044236    one
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804    two
2013-01-04  0.721555 -0.706771 -1.039575  0.271860  three
2013-01-05 -0.424972  0.567020  0.276232 -1.087401   four
2013-01-06 -0.673690  0.113648 -1.478427  0.524988  three
'''

df2[df2["E"].isin(["two", "four"])] 

'''
                   A         B         C         D     E
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804   two
2013-01-05 -0.424972  0.567020  0.276232 -1.087401  four
'''
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
new_df.reset_index(drop=True, inplace=True) #zmienia cała dataframe bez tworzenia nowej zmiennej

df.loc[df['Name'].str.contains('Mega')]  #spoko
df.loc[~df['Name'].str.contains('Mega|NO', flags=re.I, regex=True)] 

df.groupby('Type 1').mean().sort_values('Defense', ascending=False)




#############################SETTING DATA ################################

#seria z odpowiednimi indexami:
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))
s1
'''
2013-01-02    1
2013-01-03    2
2013-01-04    3
2013-01-05    4
2013-01-06    5
2013-01-07    6
Freq: D, dtype: int64
'''
df["F"] = s1 #to działa dla stworzonych kolumn oraz niestworzonych - wówczas są dodawane
medical_data['new clumn'] = 11

#po label'u/indexie
df.at[dates[0], "A"] = 0

#po pozycji:
df.iat[0, 1] = 0

#bool:
df2 = df.copy()
df2[df2 > 0] = -df2  #zamieni wszystkie wartości na ujemne

#usuwanie danych
#po indeksie/label
df.drop('Canada') #ale oto nie są twałe operacje - shallow copy
df = df.drop('Canada') #trwała zmiana
df.drop(['Canada', 'Italy'])
#kolumny
df.drop(columns=['Populaton', 'Surface'])

#zmiana nazw kolumn i indexów/labelów
df.rename(
    columns = {
        pass
    },
    index={
        pass
    }
)

#dpdawanie kolumny z innych kolumn lub wierszy:
df['GDP per Capita'] = df['GDP'] / df['Population']
medical_data['new column'] = medical_data.iloc[:, 4:10].sum(axis=1)  #dodaje kolumne która jest sumą kolumn od 4 do 9 dla każdego wiersza

#conditional changes
df.loc[df['Type 1'] == 'Flame', 'Type 1'] = 'Fire'   #używam condition do zmiany jednej kolumny (type 1) na Fire jeśli uprzednio było flame

df.loc[df['Age'] > 100, 'Age'] = df.loc[df['Age'] > 100, 'Age'] / 10   #modyfikuje wszystkie te wiersze w których wartość kolumny Age jest > 100, i modyfikuje tylko kolumne dla tyc wierszy

df1['Male_FEemale'] = df1['Gender'].map({'Male': 1, 'Female': 0})
###########################################OPERACJE################################
df.mean()
df.mean(1) #po wierszach

#funkcja apply:
df.apply(np.cumsum)
df.apply(lambda x: x.max() - x.min())

#histogramming:
s = pd.Series(np.random.randint(0, 7, size=10))
s.value_counts()

#concat

#joinowanie w sql style:
left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})
pd.merge(left, right, on="key")

#groupowanie
df.groupby("A").sum()
df.groupby(["A", "B"]).sum() #tworzy się hierarhia

#reshaping
tuples = list(
    zip(
        *[
            ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
            ["one", "two", "one", "two", "one", "two", "one", "two"],
        ]
    )
)
index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])
df2 = df[:4]
df2
'''
                  A         B
first second                    
bar   one    -0.727965 -0.589346
      two     0.339969 -0.693205
baz   one    -0.339355  0.593616
      two     0.884345  1.591431
'''

#metody stack i unstack
cor = medical_data.groupby('grupa')[['LEU', 'wiek']].corr() #cala data frame
cor.unstack().iloc[:,1] 

#pd.pivot tables

#basic statistical methods
#wiadomo

#wyswietlanie różnych typów danych i ich manipulacja
fifa.weight = [int(x.strip('lbs')) if type(x) == str else x for x in fifa.weight]




########################### FAJNE TWORZENIE DAT I CZASÓW -> DOKUMNETACJA #############
rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")
rng = pd.date_range("1/1/2012", periods=100, freq="S")




############################ DANE KATEGORYCZNE ########################################
df = pd.DataFrame(
    {"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]}
)

df["grade"] = df["raw_grade"].astype("category")
'''
0    a
1    b
2    b
3    a
4    a
5    e
Name: grade, dtype: category
Categories (3, object): ['a', 'b', 'e']
'''
df["grade"].cat.categories = ["very good", "good", "very bad"]
#mozna tez je grupowac i sortować




##################### ODCZYT I ZAPIS DANYCH #########################################

#zapis i odczyt CSV:
df.to_csv("foo.csv")
pd.read_csv("foo.csv")
medical_data = pd.read_csv(f'./{fname}', sep=';', decimal=',')

#excel
df.to_excel("foo.xlsx", sheet_name="Sheet1")
pd.read_excel("foo.xlsx", "Sheet1", index_col=None, na_values=["NA"])

#caly przykładowy proces:
df = pd.read_csv('data/btc-market-price.csv', header=None)
df.columns = ['Timestamp', 'Price']
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df.set_index('Timestamp', inplace=True)
#lub wszystko na raz:
df = pd.read_csv(
    'data/btc-market-price.csv',
    header=None,
    names=['Timestamp', 'Price'],
    index_col=0,
    parse_dates=True
)


######################### SPRAWDZANIE ######################
'''
a.empty, a.any() or a.all(). czy wszystkie wartości są ok czyli nie ma zadnego na
'''
pd.Series([1, np.nan]).isnull().any()
medical_data.isna()  #cala tablica z boolami
medical_data.isna().any()  #bool dla każdej kolumny
medical_data.columns.isna() #jak wyżej ale w formie listy

#########################PLOTTING###############################
'''
z użyciem matplotlib -> dużo w dokumentacji nie musze się tego uczyć obvi
'''


########################### MISSING DATA ##############################
df1.dropna(how="any") # usuwa cale wiersze z na lub all jeśli caly wiersz jest na
df.dropna(axis=1)  # axis='columns' also works

df1.fillna(value=5) # zapelnia na
s.fillna(s.mean()) #seria
df.fillna({'Column A': 0, 'Column B': 99, 'Column C': df['Column C'].mean()})

pd.isna(df1) #zwraca boole
pd.isnull(df1) # to samo

#not null values:
df['Sex'].replace('D', 'F')
df['Sex'].replace({'D': 'F', 'N': 'M'})

#duplikaty
ambassadors.duplicated() #zwraca boole
ambassadors.drop_duplicates()
ambassadors.drop_duplicates(keep='last')
#dla dataframe:
players.duplicated(subset=['Name'])
players.duplicated(subset=['Name'], keep='last')
players.drop_duplicates()
players.drop_duplicates(subset=['Name'])

#stringi
df = pd.DataFrame({
    'Data': [
        '1987_M_US _1',
        '1990?_M_UK_1',
        '1992_F_US_2',
        '1970?_M_   IT_1',
        '1985_F_I  T_2'
]})

df['Data'].str.split('_')
df['Data'].str.split('_', expand=True) #tworzy data frame z tego co splituje
df.columns = ['Year', 'Sex', 'Country', 'No Children']
df['Country'].str.replace(' ', '')
df['Country'].str.strip()
df['Year'].str.contains('\?')