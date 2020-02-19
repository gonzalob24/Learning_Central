# some examples from the book
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta")

print(julia[0:1])

(name, surname, b_year, movie, m_year, profession, b_place) = julia

print(name)

students = [
    ("John", ["CompSci", "Physics"]),
    ("Vusi", ["Maths", "CompSci", "Stats"]),
    ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
    ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
    ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]


julia_more_info = (("Julia", "Roberts"), (8, "October", 1967),
                   "Actress", ("Atlanta", "Georgia"),
                   [("Duplicity", 2009),
                    ("Notting Hill", 1999),
                    ("Pretty Woman", 1990),
                    ("Erin Brockovich", 2000),
                    ("Eat Pray Love", 2010),
                    ("Mona Lisa Smile", 2003),
                    ("Oceans Twelve", 2004)])

print(julia_more_info[4][2])
