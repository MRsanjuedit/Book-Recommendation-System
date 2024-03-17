import pandas as pd

# Read the dataset from the CSV file
file_path = "best-selling-books.csv"
books_data = pd.read_csv(file_path)

# Function to recommend books based on genre
def recommend_books_by_genre(books_data, user_genre):
    # Convert genre column to lowercase for case-insensitive matching
    books_data['Genre'] = books_data['Genre'].str.lower()

    # Drop rows with NaN values in the 'Genre' column
    books_data = books_data.dropna(subset=['Genre'])

    # Filter books based on user-inputted genre
    genre_books = books_data[books_data['Genre'].str.contains(user_genre.lower(), na=False)]

    # Sort books by approximate sales in descending order
    sorted_books = genre_books.sort_values(by='Approximate sales in millions', ascending=False)
    #

    # Return the top recommended book
    if not sorted_books.empty:
        recommended_book = sorted_books.iloc[0]
        return f"The best book in the '{user_genre}' genre is '{recommended_book['Book']}' by {recommended_book['Author']}."
    else:
        return f"No books found in the '{user_genre}' genre."

# Get user input for genre

user_input_genre = input("Enter a genre to get a book recommendation: ")

# Recommend a book based on user input
recommendation = recommend_books_by_genre(books_data, user_input_genre)

# Print the recommendation
print(recommendation)
