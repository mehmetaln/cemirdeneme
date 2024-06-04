from cemirutils import CemirUtils

# listem = [1,2,3,4,5,6,7]
# utils = CemirUtils(listem)
# asd = utils.list_head(5)
# asd = utils.list_sort_asc()
# asd = utils.list_sum_values()

utils = CemirUtils(data=None, dbname="testdb", dbuser="postgres", dbpassword="159753", dbhost='localhost', dbport=5432, timeout=3, dbcreate_db_if_not_exists=False)

# asd = utils.psql_create_table("testtable","id SERIAL PRIMARY KEY, name VARCHAR(100), data JSONB")
asd = utils.psql_insert("testtable",("id", "name", "data"),(1, "John Doe", {"age": 30, "city": "Istanbul"}))

asd = utils.psql_read("testtable")
print(asd)

