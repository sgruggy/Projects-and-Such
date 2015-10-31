#Word to number
#First making a dictionary
number_dictionary = {
    "one": 1,
    "two": 2,
    'three' : 3,
    'four' : 4,
    'five' : 5,
    'six' : 6,
    'seven': 7,
    'eight' : 8,
    'nine' : 9,
    'ten' : 10,
    'eleven': 11,
    "twelve" : 12,
    'thirteen' : 13,
    'fourteen' : 14,
    'fifteen': 15,
    'sixteen' : 16,
    'seventeen' : 17,
    'eighteen' : 18,
    'nineteen' : 19,
    'twenty' : 20,
    'thirty' : 30,
    'fourty' : 40,
    'fifty' : 50,
    'sixty' : 60,
    'seventy': 70,
    'eighty' : 80,
    'ninety' : 90,
    'hundred' : 100,
    'thousand': 1000,
    'million': 1000000,
    'billion' : 1000000000
    }
#Then the function
def word_to_number(word):
    #Splitting the words
    holder = word.split(" ")
    #Making a second holder
    result = []
    #output
    output = 0
    for i in holder:
        #Adding the results to second holder as integers
        result.append(number_dictionary[i.lower()])
    #Multiplying numbers less than 999
    i = 0
    while i < (len(result) - 1):
        if result[i] < 1000 and result[i+1] < 1000:
            if result[i] < result[i+1]:
                result[i] = result[i] * result[i+1]
                result.pop(i+1)
                i+=1
        i+=1
    y = 0
    while y< (len(result) - 1):
        if result[y] < 1000 and result[y+1] < 1000:
            result[y] = result[y] + result[y+1]
            result.pop(y+1)
            y+=1
        y+=1
    z = 0
    while z < (len(result) - 1):
        if result[z] < 1000 and result[z+1] < 1000:
            result[z] = result[z] + result[z+1]
            result.pop(z+1)
            z+=1
        z+=1
    x = 0
    while x < (len(result) - 1):
        if result[x] < result[x+1]:
            result[x] = result[x] * result[x+1]
            result.pop(x+1)
           
        x+=1
    total = 0
    for i in result:
        total = total + i
    return total

    
print (word_to_number("six billion six hundred sixty six million six hundred sixty six thousand six hundred sixty six"))

