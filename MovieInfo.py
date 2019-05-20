import Movies
import fresh_tomatoes

# create a new movie and init function gets called through Movies.Movie from class(Movie) and access all information
# of movie
captain_america = Movies.Movie("Captain America: The First Avenger",
                               "Predominantly set during World War II, Steve Rogers is a sickly man from Brooklyn "
                               "who's transformed into super-soldier Captain America to aid in the war effort. Rogers "
                               "must stop the Red Skull – Adolf Hitler's ruthless head of weaponry, and the leader of "
                               "an organization that intends to use a mysterious device of untold powers for world "
                               "domination.",
                               "http://www.movienewsletters.net/photos/277218R1.jpg",
                               "https://www.youtube.com/watch?v=JerVrbLldXw")

# second movie
the_avengers = Movies.Movie("The avengers",
                            "When an unexpected enemy emerges and threatens global safety and security, Nick Fury, "
                            "director of the international peacekeeping agency known as S.H.I.E.L.D., finds himself in "
                            "need of a team to pull the world back from the brink of disaster. Spanning the globe, "
                            "a daring recruitment effort begins!",
                            "http://www.movienewsletters.net/photos/130835R1.jpg",
                            "https://www.youtube.com/watch?v=eOrNdBpGMv8")

# third movie
doctor_strange = Movies.Movie("Doctor strange",
                              "After his career is destroyed, a brilliant but arrogant surgeon gets a new lease on "
                              "life when a sorcerer takes him under her wing and trains him to defend the world "
                              "against evil.",
                              "https://contentserver.com.au/assets/491602_p11214341_p_v8_ap.jpg",
                              "https://www.youtube.com/watch?v=HSzx-zryEgM")

# forth movie
thor_ragnorok = Movies.Movie("Thor: Ragnarok",
                             "Thor is on the other side of the universe and finds himself in a race against time to "
                             "get back to Asgard to stop Ragnarok, the prophecy of destruction to his homeworld and "
                             "the end of Asgardian civilization, at the hands of an all-powerful new threat, "
                             "the ruthless Hela.",
                             "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",
                             "https://www.youtube.com/watch?v=ue80QwXMRHg")

# adding the movie names into list of array called movies
movies = [captain_america, the_avengers, doctor_strange, thor_ragnorok]
# use the fresh tomatoes file and as argument(movies) is being passed to function(open_movies_page)
# the calling of that function takes in list of array as above
fresh_tomatoes.open_movies_page(movies)
