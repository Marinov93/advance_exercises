from collections import deque
# input with data from console for stack and deque
strength_of_kick = [int(x) for x in input().split()]
accuracy = deque([int(y) for y in input().split()])

scored_goals = 0

while strength_of_kick and accuracy:
    current_strength = strength_of_kick.pop()
    current_accuracy = accuracy.popleft()
    total_sum_values = current_strength + current_accuracy
    if total_sum_values == 100: # if equal he scores
        scored_goals += 1
    elif total_sum_values < 100:
        if current_strength < current_accuracy: # the condition tell to remove the strength from sequence - > already pop
            accuracy.append(current_accuracy)
        elif current_strength > current_accuracy: # the condition tell to remove the accuracy from sequence - > already pop
            strength_of_kick.append(current_strength)
        elif current_strength == current_accuracy:
            sum_current_values = current_strength + current_accuracy
            strength_of_kick.append(sum_current_values)
    elif total_sum_values > 100:
        strength_of_kick.append(current_strength - 10)
        accuracy.append(current_accuracy)

if scored_goals == 3:
    print("Paul scored a hat-trick!")
elif scored_goals <= 0:
    print("Paul failed to score a single goal.")
elif scored_goals > 3:
    print("Paul performed remarkably well!")
elif 0 < scored_goals < 3:
    print("Paul failed to make a hat-trick.")
if scored_goals:
    print(f"Goals scored: {scored_goals}")

if strength_of_kick:
    print(f"Strength values left: {', '.join(str(x) for x in strength_of_kick)}")
if accuracy:
    print(f"Accuracy values left: {', '.join(str(x) for x in accuracy)}")