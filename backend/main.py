# from fastapi import FastAPI, UploadFile, Form
# from fastapi.middleware.cors import CORSMiddleware
# from image_analyzer import analyze_image
# from stylist_llm import generate_styling_advice
# from trend_engine import get_trends
# from schemas import ChatRequest

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.post("/recommend")
# async def recommend(
#     image: UploadFile,
#     occasion: str = Form(...),
#     style: str = Form(...)
# ):
#     image_data = analyze_image(image)
#     trends = get_trends()

#     advice = generate_styling_advice(
#         image_data, occasion, style, trends
#     )

#     return {"advice": advice}


# @app.post("/chat")
# async def chat(req: ChatRequest):
#     reply = f"Yes, based on your outfit and context, {req.question.lower()} — it should work well."
#     return {"reply": reply}
from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from image_analyzer import analyze_image
from stylist_llm import generate_styling_advice
from trend_engine import get_trends
from schemas import ChatRequest

app = FastAPI()

origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "StyleSense Backend is running 🚀"}

@app.post("/recommend")
async def recommend(
    image: UploadFile,
    occasion: str = Form(...),
    style: str = Form(...)
):
    image_data = analyze_image(image)
    trends = get_trends()

    advice = generate_styling_advice(
        image_data, occasion, style, trends
    )

    return {"advice": advice}

@app.post("/chat")
async def chat(req: ChatRequest):
    reply = f"Yes, based on your outfit and context, {req.question.lower()} — it should work well."
    return {"reply": reply}
