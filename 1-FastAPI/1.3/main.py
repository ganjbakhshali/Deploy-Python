from fastapi import FastAPI , HTTPException, status
import numpy as np
import cv2
import io
from fastapi.responses import StreamingResponse
import uvicorn


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/image/{R}/{G}/{B}")
def image(R: int, G:int, B:int):
    if 0<=R<=255 and 0<=G<=255 and 0<=B<=255:
        im=np.zeros((300,250,3) ,dtype=np.uint8)
        im[:,:]=(R,G,B)
        im=cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
        # cv2.imwrite("test.jpg", im)
        # return {"status": "success", "message": "Image saved as test.jpg"}

        _,Enc_im = cv2.imencode(".png",im)
        return StreamingResponse(io.BytesIO(Enc_im.tobytes()), media_type="image/png")
    else:
        # return {"error": "Invalid RGB values. Must be between 0 and 255."}
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Numbers must be between 0 and 255")
 
if __name__ == "__main__":
    uvicorn.run(app)