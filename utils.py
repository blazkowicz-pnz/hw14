import sqlite3

def search_by_title(film):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""SELECT `title`, `country`, `release_year`, `listed_in`, `description` 
                   FROM netflix
                   WHERE `title` != '' AND `title` = '{film}'
                   ORDER BY `release_year` 
                   LIMIT 1
               
               """

        cursor.execute(query)
        execute_query = cursor.fetchall()
        if len(execute_query) > 0:
            result_dict = {
                "title": execute_query[0][0],
                "country": execute_query[0][1],
	        	"release_year": execute_query[0][2],
		        "genre": execute_query[0][3],
		        "description": execute_query[0][4].replace("\n", "")
            }
            return result_dict

        else:
            return "film not found"

print(search_by_title("Spelling the Dream"))
