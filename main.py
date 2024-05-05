import psycopg2

data_base = psycopg2.connect(
    host = "rain.db.elephantsql.com",
    user = "nytuuwcr",
    database = "nytuuwcr",
    password = "c2YdLmGam_80_0Vot_QbL4P2VpOePmiT"
)
cursor = data_base.cursor()

