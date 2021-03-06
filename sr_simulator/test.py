# Python 3 code to demonstrate
# check if list are identical
# using sort() + == operator

# initializing lists
test_list1 = ['AD466943D1BDB6A9E8FDCA662352D2D3', '6847E1A4C6BD1C2C5FD1B5F462AF7419', 'F9BDEA5537051CC70E56C6A8DCE09676', 'C0D31D15AF7C842A6DC021A675856426', 'FC38AD5BA4E92DAB829782808B33C5E8', '8C0670317BCAB0DCE0FA7249B0BF55E7', '37647F1AC631F62E1A76F75BB94A3349', '9423F4D88C77DB018B1088F4168A92FD', '0296EB7F4AD5F031AEE46572E96F82DB', '92AA4EA4B1C4E1E1BE3A59216D10EF7C', 'AF220DEC9B2AA625FD644F2DF7460A76', '69B6CB763C04DAD61A7DA8455215D436', 'F474C58883B3CABFC2BE0416E727C03B', 'A8E64B001ADB45A1C4F5AE5BFD62B630', 'E07B85DC455F24D241350A773ADCFEC9', '5AC3B6A1732008DD8CA089A0EC4E03CE', 'CE4FC3CE275831D1E2B68161F2B18286']
test_list2 = ['AD466943D1BDB6A9E8FDCA662352D2D3', '6847E1A4C6BD1C2C5FD1B5F462AF7419', 'F9BDEA5537051CC70E56C6A8DCE09676', 'C0D31D15AF7C842A6DC021A675856426', 'FC38AD5BA4E92DAB829782808B33C5E8', '8C0670317BCAB0DCE0FA7249B0BF55E7', '37647F1AC631F62E1A76F75BB94A3349', '9423F4D88C77DB018B1088F4168A92FD', '0296EB7F4AD5F031AEE46572E96F82DB', '92AA4EA4B1C4E1E1BE3A59216D10EF7C', 'AF220DEC9B2AA625FD644F2DF7460A76', '69B6CB763C04DAD61A7DA8455215D436', 'F474C58883B3CABFC2BE0416E727C03B', 'A8E64B001ADB45A1C4F5AE5BFD62B630', 'E07B85DC455F24D241350A773ADCFEC9', '5AC3B6A1732008DD8CA089A0EC4E03CE', 'CE4FC3CE275831D1E2B68161F2B18286']
# sorting both the lists
test_list1.sort()
test_list2.sort()

# using == to check if
# lists are equal
if test_list1 == test_list2:
    print("The lists are identical")
else:
    print("The lists are not identical")