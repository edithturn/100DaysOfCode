# Functions

```python
def my_functions():
    #instructions
```
```python
def greet(name, title, name1):
    print(f"My name is {name}")
    print(f"I love {title}")
    print(f"Do you want to play, {name1}")

greet()

```
### Functions with imputs
```python
def greet_with_name(name1, title, name2):
    print(f"My name is {name1}")
    print(f"I love {title}")
    print(f"Do you want to play, {name2}")

greet_with_name("Edith", "Coding", "Tomas")

```

### Functions with imputs (Positional Arguments)
```python
def greet_with_name(name1, title, name2):
    print(f"My name is {name1}")
    print(f"I love {title}")
    print(f"Do you want to play, {name2}")

greet_with_name(title="Coding", name1="Tomas",name2="Edith")

```