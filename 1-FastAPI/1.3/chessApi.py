from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from typing import List


app = FastAPI(
    title="Chess Pieces API",
    description="An API that provides information and images for the six standard chess pieces.",
    version="1.0.0"
)


class Piece(BaseModel):
    name: str
    value: int | str
    movement: str
    description: str
    image_url: str


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


@app.get("/")
def root():
    return {
        "message": (
            "Welcome to the Chess Pieces API. "
            "This API provides information about the six standard chess pieces: "
            "pawn, bishop, knight, rook, queen, and king. "
            "You can get a list of all pieces, detailed information about each piece, "
            "and an image for any specific chess piece."
        ),
        "docs": "/docs",
        "available_endpoints": [
            "/pieces",
            "/pieces/{piece_name}",
            "/pieces/{piece_name}/image"
        ]
    }


@app.get("/pieces", response_model=List[str])
def get_all_pieces():
    return list(chess_pieces.keys())


@app.get("/pieces/{piece_name}", response_model=Piece)
def get_piece(piece_name: str):
    piece_name = piece_name.lower()

    if piece_name not in chess_pieces:
        raise HTTPException(
            status_code=404,
            detail=f"Piece '{piece_name}' not found. Available pieces are: pawn, bishop, knight, rook, queen, king."
        )

    return chess_pieces[piece_name]


@app.get("/pieces/{piece_name}/image")
def get_piece_image(piece_name: str):
    piece_name = piece_name.lower()

    if piece_name not in chess_pieces:
        raise HTTPException(
            status_code=404,
            detail=f"Image for piece '{piece_name}' not found. Available pieces are: pawn, bishop, knight, rook, queen, king."
        )

    return RedirectResponse(url=chess_pieces[piece_name]["image_url"])
