import socket
from _thread import *
import sys
#uzywając modułu pickle jest o wiele latwiej - mogę wysyłac do serwera i z serwera cale obikety

server = "192.168.8.104"   #teraz użwyamy local ip czyli tylko użytkownicy tej samej sieci (tego samego wifi np) mogą sie połaczyc
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))     #bindujemy port i ip servera (jakikolwiek wprowdadze do server) do socketa
except socket.error as e:
    str(e)

s.listen(2)      #chce tylko 2 urzadzenia podłaczone do mojego serwera
print("waiting for a connection, server started")

def read_pos(stri):    #funckja obslugujaca przesylanie pozycji itd
    stri = stri.split(",")
    return int(stri[0]), int(stri[1]) #przyjmuje stringa zwracam krotke

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])  #zwracam stringa

pos = [(0, 0), (100, 100)]

def threaded_client(connection, player):
    connection.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(connection.recv(2048).decode())  #ilosc bitów przesyłanych jako informacja, im większa liczba tym dłuższa odpowiedz serwera. Jesli są błedy to zwiększyc
            #reply = data.decode("utf-8")     #dekodowanie informacji
            pos[player] = data
            if not data:
                print("Disconnected")        #jeśli brak żądan od klienta, rozłącz
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
                print("Received: ", data)
                print("Sending: ", reply)

            connection.sendall(str.encode(make_pos(reply)))
        except:
            break
    print("Lost connection")
    connection.close()

current_player = 0
while True:
    connection, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (connection, current_player))      #wielowątkowość - funckja wywołana skutkuje rozpoczęciem nowego procesu w tle, a pętla while dalej się wykonuje
    current_player += 1