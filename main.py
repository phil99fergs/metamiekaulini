def paranepara():

    c = a * 2
    b = a / c * 100

    print("Iespēja ka jūsu uzmestie kauliņi būs pāra skaitļi : ", b, "%")
    print("Iespēja ka jūsu uzmestie kauliņi būs nepāra skaitļi : ", b, "%")


def vienadi():

    c = a * 6
    d = a / c * 100
    print("Iespēja ka jūsu uzmestie kauliņi būs vienādi : ", round(d), "%")


def divivienadi():

    m = 2
    c = a * 6
    d = m / c * 100
    if a == 1:
        print("Iespēja ka starp jūsu uzmestiem kauliņiem būs divi vienādi skaitļi ir 0 %")
    else:
        print("Iespēja ka starp jūsu uzmestiem kauliņiem būs divi vienādi : ", round(d), "%")


def neatkartojas():
    if a == 1:
        print("Iespēja ka jūsu uzmestie kauliņi neatkartojās ir 100 %")
    elif a == 2:
        print("Iespēja ka jūsu uzmestie kauliņi neatkartojās ir 83 %")
    elif a == 3:
        print("Iespēja ka jūsu uzmestie kauliņi neatkartojās ir 66 %")
    elif a == 4:
        print("Iespēja ka jūsu uzmestie kauliņi neatkartojās ir 50 %")
    elif a == 5:
        print("Iespēja ka jūsu uzmestie kauliņi neatkartojās ir 33 %")



if __name__ == '__main__':
    print(
        "Sveiks, jūs sveicina programma kurā jūs varēsiet uzzināt noteiktas varbūtības uzmestiem kauliņiem. Piemēram, kāda iespēja kad jūsu uzmestie kauliņi būs pāra skaitļi?")
    a = int(input("Ievadiet kauliņu skaitu(1-5) : "))
    if a > 5:
        print("Maksimāli ir 5 kauliņi.")
        exit(0)

    paranepara()
    vienadi()
    divivienadi()
    neatkartojas()
