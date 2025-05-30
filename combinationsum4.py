# function to generate all possible letter combinations
def generate(ind, curr, ans, combos, digits):
    if ind == len(digits):
        ans.append(curr)  # when full combination is formed
        return
    index = int(digits[ind])  # get digit at current index
    for i in combos[index]:  # loop through corresponding letters
        generate(ind + 1, curr + i, ans, combos, digits)  # go to next digit

# main function to start process
def lettercombinations(digits):
    if len(digits) == 0:
        return []  # no input, return empty list
    combos = [" ", " ", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    ind = 0
    curr = ""  # start with empty string
    ans = []   # to store final combinations
    generate(ind, curr, ans, combos, digits)
    return ans

# input
digits = input()  # take digit string as input (e.g. "23")
print(lettercombinations(digits))
