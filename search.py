from pip._vendor.distlib.compat import raw_input

largest = None
smallest = None
while True:
    nums = raw_input("Enter a number: ")
    if nums == "done":
        break
    try:
        int(nums)
    except ValueError:
        print("Invalid input")
        continue
    for num in str(nums):
        if largest is None or num > largest:
            largest = nums
        if smallest is None or num < smallest:
            smallest = nums
print(str("Maximum" + " is " + largest))
print(str("Minimum" + " is " + smallest))
