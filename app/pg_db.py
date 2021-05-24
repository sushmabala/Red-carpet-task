import databases, sqlalchemy
Db_URL="postgresql://username:password@db:5432/nudges"
database=databases.Database(Db_URL)
metadata=sqlalchemy.MetaData()
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("username"  , sqlalchemy.String,unique=True),
    sqlalchemy.Column("password"  , sqlalchemy.String),
    sqlalchemy.Column("role", sqlalchemy.String),
    sqlalchemy.Column("token", sqlalchemy.String),
    sqlalchemy.Column("create_at", sqlalchemy.String),
)

relation = sqlalchemy.Table(
    "relation",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("agent_username"  , sqlalchemy.String),
    sqlalchemy.Column("customer_username"  , sqlalchemy.String),
    sqlalchemy.Column("create_at", sqlalchemy.String),
)
loan = sqlalchemy.Table(
    "loan",
    metadata,
    sqlalchemy.Column("id" , sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("agent_username"  , sqlalchemy.String),
    sqlalchemy.Column("customer_username"  , sqlalchemy.String),
    sqlalchemy.Column("create_at", sqlalchemy.String),
    sqlalchemy.Column("amount",sqlalchemy.INT),
    sqlalchemy.Column("duration",sqlalchemy.INT),
    sqlalchemy.Column("mandatory_requirement1",sqlalchemy.String),
    sqlalchemy.Column("mandatory_requirement2",sqlalchemy.String),
    sqlalchemy.Column("emi_chosen",sqlalchemy.Boolean),
    sqlalchemy.Column("status",sqlalchemy.String)
)
engine = sqlalchemy.create_engine(
    Db_URL
)
metadata.create_all(engine)
