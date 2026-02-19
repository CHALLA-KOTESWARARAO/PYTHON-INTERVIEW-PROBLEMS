# def intToRoman(num):
#     # We list all Roman numeral values in descending order — including subtractive forms:
#     roman_map = [
#         (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
#         (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
#         (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
#         (1, "I")
#     ]

#     result = ""
# #     2️⃣ Greedy Approach
# # Loop from largest to smallest Roman value:
#     for value, symbol in roman_map:
#         while num >= value:
#             result += symbol
#             num -= value
    
#     return result
# print(intToRoman(41))


# def intToRoman(rom):
#     roman_map = [
#     (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
#     (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
#     (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
#     (1, "I")]
#     res=""
   

roman_map = {
    "M":1000, "CM":900, "D":500, "CD":400,
    "C":100, "XC":90, "L":50, "XL":40,
    "X":10, "IX":9, "V":5, "IV":4, "I":1
}

 # ['C','X','I','V']

try:
    res = 0
    rom = list("I") 
    while rom:
    # Check next two characters if possible
        if len(rom) >= 2:
            pair = rom[0] + rom[1]
            if pair in roman_map:
                res += roman_map[pair]
                rom.pop(1)
                rom.pop(0)
            else:
                res += roman_map[rom[0]]
                rom.pop(0)
        else:
            res += roman_map[rom[0]]
            rom.pop(0)
    print(res)
except Exception as e:
    print("invalid input")


