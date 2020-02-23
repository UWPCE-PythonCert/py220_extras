"""
* Closure
* Scope
* Curry
* Arity
* Functional Composition
* Itertools

"""
from pymonad import curry

@curry
def db_connect(dbname, user, password):
    # long drawn out code for connection goes here
    print(f"connected to {dbname} with {user} using {password}")


db_connect("postgres", "andy", "1234")

db_connect_pg = db_connect("postgres")
db_connect_pg("fred", "456")

db_connect_mysql = db_connect("mysql")

db_connect_mysql("x", "y")


"""
state global vs local

Closures is a cool CS term for what is really just defining functions
 on the fly with some saved state.
 currying is a special case of closures
 """

