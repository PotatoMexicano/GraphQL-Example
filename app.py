import uvicorn
import strawberry
from Models import Query
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

schema = strawberry.Schema(query=Query)


graphql_app = GraphQLRouter(schema)
app = FastAPI()

app.include_router(graphql_app, prefix="/graphql")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)