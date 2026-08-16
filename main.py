while True:
    bin2 = input()

    if len(bin2) > 8:
        print("Введенное число больше требованного! Попробуйте заново ввести двоичное число!")
        continue

    correct = True

    for i in range(len(bin2)):
        if bin2[i] != '1' and bin2[i] != '0':
            correct = False
            break

    if not correct:
        print("Вы ввели что-то кроме 0 и 1. Попробуйте еще раз!")
        continue

    print("Ввод верный, идем дальше!")

    bin2 = bin2[::-1]
    step = 1
    summa = 0

    for i in range(len(bin2)):
        bin4 = int(bin2[i]) * step
        step = step * 2
        summa = summa + bin4

    print(summa)
    break