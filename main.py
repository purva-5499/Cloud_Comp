from fastapi import FASTAPI 
app=FASTAPI()
@app.get(*/home*)
def home():
    return {
        "success":True, "message":"Hello World!"
    }

@app.get("/home")