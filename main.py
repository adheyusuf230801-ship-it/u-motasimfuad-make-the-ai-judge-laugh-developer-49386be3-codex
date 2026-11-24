from pathlib import Path


EXCUSE = "I didn’t charge them twice; the retry count was in the idempotency key, so each retry arrived as a first-time customer."


def main():
    output = Path("/output")
    output.mkdir(parents=True, exist_ok=True)
    (output / "entry.txt").write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
