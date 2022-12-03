import os

import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request

# 실행경로가 다르더라도 정확한 주소를 받기 위해 사용
main_dir = os.path.dirname(__file__)

app = FastAPI()

# 템플릿과 스태틱 파일 가져오기
templates = Jinja2Templates(directory=f"{main_dir}/templates")
app.mount(
    "/static", StaticFiles(directory=f"{main_dir}/static"), name="static")


@app.get("/")
async def test(request: Request):
    return templates.TemplateResponse("test.html", {"request": request, "data": "테스트"})

# 패키지 경로를 정확히 하기 위해서 아래방식으로 실행
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)