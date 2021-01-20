
**Wrong indentation**
```python
def my_function():
print("This will run")
```

```python
def my_function():
    #This is my function
    print("This will run!")
    my_function()
```

```python
def my_function():
    a = 3
    if a > 2:
        print("This will run!")
my_function()
```

```python
def my_function():
a = 3
    if a > 2:
        print("This will run!")
my_function()
```

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
  print("This will run")
```

```python
def my_function():
    print("This will run")
```

```python
def my_function():
  print("This will run")
print("Bye")
```

```python
def my_function():
    #This is my function
    print("This will run!")
my_function()
```

```python
def my_function():
    a = 3
    if a > 2:
        print("This will run!")
my_function()
```