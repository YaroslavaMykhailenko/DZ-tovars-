import collections
tovars_list =input("Enter tovars that you bought:")
price_list =input("Enter prices of all tovars:")
my_sum = 0
def UniqueData(tovars_list):
    new_list = tovars_list.split(' ')
    print("Your tovars list:",new_list)
    new_price_list = price_list.split(" ")
    i = 0
    final_list = []
    for element in new_list:
        temporary_list = new_list[i]+ '-' + new_price_list[i]
        final_list.append(temporary_list)
        i +=1
    unigue_tovars = collections.Counter(final_list)
    return list(unigue_tovars)
my_unique_data = UniqueData(tovars_list)
print("Your unique Tovars:",my_unique_data)
for element in list(my_unique_data):
    a = element.split("-")
    my_sum += int(a[1])
print("Tovars' total sum:",my_sum)
