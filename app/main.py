from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import contracts, contract_source, chat, licensing

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(contracts.router)
app.include_router(contract_source.router)
app.include_router(chat.router)
app.include_router(licensing.router)