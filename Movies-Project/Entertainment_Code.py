import media
import fresh_tomatoes

Blade_runner = media.Movie("Blade_runner",
                           "Detective that hunts androids",
                           "https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg",
                           "https://www.youtube.com/watch?v=eogpIG53Cis")
#print Blade_runner.storyline

Dredd = media.Movie("Dredd",
                    "Crazy future cop",
                    "https://en.wikipedia.org/wiki/Dredd#/media/File:Dredd2012Poster.jpg",
                    "https://www.youtube.com/watch?v=G-eI5oLlIeY")

Requiem_for_a_Dream = media.Movie("Requim for a Dream",
                                  "Heroin Addicts",
                                  "https://en.wikipedia.org/wiki/Requiem_for_a_Dream",
                                  "https://www.youtube.com/watch?v=yVIRcnlRKF8")

Lord_of_War = media.Movie("Lord of War",
                          "Firearm dealers",
                          "https://en.wikipedia.org/wiki/Lord_of_War#/media/File:Lordofwar.jpg",
                          "https://www.youtube.com/watch?v=38vd_j7e2HY")

Final_Project_Udacity = [Blade_runner, Dredd, Requiem_for_a_Dream, Lord_of_War]

#print (media.Movie.__module__)
