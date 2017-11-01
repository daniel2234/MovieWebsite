import fresh_tomatoes
import media

# Every instance of a movie class is created
a_space_odyessey= media.Movie("2001: A Space Odyssey",
                             "The film follows a voyage to Jupiter with the sentient computer Hal after the discovery of a mysterious black monolith affecting human evolution.",
                             "http://t0.gstatic.com/images?q=tbn:ANd9GcQdmmLZ7lXsw1WRy7c5qN3mka2e9ANSpHIG2INi53P6OVS8KyJo",
                             "https://www.youtube.com/watch?v=XHjIqQBsPjk")

alien = media.Movie("Alien",
                    "In deep space, the crew of the commercial starship Nostromo is awakened from their cryo-sleep capsules halfway through their journey home to investigate a distress call from an alien vessel.",
                    "http://t2.gstatic.com/images?q=tbn:ANd9GcRGWyg4tnCNzaiUna7JSzV3I8NcwMaFhpulr1iWSd0FwW-r_89e", 
                    "https://www.youtube.com/watch?v=bEVY_lonKf4")

blade_runner = media.Movie("Blade Runner",
                        "Deckard is forced by the police Boss to continue his old job as Replicant Hunter.",
                        "http://t3.gstatic.com/images?q=tbn:ANd9GcTcvek3p12Gwqwk-2wjTSHWTNq0LTTeoOgXUwqerVOY2u9zjOgO",
                        "https://www.youtube.com/watch?v=eogpIG53Cis");

the_spy_who_loved_me= media.Movie("The Spy Who Loved Me",
                                   "British super-spy James Bond (Roger Moore) unites with sexy Russian agent Anya Amasova (Barbara Bach) to defeat megalomaniac shipping magnate Karl Stromberg.", 
                                   "http://t0.gstatic.com/images?q=tbn:ANd9GcQ7gsZxPkAPySXQitJiBE2eusPjcYQmFcSwcVBWRBNMTxcIOBUp", 
                                   "https://www.youtube.com/watch?v=UBxG_TJvYTg")

superman = media.Movie("Superman", 
                        "Just before the destruction of the planet Krypton, scientist Jor-El (Marlon Brando) sends his infant son Kal-El on a spaceship to Earth.", 
                        "http://t2.gstatic.com/images?q=tbn:ANd9GcSBymxrwRWv7EE3whu1s3PqAptCNZ4RYq7jPX78bLQba8DSvVXc", 
                        "https://www.youtube.com/watch?v=XWHyvubVdPA")

the_hit= media.Movie("The Hit",
                       "Willie Parker gives evidence against his criminal compatriots in return for a very generous offer from the police.", 
                       "http://www.gstatic.com/tv/thumb/movieposters/8839/p8839_p_v8_aa.jpg", 
                       "https://www.youtube.com/watch?v=Vmty5rt-yF8")

angry_men = media.Movie("12 Angry Men",
                      "A jury holdout attempts to prevent a miscarriage of justice by forcing his colleagues to reconsider the evidence.", 
                      "http://t1.gstatic.com/images?q=tbn:ANd9GcQuhFZT3lQfr0vDy4XWMHQ8X93FWuamEuw_5iB4dmOTxc_w79rA", 
                      "https://www.youtube.com/watch?v=A7CBKT0PWFA")

the_thin_red_line= media.Movie("The Thin Red Line",
                      "Adaptation of James Jones' autobiographical 1962 novel, focusing on the conflict at Guadalcanal during the second World War.", 
                      "http://www.gstatic.com/tv/thumb/movieposters/22250/p22250_p_v8_ag.jpg", 
                      "https://www.youtube.com/watch?v=LCmlOhsIwBk")

dr_mabuses_testmente= media.Movie("The Testament of Dr. Mabuse",
                      "A new crime wave grips the city and all clues seem to lead to the nefarious Dr. Mabuse, even though he has been imprisoned in a mental asylum for nearly a decade.", 
                      "https://upload.wikimedia.org/wikipedia/en/d/d4/TestamentOfDrMabuse-Poster.jpg", 
                      "https://www.youtube.com/watch?v=n-WnY_ZmT9E")

bad_timing= media.Movie("Bad Timing",
                      "A psychiatrist living in Vienna enters a torrid relationship with a married woman. When she ends up in the hospital from an overdose, an inspector becomes set on discovering the demise of their affair.", 
                      "http://c8.alamy.com/comp/DXJ436/bad-timing-DXJ436.jpg", 
                      "https://www.youtube.com/watch?v=LC-asNConRk")

merry_christmas_mr_lawrence= media.Movie("Merry Christmas Mr. Lawrence",
                      "During WWII, a British colonel tries to bridge the cultural divides between a British POW and the Japanese camp commander in order to avoid bloodshed.", 
                      "http://www.gstatic.com/tv/thumb/dvdboxart/7713/p7713_d_v8_aa.jpg", 
                      "https://www.youtube.com/watch?v=YHRPwjpH6tM")

for_all_mankind=media.Movie("For All Mankind",
                            "An in-depth look at various NASA moon landing missions, starting with Apollo 8.",
                            "http://www.gstatic.com/tv/thumb/dvdboxart/51078/p51078_d_v8_aa.jpg", 
                            "https://www.youtube.com/watch?v=aTP-f8Hpu6g")

koyaanisqatsi = media.Movie("Koyaanisqatsi",
                            "A collection of expertly photographed phenomena with no conventional plot. The footage focuses on nature, humanity and the relationship between them.",
                            "http://www.gstatic.com/tv/thumb/dvdboxart/8176/p8176_d_v8_aa.jpg",
                            "https://www.youtube.com/watch?v=PirH8PADDgQ")

greed = media.Movie("Greed",
                    "The sudden fortune won from a lottery fans such destructive greed that it ruins the lives of the three people involved.",
                    "https://upload.wikimedia.org/wikipedia/commons/2/27/Greed3.jpg",
                    "https://www.youtube.com/watch?v=UWLUxuoLFvo")

# This python list shows all the instances of the movie class
movies = [a_space_odyessey, alien, blade_runner, the_spy_who_loved_me,superman, the_hit, angry_men, the_thin_red_line, dr_mabuses_testmente, bad_timing, merry_christmas_mr_lawrence, for_all_mankind, koyaanisqatsi, greed]

#this method renders the movie website and movie tiles
fresh_tomatoes.open_movies_page(movies)