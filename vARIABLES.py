# 1. Store the book's basic details in separate variables.
book_title = "The Hobbit"
page_count = 310
is_finished = False

# 2. Keep three favorite genres in a list, then add a fourth.
favorite_genres = ["fantasy", "adventure", "mystery"]
favorite_genres.append("science fiction")

# 3. Group the book details in a dictionary and print selected values.
book_details = {
    "title": book_title,
    "pages": page_count,
    "finished": is_finished,
}

print("Book title:", book_details["title"])
print("Page count:", book_details["pages"])
print("Favorite genres:", favorite_genres)

# 4. Store the publication year and edition number in an immutable tuple.
publication_info = (1937, 1)
print("Publication year and edition:", publication_info)

# 5. Print the type of each separate book variable.
print("Type of book_title:", type(book_title))
print("Type of page_count:", type(page_count))
print("Type of is_finished:", type(is_finished))