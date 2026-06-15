from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

chess_pieces = {
    "pawn": {
        "name": "Pawn",
        "value": 1,
        "movement": "Moves forward one square, but captures diagonally. On its first move, it may move forward two squares.",
        "description": "The pawn is the most numerous chess piece. Although it has the lowest material value, it plays a crucial role in controlling space and supporting other pieces.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/45/Chess_plt45.svg"
    },
    "bishop": {
        "name": "Bishop",
        "value": 3,
        "movement": "Moves diagonally any number of squares.",
        "description": "The bishop is a long-range piece that stays on the same color of square throughout the game. It is especially powerful on open diagonals.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/b/b1/Chess_blt45.svg"
    },
    "knight": {
        "name": "Knight",
        "value": 3,
        "movement": "Moves in an L-shape: two squares in one direction and one square perpendicular. It can jump over other pieces.",
        "description": "The knight is the only chess piece that can jump over other pieces. Its unusual movement makes it excellent for forks and tactical attacks.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/7/70/Chess_nlt45.svg"
    },
    "rook": {
        "name": "Rook",
        "value": 5,
        "movement": "Moves horizontally or vertically any number of squares.",
        "description": "The rook is a powerful long-range piece, especially effective on open files and ranks. It also participates in castling with the king.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/7/72/Chess_rlt45.svg"
    },
    "queen": {
        "name": "Queen",
        "value": 9,
        "movement": "Moves horizontally, vertically, or diagonally any number of squares.",
        "description": "The queen is the most powerful chess piece because it combines the movement abilities of both the rook and the bishop.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/15/Chess_qlt45.svg"
    },
    "king": {
        "name": "King",
        "value": "invaluable",
        "movement": "Moves one square in any direction.",
        "description": "The king is the most important piece in chess. The objective of the game is to checkmate the opponent's king.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/42/Chess_klt45.svg"
    }
}


@app.get("/", response_class=HTMLResponse)
def root(request: Request):

    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"pieces": chess_pieces.keys()}
    )


@app.get("/pieces/{piece_name}", response_class=HTMLResponse)
def get_piece_html(request: Request, piece_name: str):
    piece_name = piece_name.lower()
    if piece_name not in chess_pieces:
        raise HTTPException(status_code=404, detail="Piece not found")
    
    return templates.TemplateResponse(
        request=request, 
        name="piece.html", 
        context={"piece": chess_pieces[piece_name]}
    )


@app.get("/api/pieces/{piece_name}")
def get_piece_json(piece_name: str):
    piece_name = piece_name.lower()
    if piece_name not in chess_pieces:
        raise HTTPException(status_code=404, detail="Piece not found")
    return chess_pieces[piece_name]
