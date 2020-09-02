import strategies
import generator2
import queries

strategies.DumbStrategy(
    login_generator = generator2.LoginGenerator(),
    password_generator = generator2.PopularStringGenerator(),
    query = queries
)

