def all_palindrome(arr):
    for num in arr:
        # Convert number to string
        if str(num) != str(num)[::-1]:
            return False
    return True



arr1 = [111, 222, 333, 444, 555]
print(all_palindrome(arr1))  

arr2 = [121, 131, 20]
print(all_palindrome(arr2)) 
