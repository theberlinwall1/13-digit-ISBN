while True:
        digit13 = input("Enter the first 12 digits of the 13 digit code (format: XXXXXXXXXXXX):\n >>> ")
        if digit13.isnumeric():
            if len(digit13) == 12:
                n = 0
                a = 0
                a += int(digit13[0])
                a += 3 * int(digit13[1])
                a += int(digit13[2])
                a += 3 * int(digit13[3])
                a += int(digit13[4])
                a += 3 * int(digit13[5])
                a += int(digit13[6])
                a += 3 * int(digit13[7])
                a += int(digit13[8])
                a += 3 * int(digit13[9])
                a += int(digit13[10])
                a += 3 * int(digit13[11])
                n = a % 10
                if n != 0:
                    n = 10 - n
                else:
                    n = 0
                print("The check digit is {}." .format(n))
                print("Your 13 digit ISBN code is...\n{}{}{}-{}-{}{}{}{}{}-{}{}{}-{}" .format(
                    digit13[0],digit13[1],digit13[2],digit13[3],digit13[4],digit13[5],digit13[6],digit13[7],digit13[8],digit13[9],digit13[10],digit13[11],n
                    ))
                break
            else:
                print("Input must be 12 digits long.")
                continue
        else:
            print("Input must have not special characters and letters.")
            continue