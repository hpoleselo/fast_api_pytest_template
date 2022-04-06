from fastapi import FastAPI, Header, HTTPException, status
from schemas import model

description = """
# FastAPI Project Example

FastAPI project example which tries to follow MVC pattern.

Reference: https://stackoverflow.com/questions/64943693/what-are-the-best-practices-for-structuring-a-fastapi-project

## Side Note

If placing main.py inside an /app directory, one has to read
about setting PYTHONPATH correctly, which leads to this:

`path = 'SET_YOUR_ABSOLUTE_PATH'`
`sys.path.insert(0, path)`

https://stackoverflow.com/questions/31291608/effect-of-using-sys-path-insert0-path-and-sys-pathappend-when-loading-modul


TODO:
* ToDo1
* ToDo2
"""

app = FastAPI(description=description,
              title="FastAPI Example",
              version="0.0.1",
              contact={
                  "name": "Henrique Poleselo",
                  "email": "hpoleselo@example.com"
              },
              license_info={
                  "name": "Apache 2.0",
                  "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
              },
              redoc_url="/redoc",)


@app.post("/insert_data")
async def parse_data(incoming_payload: model.IncomingPayload,
                     x_hub_signature: str = Header(None)
                     #strange_header: Optional[str] = Header(None, convert_underscores=False)
                     #price: float = Field(..., gt=0, description
                    ):
    print(incoming_payload.dict())
    if x_hub_signature is None:
        print("Payload is not from GitHub as it doesn't contain X-Hub-Signature.")
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Payload is not from GitHub as it doesn't contain X-Hub-Signature.")
    
    # Otherwise it will return a 200 along with this dictionary.
    return {"detail": "Successfull"}

@app.get("/data")
async def read_main():
    return {"msg": "Hello World"}