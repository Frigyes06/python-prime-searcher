PRIME_SERIAL_NUMBER = 0

def check():
    global PRIME_SERIAL_NUMBER
    global INDEX
    NUMBER_OF_DIVIDER = 0
    TMP = round(INDEX/2)
    LOOP_COUNTER = 1
    for _ in range(TMP + 1):
        if INDEX % LOOP_COUNTER == 0:
            NUMBER_OF_DIVIDER += 1
            # print ("num div++") debug command
        LOOP_COUNTER += 1
        # print ("loop++") debug command
    if NUMBER_OF_DIVIDER == 1:
        PRIME_SERIAL_NUMBER -= 1
        # print ("serial num: " + str(PRIME_SERIAL_NUMBER)) debug command

if __name__ == '__main__':
    PRIME_SERIAL_NUMBER = int(input("hanyadik prímre vagy kíváncsi?: "))
    answer = PRIME_SERIAL_NUMBER
    INDEX = 1

    while PRIME_SERIAL_NUMBER != 0:
        INDEX += 1
        NUMBER_OF_DIVIDER = 0
        TMP = round(INDEX/2)
        LOOP_COUNTER = 1
        for _ in range(TMP + 1):
            if INDEX % LOOP_COUNTER == 0:
                NUMBER_OF_DIVIDER += 1
                # print ("num div++") debug command
            LOOP_COUNTER += 1
            # print ("loop++") debug command
        if NUMBER_OF_DIVIDER == 1:
            PRIME_SERIAL_NUMBER -= 1
            # print ("serial num: " + str(PRIME_SERIAL_NUMBER)) debug command
        # print ("Index: " + str(INDEX)) debug command
    else:
        print ("A " + str(answer) + ". prímszám a(z) " + str(INDEX))