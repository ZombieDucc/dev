from quart import Quart, jsonify, request
import random
word_list=["ye", "frank ocean", "drake", "MF DOOM", "kendrick lamar" ]

app = Quart(__name__)

@app.get("/health")
async def health():
    return jsonify({"status": "ok"})

@app.get("/api/v1/random")
async def get_random():
    return jsonify({"value": random.randint(1, 100), "min": 1, "max": 100})

@app.post("/api/v1/reverse")
async def post_reverse():
    data = await request.get_json()
    num = data.get("number", 0)
    return jsonify({"original": num, "reversed": int(str(num)[::-1])})

@app.post("/artists")
async def get_artist():
    return jsonify({"value":random.choice(word_list)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
