```python
def odd_sum(nums):
    # your code here
    total_sum = 0
    for num in nums:
        if num % 2 != 0:
            total_sum += num
    return total_sum

print(odd_sum([5, 4, 6, 13, 1]))
```


```python
def bigger_filter(nums, target):
    # your code here
    new_list = []
    for num in nums:
        if num > target:
            new_list.append(num)
    return new_list

print(bigger_filter([7, 3, 2, 8, 12], 5))
```

```python
def strange_words(words):
    # your code here
    # Less than 6 characters and don't start with e letter
    # more than 6 character and start with e letter
    final_words = []
    for letter in words:
        if len(letter) < 6 and letter[0] != "e":
            final_words.append(letter)
        if len(letter) >= 6 and letter[0] == "e":
            final_words.append(letter)
            
    return final_words

def print_string_array(strings):
```
