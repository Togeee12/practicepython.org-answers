# Welcome!
In this repository you can find answers to the challenges from [PracticePython](https://www.practicepython.org/). 

## What is it about?

Practice Python is a site which contains cool exercises created for Python Beginners! You can find out more about this project at [THIS LINK](https://www.practicepython.org/why-practice-python).

## Example

```python
how_many = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if how_many <= 0:
    print("Please enter a positive value: ")
elif how_many == 1:
    print("Fibonacci sequence upto", how_many, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < how_many:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
