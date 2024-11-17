# list_1 = [2,3,4]
# print(list_1)
# list_1[2] = 5
# print(list_1)

# pers = {
#     'name': 'Elena',
#     'age': 33,
#     'phone': [555,72851,665],
#     'language': {'mine': 'Russian', 'other': 'English'}
# }
# print(pers.items())
# print(pers.get('language', {}).get('mine'))

month_dict = {}
month = [1,2,3,4,5,6,7,8,9,10,11,12]
for i in month:
    month_dict[i] = f'Month - {i}'

print(month_dict)

users_info = []
N=3

for i in range(N):
    print(f'Enter {i+1} user`s info')
    name = input()