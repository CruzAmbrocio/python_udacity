import fresh_tomatoes
import media

toy_story = media.Movie(
    "Toy Story",
    "A story of a body and his toys that come to life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=vwyZH85NQC4"
    )
#print(toy_story.storyline)
avatar=media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
    "http://www.youtube.com/watch?v=-9ceBgWV8io"
    )
#print(avatar.storyline)
#avatar.show_trailer()
school_of_rock=media.Movie(
    "school_of_rock",
    "Using rock music to learn",
    "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?=3PsUJFEBC74"
    )
ratatouille=media.Movie(
    "Ratatouille",
    "A rat is a chef in Paris",
    "http://upload.wikimedia.org/wikipedia/en/5/0/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk"
    )
movies=[toy_story,avatar,school_of_rock, ratatouille]
fresh_tomatoes.open_movies_page(movies)