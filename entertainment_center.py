import media
import fresh_tomatoes


"""
declare movies, with 4 args each:
movie_title (movie's title)
movie_storyline (year movie was released)
movie_poster (url to poster image)
movie_trailer (url to youtube trailer)
"""

scent_of_a_woman = media.Movie(
    "Scent of a Woman",
    "A prep school student needing money agrees to babysit a blind man,"
    " but the job is not at all what he anticipated.",
    "https://upload.wikimedia.org/wikipedia/en/9/91/Scent_of_a_Woman.jpg",
    "https://www.youtube.com/watch?v=ebDO0C-RTpU")


beautiful_mind = media.Movie(
    "A Beautiful Mind",
    "After John Nash, a brilliant but asocial mathematician, accepts secret"
    " work in cryptography, his life takes a turn for the nightmarish.",
    "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=nIR3wj9Ssaw")

the_pursuit_of_happyness = media.Movie(
    "The Pursuit of Happyness",
    "A struggling salesman takes custody of his son as he's poised to begin a"
    "life-changing professional endeavor.",
    "http://www.impawards.com/2006/posters/pursuit_of_happyness.jpg",
    "https://www.youtube.com/watch?v=89Kq8SDyvfg")

wild = media.Movie(
    "Wild",
    "A chronicle of one woman's 1,100-mile solo hike undertaken as a way to"
    "recover from a recent personal tragedy.",
    "https://www.pcta.org/wp-content/uploads/2014/07/WILD_movie_poster.jpg",
    "https://www.youtube.com/watch?v=tn2-GSqPyl0")


unbroken = media.Movie(
    "Unbroken",
    "After a near-fatal plane crash in WWII, Olympian Louis Zamperini spends "
    "a harrowing 47 days in a raft with two fellow crewmen before he's caught"
    "by the Japanese navy and sent to a prisoner-of-war camp.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY3ODg2OTgyOF5BMl5BanBnXkFtZTgwODk1OTAwMzE@._V1_UY1200_CR64,0,630,1200_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=kk1M_HwmFMM"
)

eat_pray_love = media.Movie(
    "Eat Pray Love",
    "A married woman realizes how unhappy her marriage really is, "
    "and that her life needs to go in a different direction."
    "After a painful divorce, she takes off on a round-the-world journey to "
    "find herself.",
    "https://upload.wikimedia.org/wikipedia/en/7/7e/Eat_pray_love_ver2.jpg",
    "https://www.youtube.com/watch?v=mjay5vgIwt4")


the_intern = media.Movie(
    "The Intern",
    "70-year-old widower Ben Whittaker has discovered that retirement isn't"
    "all it's cracked up to be.Seizing an opportunity to get back in the game,"
    " he becomes a senior intern at an online fashion site,"
    "founded and run by Jules Ostin.",
    "https://s-media-cache-ak0.pinimg.com/originals/4c/09/1c/4c091cf615a3f79ef79047c76223f769.jpg",  # NOQA
    "https://www.youtube.com/watch?v=W-DEy3mylCs")


mr_church = media.Movie(
    "Mr. Church",
    "Mr. Church tells the story of a unique friendship that develops when a "
    "little girl and her dying mother retain the services of a talented cook "
    "- Henry Joseph Church. What begins as a six month arrangement instead "
    "spans into fifteen years and creates a family bond that lasts forever.",
    "http://www.indiewire.com/wp-content/uploads/2016/04/mr-church.jpg",
    "https://www.youtube.com/watch?v=wySiVNV71IQ")

manchester_by_the_sea = media.Movie(
    "Manchester by the Sea",
    "A depressed uncle is asked to take care of his teenage nephew after "
    "the boy's father dies.",
    "http://www.impawards.com/2016/posters/manchester_by_the_sea.jpg",
    "https://www.youtube.com/watch?v=gsVoD0pTge0")

lala_land = media.Movie(
    "La La Land",
    "A jazz pianist falls for an aspiring actress in Los Angeles.",
    "https://d35fkdjhhgt99.cloudfront.net/static/use-media-items/48/47382/full-1382x2048/587a5198/1.jpeg?resolution=0",  # NOQA
    "https://www.youtube.com/watch?v=0pdqf4P9MB8")


hacksaw_ridge = media.Movie(
    "Hacksaw Ridge",
    "WWII American Army Medic Desmond T. Doss, who served during the Battle"
    " of Okinawa, refuses to kill people, and becomes the first man in"
    " American history to receive the Medal of Honor without firing a shot.",
    "http://cdn3-www.comingsoon.net/assets/uploads/gallery/hacksaw-ridge/hacksaw0001.jpg",  # NOQA
    "https://www.youtube.com/watch?v=s2-1hz1juBI")

fences = media.Movie(
    "Fences",
    "A working-class African-American father tries to raise his family in"
    "the 1950s, while coming to terms with the events of his life.",
    "http://cdn2-www.comingsoon.net/assets/uploads/gallery/fences/fences.jpg",
    "https://www.youtube.com/watch?v=a2m6Jvp0bUw")

# assign individual movies to movies array
movies = [
    scent_of_a_woman,
    beautiful_mind,
    the_pursuit_of_happyness,
    eat_pray_love,
    wild,
    unbroken,
    the_intern,
    mr_church,
    lala_land,
    manchester_by_the_sea,
    hacksaw_ridge,
    fences]

# call movie trailer page method and pass movies array

fresh_tomatoes.open_movies_page(movies)
