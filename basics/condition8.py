num = int(input('enter a number:'))

match num:
    case 1:
        print('sunday')
    case 2:
        print('monday')
    case 3:
        print('tuesday')
    case 4:
        print('wednesday')
    case 5:
        print('thursday')
    case 6:
        print('friday')
    case 7:
        print('saturday')
    case _ :#_ char act as a default, if one of the cases match
        print('invalid data')