# Africa's Talking sandbox SMS

This project sends one SMS with the [Africa's Talking](https://africastalking.com/) Python SDK. It uses the sandbox, so messages stay in the test environment and do not go out to a live phone network.

The sandbox username is always `sandbox`. The API key must come from the sandbox app. A key from a live app will be rejected.

## 1. Open the sandbox

1. Create an account at [account.africastalking.com](https://account.africastalking.com/).
2. Log in and click the orange **Go To Sandbox App** button. You can also open [the sandbox app](https://account.africastalking.com/apps/sandbox) directly.
3. In the left menu, open **Settings**, then **API Key**.
4. Enter your password and click **Generate**.
5. Copy the key immediately. The dashboard shows it only once.

Wait a few minutes before using a new key. Africa's Talking says about 3 minutes; a new key can take up to 20 minutes to start working. Generating another key turns the previous one off.

## 2. Install the project

Python 3 is required. From this folder:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` installs `africastalking` and `python-dotenv`.

## 3. Add the sandbox credentials

```bash
cp .env.example .env
```

Edit `.env`:

```bash
AT_USERNAME=sandbox
AT_API_KEY=your_sandbox_api_key
```

Leave `AT_USERNAME` as `sandbox`. Paste the key from the sandbox app into `AT_API_KEY`. `.env` is listed in `.gitignore`, so the key stays off git.

## 4. Set the test number

In `main.py`, set `recipients` to the number you want to test, in international format:

```python
recipients = ["+2547XXXXXXXX"]
```

Open the sandbox SMS simulator from the sandbox dashboard and add that same number there. The sandbox delivers the message to the simulator inbox, not to a real handset.

## 5. Send the first SMS

With the virtual environment still active:

```bash
python main.py
```

`main.py` loads `.env`, calls `africastalking.initialize()`, then `sms.send()`. A successful run prints `Africa's Talking is configured!` and an API response like this:

```text
{'SMSMessageData': {'Message': 'Sent to 1/1 Total Cost: KES 0.8000', 'Recipients': [...]}}
```

Check the simulator inbox for the text `Hello! This is my first Python SMS application.`

## Troubleshooting

**`The supplied authentication is invalid`**

The sandbox rejected the key. Confirm all of the following:

- The key was generated under **Go To Sandbox App → Settings → API Key**, not from a live app.
- `AT_USERNAME` is exactly `sandbox`.
- `.env` contains the newest key, and you waited a few minutes after generating it.

**WhatsApp warning**

```text
UserWarning: Sandbox is currently not available for the Whatsapp service.
```

`africastalking.initialize()` loads every service, including WhatsApp. The sandbox has no WhatsApp API, so the SDK prints that warning and continues. SMS is unaffected.

**`Set AT_USERNAME and AT_API_KEY in the .env file.`**

`.env` is missing, or one of those two values is empty. Copy `.env.example` to `.env` and fill in the sandbox key.
