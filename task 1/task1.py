# Create a shopping list
shopping_list = []

def add_to_shopping_list(item):
  """Adds an item to the shopping list."""
  shopping_list.append(item)
  print(f"Added {item} to shopping list.")

def remove_from_shopping_list(item):
  """Removes an item from the shopping list."""
  if item in shopping_list:
    shopping_list.remove(item)
    print(f"Removed {item} from shopping list.")
  else:
    print(f"{item} not found in shopping list.")

def print_shopping_list():
  """Prints the current shopping list."""
  if shopping_list:
    print("Shopping List:")
    for item in shopping_list:
      print(f"- {item}")
  else:
    print("Shopping list is empty.")

# Create a student information dictionary
student_info = {}

def add_student_info(key, value):
  """Adds a key-value pair to the student information dictionary."""
  student_info[key] = value
  print(f"Added {key}: {value} to student information.")

def update_student_info(key, value):
  """Updates the value of an existing key in the student information dictionary."""
  if key in student_info:
    student_info[key] = value
    print(f"Updated {key} to {value} in student information.")
  else:
    print(f"{key} not found in student information.")

def print_student_info():
  """Prints the current student information."""
  if student_info:
    print("Student Information:")
    for key, value in student_info.items():
      print(f"{key}: {value}")
  else:
    print("Student information is empty.")


# Create a set of movies watched
watched_movies = set()

def add_watched_movie(movie):
  """Adds a movie to the set of watched movies."""
  watched_movies.add(movie)
  print(f"Added {movie} to watched movies.")

def remove_watched_movie(movie):
  """Removes a movie from the set of watched movies (if present)."""
  watched_movies.discard(movie)  # discard won't raise an error if not found
  print(f"Removed {movie} from watched movies (if present).")

def print_watched_movies():
  """Prints the set of watched movies."""
  if watched_movies:
    print("Watched Movies:")
    for movie in watched_movies:
      print(f"- {movie}")
  else:
    print("No movies watched yet.")


# Example usage
add_to_shopping_list("apples")
add_to_shopping_list("bread")
remove_from_shopping_list("milk")  # Not added yet
print_shopping_list()

add_student_info("name", "Bob")
update_student_info("age", 25)
add_student_info("course", "Mathematics")
print_student_info()

add_watched_movie("The Shawshank Redemption")
add_watched_movie("The Godfather")
remove_watched_movie("The Lord of the Rings")  # Not added yet
print_watched_movies()
