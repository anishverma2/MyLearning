my_read = open('questions.txt', 'r')
list1 = [line.strip() for line in my_read.readlines()]
my_read.close()

count = 0
for line in list1:
    ques, ans = line.split('=')
    answer = int(input(f"{ques}="))
    if answer == int(ans):
        count += 1

my_write = open('results.txt', 'w')
my_write.write(f"Your final score is {count}/{len(list1)}.")
my_write.close()
