# degrees

This project is part of Introduction to AI course on Edx

Using breadth first search, finding shortest path from source actor name to target actor name giving a path of movies the connecting actors starred in. 

The path looks as follows:
[(person_id1), (movie_id2, person_id2).....(movie_idn, person_idn)] 

where person_id1 is source and person_idn is target. It means that person_id1 starred in movie_id2 with person_id2, person_id2 starred in movie_id3 with person_id3 and so on. 
The dataset is in csv format. It consists of 3 csv files namely: stars.csv, movies.csv, people.csv.

util.py contains stack and queue frontiers
degrees.py contains the main search algorithm of breadth first search

