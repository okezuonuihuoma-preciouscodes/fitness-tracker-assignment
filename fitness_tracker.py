
Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
Starting_fitness_level = input("Enter starting fitness level (beginner,intermediate,advanced): ")
Daily_step_goal = int(input("Enter daily step goal: "))
num_of_days = int(input("How many days is your challenge: "))
total_steps = 0
days_completed = 0
average_steps_per_day = 0
remark = ""
award = ""

while Name != "":   
    for i in range(1,num_of_days+1):
        day = int(input(f"Day{i}: "))
        total_steps += day
        if day >= Daily_step_goal:
            days_completed += 1

    average_steps_per_day = (total_steps/num_of_days)
    print()
    print(f"Total steps: {total_steps}")
    print(f"Average steps: {round(average_steps_per_day)}")
    print(f"Days goal achieved: {days_completed}")

    if average_steps_per_day >= 10000:
        remark = "Excellent"
    elif 9999 >= average_steps_per_day >= 8000:
        remark = "Great"
    elif 7999 >= average_steps_per_day >= 7000:
        remark = "Good"
    else:
        remark = "Needs improvement"
    print(f"Fitness rating: {remark}")

    if (average_steps_per_day >= 10000 and days_completed >= 5) or (Starting_fitness_level == 'advanced' and average_steps_per_day >= 12000):
        award = "🏆 Congratulations! You earned the Fitness Challenge Reward!"
    else:
        award = "Keep going! You didn't qualify for the reward this time."

    print(f"Award: {award}")
    question = input("Would you like to enter another participant? (yes/no):")
    if question == "yes":
        Name = input("Enter your name: ")
        Age = int(input("Enter your age: "))
        Starting_fitness_level = input("Enter starting fitness level (beginner,intermediate,advanced): ")
        Daily_step_goal = int(input("Enter daily step goal: "))
        num_of_days = int(input("How many days is your challenge: "))
    else:
        Name = ""

print("Thank you for using fitness tracker")

highest_number_of_steps_in_a_single_day = input("Enter your highest number of steps in a single day:")
lowest_number_of_steps_in_a_single_day = input("Enter your lowest number of steps in a single day:")
step_range = highest_number_of_steps_in_a_single_day - lowest_number_of_steps_in_a_single_day

print("")
print(f"Highest Steps per day:{highest_number_of_steps_in_a_single_day}")
print(f"Lowest Steps per day: {lowest_number_of_steps_in_a_single_day}")
print(f"step range/difference: {step_range}")



