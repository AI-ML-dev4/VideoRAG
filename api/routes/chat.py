from fastapi import APIRouter, Request, Response
from pydantic import BaseModel
import uuid
from rag.llm import ask_rag

router = APIRouter()


class ChatRequest(BaseModel):
    query: str
    video_name: str
  



@router.post("/chat")
def chat(rq: ChatRequest,request:Request,response:Response):

    session_id = request.cookies.get("session_id")

    if not session_id:
        session_id = str(uuid.uuid4())
        response.set_cookie(key="session_id", value=session_id)

    answer = ask_rag(rq.query, rq.video_name, session_id)

    return {
        "answer": answer
    }