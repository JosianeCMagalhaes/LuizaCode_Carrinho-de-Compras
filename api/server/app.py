from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.server.database import connect_db, disconnect_db
from api.routers import routes_conf

app = FastAPI()

app.add_event_handler('startup', connect_db)
app.add_event_handler('shutdown', disconnect_db)

app.add_middleware( 
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],    
        allow_headers=["*"],
    )

app.include_router(routes_conf.routes)
