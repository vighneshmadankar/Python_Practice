if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    def find_runner_up(scores):
        unique_scores = list(set(scores))
    
    # Sort the unique scores in descending order
        unique_scores.sort(reverse=True)
    
        # The runner-up score is the second item in the sorted list
        if len(unique_scores) > 1:
            return unique_scores[1]
        else:
            return "No runner-up exists"

scores = list(map(int, input("Enter the scores separated by spaces: ").split()))

# Find and print the runner-up score
runner_up = find_runner_up(scores)
print(f"The runner-up score is: {runner_up}")
