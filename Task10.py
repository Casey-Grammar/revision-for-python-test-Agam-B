# Task 10 Class roll
# Write a program that takes a list of student names and sorts them
# to create a class roll. The list of names will be given on a one line
# separated by a single space.

#The student names could be entered with any combination of capitals or not.
#If they are entered with no capital first letter the list should not append.
#If they are entered with a capital first letter the list should append
#If they are entered with a mix of capitals the name should be converted to capital first letter and
#then added to the list.

def main():
    #Write your code here
    students = input('Students: ')
    all_names = students.split()
    all_names.sort()
    final_roll = []
    bad = []
    print('Class Roll')
    for name in all_names:
        if name.istitle():
            final_roll.append(name)
        elif name.isupper() or name.islower():
            bad.append(name)
        elif not name.islower() and not name.isupper():
            mixed = name.title()
            final_roll.append(mixed)
    for namez in final_roll:
        print(namez)
    # End of your code here





if __name__ == '__main__':
    main()