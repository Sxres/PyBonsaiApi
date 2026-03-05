from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import io, re, sys
from unittest.mock import patch, MagicMock
import random

if sys.platform == "win32":
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:4173", "https://dragossorescu.vercel.app", "https://sxres.dev"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

ANSI_ESCAPE = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

def strip_ansi(text: str) -> str:
    return ANSI_ESCAPE.sub('', text)

def make_terminal_size(w=100, h=40):
    ts = MagicMock()
    ts.columns = w
    ts.lines = h
    ts.__iter__ = lambda self: iter((w, h))
    return ts

@app.get("/tree/instant")
def instant_tree():
    captured = io.StringIO()
    tree_type = random.choice([0, 1, 2])
    
    with patch("shutil.get_terminal_size", return_value=make_terminal_size()):
        with patch("pybonsai.__main__.get_terminal_size", return_value=make_terminal_size()):
            with patch("sys.stdout", captured):
                try:
                    from pybonsai.__main__ import main
                    sys.argv = ["pybonsai", "-i", "-x", "100", "-y", "40", "-t", str(tree_type)]
                    main()
                except SystemExit:
                    pass
                except Exception as e:
                    return {"tree": "", "error": str(e)}

    return {"tree": strip_ansi(captured.getvalue())}