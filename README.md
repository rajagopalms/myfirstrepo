# AI Agent Workshop: Day 1 starter kit

Goal for today: call a free AI model from Python and see the answer and how many tokens it used.
Time: about 2 hours (1 hour reading the concepts section of the plan, 1 hour on these steps).

## 1. Create the repo (5 min)

1. On GitHub, create a new **public** repo, for example `ai-agent-workshop` (public repos get free Actions minutes).
2. Copy every file from this kit into it, keeping the folders, and push.

## 2. Get a GitHub token for the models (5 min)

1. GitHub → Settings → Developer settings → Personal access tokens → **Fine-grained tokens** → Generate new token.
2. Name it `ai-workshop`, expiry 30 days, and under **Account permissions** set **Models** to **Read-only**. Nothing else.
3. Copy the token. Treat it like a password.

## 3. Try the playground first (10 min)

Open https://github.com/marketplace/models, pick a small chat model (for example GPT-4.1 mini), and ask it:
"Explain this GitHub Actions error and suggest a fix: `npm ERR! code ETIMEDOUT`".
Change the system prompt and temperature, and see how the answer changes.

## 4. Run it from Python (20 min)

```bash
git clone https://github.com/<you>/ai-agent-workshop.git
cd ai-agent-workshop
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # Windows: copy .env.example .env
# edit .env and paste your token after GITHUB_TOKEN=
python day01/hello_model.py "In 3 sentences: what is an LLM, in DevOps terms?"
```

## 5. Experiments (20 min)

Edit `day01/hello_model.py` and run it again after each change:

- `temperature=0.2` → `1.0`: answers become more varied.
- `max_tokens=400` → `40`: the answer gets cut off. That is the token limit in action.
- Change `SYSTEM_PROMPT` to "Answer only in JSON with keys cause and fix". This is a preview of day 3.
- Paste a real failed Actions log line as the question.

## Done when

The script prints an answer and a line like `tokens in: 52 | out: 118 | total: 170`.

## If it fails

- `401` or `Unauthorized`: the token is missing the Models read permission, or `.env` is not in the folder you ran from.
- `429` or `RateLimitReached`: the free tier limit was hit. Wait a minute, or switch `MODEL_NAME` to another small model.
- `model not found`: copy the exact model name from the model's page in the GitHub Models catalog into `MODEL_NAME`.

Paste any error into the workshop thread and we'll fix it together.
