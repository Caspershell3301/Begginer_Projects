# Love Calculator :)
print("Welcome to the Love Calculator! ")
name1 = input("What is your Name? \n ").strip().lower()
name2 = input("What is your partner's name? \n").strip().lower()

combined_stg = name1 + name2

t = combined_stg.count('t')
r = combined_stg.count('r')
u = combined_stg.count('u')
e = combined_stg.count('e')
true_count = int(t) + int(r) + int(u) + int(e)

l = combined_stg.count('l')
o = combined_stg.count('o')
v = combined_stg.count('v')
e2 = combined_stg.count('e')
love_count = l + o + v + e2

total_count = str(true_count) + str(love_count)
total_count = int(total_count)

if total_count <= 10 or total_count >= 90:
    print(f" Your Score is {total_count}. You go together like Coke & Mentos ;) ")
elif total_count >= 40 and total_count <= 50:
    print(f" Your Score is {total_count}. You are alright together :) ")
else:
    print(f" You Score is {total_count}. Add some love to your life :|  ")






# Self Code Logic
# name1_count1 = name1.count('t')
# name1_count2 = name1.count('r')
# name1_count3 = name1.count('u')
# name1_count4 = name1.count('e')
#
# name2_count1 = name2.count('l')
# name2_count2 = name2.count('o')
# name2_count3 = name2.count('v')
# name2_count4 = name2.count('e')
#
# total_count1 = int(name1_count1) + int(name1_count2) + int(name1_count3) + int(name1_count4)
# total_count2 = int(name2_count1) + int(name2_count2) + int(name2_count3) + int(name2_count4)
#
# total_count = str(total_count1) + str(total_count2)
#
# total_count = int(total_count)
