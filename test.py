'''задание 1'''
number = int(input("Веведите число: "))
i = 1
factorial = 1
while i <= number :
    factorial *= i
    i+= 1
print(f"Факториал числа {number} равен {factorial}")

'''задание 2'''
a = int(input("Введите a: "))

even = 0
odd = 0
while a > 0:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1
    a = a // 10

print(f"Even: {even} \nOdd: {odd}")

'''задание 3'''
number = int(input("Введите число: "))
factorial = 1
for i in range(1, number+1):
    factorial *= i
print(f"Факториал числа {number} равен {factorial}")

'''задание 4'''
import math
a = int(input("Введите a: "))
print(math.factorial(a))

'''задание 5'''
x1 = int(input("Enter x1: "))
x2 = int(input("Enter x2: "))

h = 0.5
while x1 <= x2:
    y = -0.23 * x1 *x1 +x1
    print((f'x1 = {x1} -> y = {y}'))
    x1 += h

'''задание 6'''
k = 0
n = int(input("Введите число n: "))

for i in range(1, n+1):
    if (n % i) == 0:
        k += 1
if k == 2:
    print("Yes")
else:
    print("No")

'''задание 7'''
a = int(input("a = "))
b = int(input("b = "))

print(f'a = {a} -> b = {b}')
k = 0
for n in range(a, b+1):
    k = 0
    for i in range(2, n):
        if (n % i) == 0:
            k += 1
    if k == 0:
        print(n)

movies = {
    "Django Unchained": {
        "John": 10,
        "Jack": 9
    },
    "Troy": {}
}


def add_movie(movie_name):
    movie_name = movie_name.capitalize()
    if movie_name in movies:
        print("This movie already exists!")
    else:
        movies[movie_name] = {}
        print("Movie added successfully")
        print(movies)



def add_rating(movie_name, user_name, rating):
    movie_name = movie_name.capitalize()
    if movie_name not in movies:
        print("This movie doesn't exist")
        return

    if user_name in movies[movie_name]:
        print("User with this name already rated the movie. Please enter a different name.")
        return

    if 1 <= rating <= 10:
        movies[movie_name][user_name] = rating
        print(f"A rating has been added for {movie_name}: {user_name} rated it {rating}")
    else:
        print("Error: Rating should be between 1 and 10.")


def calculate_average_ratings():
    for movie_name, ratings in movies.items():
        if ratings:
            average_rating = sum(ratings.values()) / len(ratings)
            print(f"{movie_name} has an average rating of {average_rating}")
        else:
            print(f"Rating is not yet available for {movie_name}")


def find_movie(movie_name):
    movie_name = movie_name.capitalize()
    return movies.get(movie_name)


while True:
    print("\nOptions:")
    print("1. Add Movie")
    print("2. Add Rating")
    print("3. View Ratings")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        movie_name = input("Enter the movie name: ")
        add_movie(movie_name)
    elif choice == "2":
        movie_name = input("Enter the movie name: ")
        user_name = input("Enter your name: ")
        rating = int(input("Enter your rating (0-10): "))
        add_rating(movie_name, user_name, rating)
    elif choice == "3":
        calculate_average_ratings()
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")