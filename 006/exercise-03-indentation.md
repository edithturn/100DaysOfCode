
**Wrong indentation**
```python
def my_function():
print("This will run")
```

**Good indentation**
```python
def my_function():
  print("This will run")
```

**Good indentation**
```python
def my_function():
    print("This will run")
```

**Good indentation**
```python
def my_function():
  print("This will run")
print("Bye")
```

**Wrong indentation**
```python
def my_function():
    #This is my function
    print("This will run!")
    my_function()
```

**Good indentation**
```python
def my_function():
    #This is my function
    print("This will run!")
my_function()
```
**Wrong indentation**
```python
def my_function():
    a = 3
    if a > 2:
        print("This will run!")
my_function()
```

**Wrong indentation**
```python
def my_function():
a = 3
    if a > 2:
        print("This will run!")
my_function()
```

**Wrong indentation**
```python
def my_function():
    a = 3
    if a > 2:
        print("This will run!")
    my_function()
```

**Good indentation**
```python
def my_function():
    a = 3
    if a > 2:
        print("This will run!")
my_function()
```