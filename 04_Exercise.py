import numpy as np
import matplotlib.pyplot as plt

filename = './befkbhalderstatkode.csv'

bef_stats_df = np.genfromtxt(
    filename, delimiter=',', dtype=np.uint, skip_header=1)

neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave',
          5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst',
          10: 'Amager Vest', 99: 'Udenfor'}

# print(bef_stats_df)
dd = bef_stats_df
area_mask = (dd[:, 0] == 2015)


def number_of_people_per_neighbourhood(n, mask):
    all_people_in_given_n = dd[mask & (dd[:, 1] == n)]
    # index 4 is no of 'PERSONER'
    sum_of_people = all_people_in_given_n[:, 4].sum()
    return sum_of_people


people2015 = np.array([number_of_people_per_neighbourhood(
    n, area_mask) for n in neighb.keys()])


index_max_ppl = np.argmax(people2015)

# print(list(neighb.keys()))

for i in range(0, 11):
    print("in 2015", people2015[i], 'people lived in',
          neighb[list(neighb.keys())[i]])

people2015 = np.array([number_of_people_per_neighbourhood(
    n, area_mask) for n in neighb.keys()])

temp = sorted(people2015)
plt.bar(list(neighb.values()), temp)
plt.xlabel("city")
plt.ylabel("people")
plt.title("amount of people in city")
# plt.show()


boolean_mask = (dd[:, 0] == 2015) & (dd[:, 2] > 64) & (
    dd[:, 3] == 5122) | (dd[:, 3] == 5114) | (dd[:, 3] == 5104)
all_people_in_other_c = dd[boolean_mask]
sum_of_people_in_other_c = all_people_in_other_c[:, 4].sum()
print(sum_of_people_in_other_c)
