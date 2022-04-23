import sqlite3


def sqlite3_connection(query):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        # query = query
        result = cursor.execute(query)
        return result.fetchall()


def search_by_title(film):
    query = f"""SELECT `title`, `country`, `release_year`, `listed_in`, `description` 
                   FROM netflix
                   WHERE `title` != '' AND `title` = '{film}'
                   ORDER BY `release_year` 
                   LIMIT 1
               
               """
    result = sqlite3_connection(query)
    if len(result) > 0:
        result_dict = {
            "title": result[0][0],
            "country": result[0][1],
            "release_year": result[0][2],
            "genre": result[0][3],
            "description": result[0][4].replace("\n", "")
        }
        return result_dict

    else:
        return "film not found"


def search_by_release_year(start_year, stop_year):
    query = f"""SELECT `title`, `release_year`, `rating` 
                FROM netflix
                WHERE `release_year` BETWEEN {start_year} AND {stop_year}
                ORDER BY `release_year`
                LIMIT 100
        
    """
    result = sqlite3_connection(query)
    films_list = []
    film_dict = {}
    for film in result:
        film_dict["title"] = film[0]
        film_dict["release_year"] = film[1]
        film_dict["rating"] = film[2]
        films_list.append(film_dict)
        film_dict = {}
    return films_list


def search_by_rating(rating):
    rating_dict = {"children": ("G", ""), "family": ("G", "PG", "PG-13"), "adult": ("R", "NC-17")}
    query = f"""SELECT `title`, `rating`, `description`
                FROM netflix
                WHERE `rating` IN {rating_dict[str(rating)]}
                ORDER BY `title`
                LIMIT 100
        
    """
    result = sqlite3_connection(query)
    films_list = []
    film_dict = {}
    for film in result:
        film_dict["title"] = film[0]
        film_dict["rating"] = film[1]
        film_dict["description"] = film[2].replace("\n", "")
        films_list.append(film_dict)
        film_dict = {}
    return films_list


def search_by_genre(genre):
    query = f"""SELECT `title`, `description`, `release_year`
                FROM netflix
                WHERE `listed_in` LIKE "%{genre}%"
                ORDER BY `release_year` DESC 
                LIMIT 10
                
    """
    result = sqlite3_connection(query)
    film_list = []
    film_dict = {}
    for film in result:
        film_dict["title"] = film[0]
        film_dict["description"] = film[1].replace("\n", "")
        film_dict["release_year"] = film[2]
        film_list.append(film_dict)
        film_dict = {}
    return film_list


def search_actors(actor_1, actor_2):
    query = f"""SELECT netflix.cast 
                FROM netflix
                WHERE netflix.cast LIKE "%{actor_1}%" AND netflix.cast LIKE "%{actor_2}%"
                LIMIT 10
                
    
    """
    result = sqlite3_connection(query)
    actors_all = []
    actors_list = []
    for actor in result:
        actors_all.extend(actor[0].split(", "))
    for man in actors_all:
        if man not in [actor_1, actor_2]:
            if actors_all.count(man) > 2:
                actors_list.append(man)
    return set(actors_list)


# print(search_actors("Jack Black", "Dustin Hoffman"))


def search_films(type_film, year, genre):
    query = f"""
            SELECT `title`, `description`
            FROM netflix
            WHERE netflix.type = "{type_film}" AND `release_year` = {year} AND `listed_in` LIKE "%{genre}%"
            LIMIT 10
    """
    result = sqlite3_connection(query)
    film_list = []
    for film in result:
        film_list.append(
            {
                "title": film[0],
                "description": film[1].strip()
            }
        )
    return film_list

# print(search_films("Movie", 2000, "horror"))






