# importowanie słownika użytkowników
from file_with_dict_of_users import users_data

# funkcja logowania do systemu
def program():
    while True:
        user_login = input("Podaj login: ")
        if user_login in users_data.keys():
            log_in(user_login, users_data)
            break
        else:
            answer = input("Nie ma takiego użytkownika. Jeżeli chcesz się zarejestrować naciśnij klawisz T")
            if answer == "T" or answer == "t":
                sign_up(user_login, users_data)
                break

def log_in(login, users):
    counter = 1
    while counter != 4:
        user_password = input("Podaj hasło: ")
        if users[login] != user_password and counter < 3:
            print(f"Nieprawidłowe hasło !!! Możesz próbować jeszcze {3 - licznik}x")
            counter += 1
        elif users[login] != user_password and counter == 3:
            print(f"Użytkownik niezalogowany")
            counter += 1
        else:
            print("Użytkownik zalogowany")
            break

def sign_up(login, users):
    user_password = input(f"Podaj hasło dla użytkownika {login}: ")
    users[login] = user_password

if __name__ == "__main__":
    while True:
        program()
        for key, value in users_data.items():
            print(f"Użytkownik {key} - hasło {value}")
        answer = input("Jeżeli chcesz zakończyć pracę programu naciśnij klawisz T")
        if answer == "T" or answer == "t":
            break
    print("KONIEC PRACY PROGRAMU")
