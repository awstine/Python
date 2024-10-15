numbers = [6,3,6,7,3,7,4,2,78,3,2,]

mostFrequent = None
maxCount = 0

for num in numbers:
    count = numbers.count(num)

    if count>maxCount:
        maxCount = count
        mostFrequent = num
        if mostFrequent>1:
            print("cant display number with more than one frequency")
      

