try:
    numberOne = int(input("Enter the first number: "))
except Exception as e:
    print(f"An error occurred:")
else: # This block executes if no exceptions were raised
    print("No errors occurred.")
finally: # This block always executes
    print("Execution completed.")