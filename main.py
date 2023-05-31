from fastapi import *
from fastapi.responses import *
import uvicorn

app=FastAPI()

@app.get("/report")
async def get_report():
    f=open("./reports/report.html","r")
    resp_str=f.read()
    f.close()
    return HTMLResponse(content=resp_str)


if __name__=="__main__":
    server=uvicorn.Server( config=uvicorn.Config(app=app, host="0.0.0.0",port=8088))
    server.run()