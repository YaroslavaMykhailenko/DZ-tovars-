import collections
tovars_list =input("Enter tovars that you bought and their prices(use '-'):")
my_sum = 0
def UniqueData(tovars_list):
    new_list = tovars_list.split(' ')
    print("Your tovars list:",new_list)
    unigue_tovars = collections.Counter(new_list)
    return list(unigue_tovars)
my_unique_data = UniqueData(tovars_list)
print("Your unique Tovars:",my_unique_data)
for element in list(my_unique_data):
    a = element.split("-")
    my_sum += int(a[1])
print("Tovars' total sum:",my_sum)
