# ISBN Check Digit Calculator
# This program gives the user the ability to verify
# the check digit of a ten digit and thirteen digit
# ISBN number and the option to convert between the two

print('Welcome to your ISBN Check Digit Calculator. \n\n' \
              'This program verifies the check digit of a given ISBN '\
              'number. \nIt has the ability to verify ten and thirteen '\
              'digit numbers \nas well as convert from one to the other. '\
              'Enjoy!')
print()
input('Press ENTER to Continue')

### MAIN MENU ###

def main():
    loop = 1
    choice = 0
    while loop == 1:
        print('')
        
        print('')
        print('Your options are: ')
        print('')
        print('1.Verify the check digit of an ISBN-10')
        print('2.Verify the check digit of an ISBN-13')
        print('3.Convert an ISBN-10 to an ISBN-13')
        print('4.Convert an ISBN-13 to an ISBN-10')
        print('5.Exit')
        print()
                
        while True:
            try:
                choice = int(input('Choose your option: '))
            except ValueError:
                print('INVALID ENTRY')
                print()
                continue
            else:
                if choice == 1:
                    read_write_10()
                elif choice == 2:
                    read_write_13()
                elif choice == 3:
                    read_write_10_13()
                elif choice == 4:
                    read_write_13_10()
                elif choice == 5:
                    Exit()

                    
### INPUT SECTION ###

def read_write_10():
    
    # Ask the user if they would like to inout the number
    # or for the number to be read from a file
    print('Would you like to input the number '\
          'or have it read from a text file?: ')
    
    while True:
            try:
                choice = str(input("Hit 'F' for File or 'M' for Manual entry: "))
                
            except ValueError:
                print('INVALID ENTRY')
                print()
                continue
            else:
                choice = choice.upper()
                if choice == 'M':
                    ISBN_10()
                elif choice == 'F':
                    check_file()
                elif choice != 'F' or choice != 'M':
                    print('INVALID ENTRY')
                

def read_write_13():
    
    # Ask the user if they would like to input the number
    # or for the number to be read from a file
    print('Would you like to input the number '\
          'or have it read from a text file?: ')
    
    while True:
            try:
                choice = str(input("Hit 'F' for File or 'M' for Manual entry: "))
                
            except ValueError:
                print('INVALID ENTRY')
                print()
                continue
            else:
                choice = choice.upper()
                if choice == 'M':
                    ISBN_13()
                elif choice == 'F':
                    check_file()
                elif choice != 'F' or choice != 'M':
                    print('INVALID ENTRY')

def read_write_10_13():
    
    # Ask the user if they would like to inout the number
    # or for the number to be read from a file
    print('Would you like to input the number '\
          'or have it read from a text file?: ')
    
    while True:
            try:
                choice = str(input("Hit 'F' for File or 'M' for Manual entry: "))
                
            except ValueError:
                print('INVALID ENTRY')
                print()
                continue
            else:
                choice = choice.upper()
                if choice == 'M':
                    ISBNC_10_13()
                elif choice == 'F':
                    check_file_change()
                elif choice != 'F' or choice != 'M':
                    print('INVALID ENTRY')

def read_write_13_10():
    
    # Ask the user if they would like to inout the number
    # or for the number to be read from a file
    print('Would you like to input the number '\
          'or have it read from a text file?: ')
    
    while True:
            try:
                choice = str(input("Hit 'F' for File or 'M' for Manual entry: "))
                
            except ValueError:
                print('INVALID ENTRY')
                print()
                continue
            else:
                choice = choice.upper()
                if choice == 'M':
                    ISBNC_13_10()
                elif choice == 'F':
                    check_file_change()
                elif choice != 'F' or choice != 'M':
                    print('INVALID ENTRY')

def check_file():
    digits = 0
    
    print('\nEnsure the text file is located in the same folder '\
          'as the program and continue.')
    
    # Request input fron the user
    try:
        filename = input('Enter the name of the text file. \nMake sure '\
             'to include the file extension: ')

        # open the file for reading assigned to infile variable
        infile = open(filename, 'r')
        isbn = infile.read()
        
    # Exception handler for if there is no file located
    # in the folder with the specified name
    except IOError:
        print('AN ERROR OCCURED WHEN TRYING TO READ THE FILE.')
        print('IT MAY NOT EXIST IN THE PROPER LOCATION.')
        check_file()
        
    # Close the file
    infile.close()
    
    # Clean the input
    clean_isbn = isbn.replace('-','').replace(' ','')

    # Input the numbers into a list
    clean_isbn = [str(i) for i in clean_isbn]

    # Map to a list of integers
    clean_isbn = list(map(int, clean_isbn))

    # Calculate the number of digits in the list
    for ch in range(len(clean_isbn)):
        digits+=1

    # Pass the argument to the appropriate function    
    if digits == 10:
        clean_10 = clean_isbn[:9]                    
        Calculate_Check10(clean_10)
        
    elif digits == 9:
        Calculate_Check10(clean_isbn)
        
    elif digits == 13:
        clean_13 = clean_isbn[:12]
        Calculate_Check13(clean_13)
        
    elif digits == 12:
        Calculate_Check13(clean_isbn)
        
    else:
        print('Your file is unable to be read correctly')
        print('Please correct the file or '\
              'proceed with entering you number manually.')
        main()
                  
def check_file_change():
    digits = 0
    
    print('\nEnsure the text file is located in the same folder '\
          'as the program and continue.')
    
    # Request input fron the user
    try:
        filename = input('Enter the name of the text file. \nMake sure '\
             'to include the file extension: ')

        # open the file for reading assigned to infile variable
        infile = open(filename, 'r')
        isbn = infile.read()
        
    # Exception handler for if there is no file located
    # in the folder with the specified name
    except IOError:
        print('AN ERROR OCCURED WHEN TRYING TO READ THE FILE.')
        print('IT MAY NOT EXIST IN THE PROPER LOCATION.')
        check_file_change()
        
    # Close the file
    infile.close()
    
    # Clean the input
    clean_isbn = isbn.replace('-','').replace(' ','')

    # Input the numbers into a list
    clean_isbn = [str(i) for i in clean_isbn]

    # Map to a list of integers
    clean_isbn = list(map(int, clean_isbn))

    # Calculate the number of digits in the list
    for ch in range(len(clean_isbn)):
        digits+=1

    # Pass the argument to the appropriate function    
    if digits == 10:
        clean_10 = clean_isbn[:9]                    
        Convert_10_13(clean_10)
        
    elif digits == 9:
        Convert_10_13(clean_isbn)
        
    elif digits == 13:
        clean_13 = clean_isbn[:12]
        Convert_13_10(clean_13)
        
    elif digits == 12:
        Convert_13_10(clean_isbn)
        
    else:
        print('Your file is unable to be read correctly')
        print('Please correct the file or '\
              'proceed with entering you number manually.')
        main()


def ISBN_10():
    user_list10 = []
    index = 0

    # Communicate the chosen action
    print('\nYou have chosen to verify the check digit of an ISBN-10.')

    # Ensure that only integers are accepted
    while True:
        try:
            # Get the nine digits from the user
            ISBN = input('Enter the first nine digits of '\
                             'your number with no dashes: ')

            # Convert the individual integers into a list
            # of string characters first to accept leading zeroes
            user_list10 = [str(i) for i in ISBN]
                        
            # Then convert to a list of integers for calculations
            user_list10 = list(map(int, user_list10))
            
            # Ensure nine digits are entered 
            for ch in range(len(ISBN)):
                index += 1
                
            if index != 9:
                print('INVALID NUMBER OF DIGITS')
                ISBN_10()
            else:
                True
        except ValueError:
            print('INVALID ENTRY')
            continue
        else:
            # Pass the list as an argument to processing section
            # to be used for calculation of ISBN-13
            Calculate_Check10(user_list10)
            
            

def ISBN_13():
    user_list13 = []
    index = 0

    print('\nYou have chosen to verify the check digit of an ISBN-13.')
          
    while True:
        try:
            # Get the first twelve digits from the user
            ISBN = input('Enter the first twelve digits of '\
                         'your number with no dashes: ')
            user_list13 = [str(i) for i in ISBN]
                        
            # Then convert to a list of integers for calculations
            user_list13 = list(map(int, user_list13))
            
            # Ensure twelve digits are entered 
            for ch in range(len(ISBN)):
                index += 1
                
            #print(index)
            if index != 12:
                print('INVALID NUMBER OF DIGITS')
                ISBN_13()
            else:
                True
        # Handle exceptions        
        except ValueError:
            print('INVALID ENTRY')
            continue
        else:
            # Send argument to processing
            Calculate_Check13(user_list13)

def ISBNC_10_13():
    userlist10 = []
    index = 0
    
    print('\nYou have chosen to convert an ISBN-10 to an ISBN-13.')
    print('A new check digit will be calculated as well.')
          
    while True:
        try:
            # Get the nine digits from the user
            ISBN = input('Enter the first nine digits of '\
                             'your number with no dashes: ')

            # Convert the individual integers into a list
            # of string characters first to accept leading zeroes
            userlist10 = [str(i) for i in ISBN]
                        
            # Then convert to a list of integers for calculations
            userlist10 = list(map(int, userlist10))
            
            # Ensure nine digits are entered 
            for ch in range(len(ISBN)):
                index += 1
                
            #print(index)
            if index != 9:
                print('INVALID NUMBER OF DIGITS')
                ISBNC_10_13()
            else:
                True
        except ValueError:
            print('INVALID ENTRY')
            continue
        else:
            # Pass the argument to be processed
            Convert_10_13(userlist10)

def ISBNC_13_10():
    userlist13 = []
    index = 0
    
    print('\nYou have chosen to convert an ISBN-13 to an ISBN-10.')
    print('A new check digit will be calculated as well.')
    
    while True:
        try:
            # Get the first twelve digits from the user
            ISBN = input('Enter the first twelve digits of '\
                         'your number with no dashes: ')
            userlist13 = [str(i) for i in ISBN]
                        
            # Then convert to a list of integers for calculations
            userlist13 = list(map(int, userlist13))
            
            # Ensure twelve digits are entered 
            for ch in range(len(ISBN)):
                index += 1
                
            #print(index)
            if index != 12:
                print('INVALID NUMBER OF DIGITS')
                ISBNC_13_10()
            else:
                True
        # Handle exceptions        
        except ValueError:
            print('INVALID ENTRY')
            continue
        else:
            # Send argument to processing
            Convert_13_10(userlist13)
            

### PROCESSING SECTION ###

def Calculate_Check10(numberlist):
    total = 0
    multiplier = 1
    
    # Use a for loop multiply each character by its weighted value
    # and then total the sum of the characters
    for ch in numberlist:
        check = ch*multiplier
        multiplier+=1
        
        total += check

    # Get the remainder when devided by 11 to get the check digit
    check_digit = total%11
    
    # Convert to Roman Numeral X for remainder of 10
    if check_digit == 10:
        check_digit = ('X')
    else:
        True

    #print('The total so far after weighting is: ', total)
    print('\nThe check digit is: ', check_digit)
    
    # Add the check digit to our ISBN list
    numberlist.append(check_digit)
        
    # Send the updated list to the Output section as an argument
    Output_10(numberlist)

    
def Calculate_Check13(numberlist):
    total = 0
    multiplier = [1,3,1,3,1,3,1,3,1,3,1,3]
    
    # Use a for loop to iterate through the lists
    # and multiply the corresponding values
    # Then accumulate them with total
    for i in range(len(numberlist)):
        weight = numberlist[i]*multiplier[i]
        total += weight

    # Calculate the check digit    
    check_digit = total%10
        
    #print('The total so far after weighting is: ', total)
    print('\nThe check digit is: ', check_digit)

    # Add the check digit to the end of the list
    numberlist.append(check_digit)

    # Send argument to output
    Output_13(numberlist)

def Convert_10_13(numberlist):
    # Initialize variables
    total = 0
    multiplier = [1,3,1,3,1,3,1,3,1,3,1,3]
    addtolist = [9,7,8]

    # Add 9,7,8 to the beginning of the list
    userlist_converted13 = addtolist + numberlist
    
    # Calculate the new check digit
    for i in range(len(userlist_converted13)):
        weight = userlist_converted13[i]*multiplier[i]
        total += weight

    check_digit = total%10

    print('\nThe new check digit is: ', check_digit)
    
    # Append the new check digit to the list    
    userlist_converted13.append(check_digit)
        
    Output_13(userlist_converted13)

def Convert_13_10(numberlist):
    total = 0
    multiplier = 1

    # Remove the 9,7,8 from the beginning of the list
    numberlist = numberlist[3:]
    
    # Calculate new check digit
    # Use a for loop multiply each character by its weighted value
    # and then total the sum of the characters
    for ch in numberlist:
        check = ch*multiplier
        multiplier+=1
        
        total += check

    # Get the remainder when devided by 11 to get the check digit
    check_digit = total%11
    
    # Convert to Roman Numeral X for remainder of 10
    if check_digit == 10:
        check_digit = ('X')
    else:
        True
    #print('The total so far after weighting is: ', total)
    print('\nThe new check digit is: ', check_digit)
    
    # Add the check digit to our ISBN list
    numberlist.append(check_digit)
    
    # Send the updated list to the Output section as an argument
    Output_10(numberlist)


### OUTPUT SECTION ###

def Output_10(Final_ISBN):
    
    # Copy to a new list f as a string
    f = Final_ISBN
    f = list(map(str, f))

    # Concantenate into one string
    f = ''.join(f)

    # Format for printing with dashes
    f = '-'.join((f[:1],f[1:3],f[3:9],f[9:]))
    
    print('Your formatted ISBN-10 number is: ', f)
    print('Your formatted ISBN-10 number has also been '\
          'written \nto a file named ISBN_10_Output.txt')
    
    # Write the data to an output file
    outfile = open('ISBN_10_Output.txt', 'a')
    outfile.write('\nYour formatted ISBN-10 number is: '+ str(f))
    outfile.close()
    
    
    # Option to continue
    rerun=input('\nWould you like to analyze another number?\n' + \
                '(Enter y for Yes): ')
    if rerun==('y') or rerun==('Y'):
        main()
    else:
        Exit()

def Output_13(Final_ISBN):
    
    # Copy to a new list f as a string
    f = Final_ISBN
    f = list(map(str, f))

    # Concantenate into one string first
    f = ''.join(f)

    # Format for printing with dashes
    f = '-'.join((f[:3],f[3:4],f[4:6],f[6:12],f[12:]))
    
    print('Your formatted ISBN-13 number is: ', f)
    print('Your formatted ISBN-13 number has also been '\
          'written \nto a file named ISBN_13_Output.txt')
    
    # Write the data to an output file
    outfile = open('ISBN_13_Output.txt', 'a')
    outfile.write('\nYour formatted ISBN-13 number is: '+ str(f))
    outfile.close()
    
    
    # Option to continue
    rerun=input('\nWould you like to analyze another number?\n' + \
                '(Enter y for Yes): ')
    if rerun==('y') or rerun==('Y'):
        main()
    else:
        Exit()
    
    
            
def Exit():
    print('OK, GOODBYE.')
    input()
    exit()
    

main()
              
