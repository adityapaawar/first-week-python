#program to sort a dictionary

color_dict= {'red':'#FF0000',
             'green':'#008000',
             'black':'#000000',
             'white':'#FFFFFF'}
sorted_dict = dict(sorted(color_dict.items()))
print("sorted dictionary based on keys:")
for key, value in sorted_dict.items():
    print(key, '--->>', value)

