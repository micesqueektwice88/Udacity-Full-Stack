import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "Marine on a crazy planet",
                     "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")
#print(avatar.storyline)
#avatar.show_trailer()

Dredd = media.Movie("Dredd",
                    "Dystopian future",
                    "https://en.wikipedia.org/wiki/Dredd#/media/File:Dredd2012Poster.jpg",
                    "https://www.youtube.com/watch?v=qVIba2N6MTA")

#print (Dredd.storyline)
#Dredd.show_trailer()

Sicario = media.Movie("Sicario",
                      "Cartel Hitman",
                      "https://en.wikipedia.org/wiki/Sicario_(2015_film)#/media/File:Sicario_poster.jpg",
                      "https://www.youtube.com/watch?v=sR0SDT2GeFg")

Interstellar = media.Movie ("Interstellar",
                            "Alright alright alright",
                            "https://en.wikipedia.org/wiki/Interstellar_(film)#/media/File:Interstellar_film_poster.jpg",
                            "https://www.youtube.com/watch?v=0vxOhd4qlnA")

Fury = media.Movie ("Fury",
                    "Tank Crew",
                    "https://en.wikipedia.org/wiki/Fury_(2014_film)#/media/File:Fury_2014_poster.jpg",
                    "https://www.youtube.com/watch?v=-OGvZoIrXpg")

movies = [toy_story, avatar, Dredd, Sicario, Interstellar, Fury]
#fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.VARIOUS_RATINGS)
print (media.Movie.__module__)

#THis note has been added as a GItHub upload test

