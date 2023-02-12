# # Given a “Matrix” string:
# #
# # 7i3
# # Tsi
# # h%x
# # i #
# # sM
# # $a
# # #t%
# # ^r!
#
# # The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden message in it.
# # A grid means that you could potentially break it into rows and columns, like here
# #
# # Use
# # ● lists for storing data
# # ● Loops for going through the data
# # ● if/else statements to check the data
# # ● String for the output of the secret message

list_matrix = '''7i3
Tsi
h%x
i #
sM 
$a 
#t%
^r!'''

list_items = list_matrix.split('\n')
final = ' '
if len(list_items) > 0:
    for col in range(0, len(list_items[0])):
        for row in list_items:
            if row[col].isalpha():
                final += row[col]
            else:
                if final[-1] != ' ':
                    final += ' '
print(final)
