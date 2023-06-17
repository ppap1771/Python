from tika import parser
file = r'challenges\NIOS_YOGA-A_Sanskrit_Ch-2.pdf'
file_data = parser.from_file(file)
text = file_data['content']
print(text)