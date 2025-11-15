import argparse,logging,os,time,schedule,requests
from datetime import datetime
from pathlib import Path
data_dir = Path("crypto_data"); data_dir.mkdir(exist_ok=True)

def fetch_crypto():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        r = requests.get(url, timeout=10); r.raise_for_status()
        file= data_dir / f"btc_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
        file.write_text(r.text)
        logging.info(f"Saved {file}")
    except Exception as e:
        logging.error(f"Error fetching crypto data: {e}")
def main():
    p = argparse.ArgumentParser(description="Auto Crypto Tracker")
    p.add_argument("--interval", type=int, default=60, help="Fetch interval in minutes")
    args = p.parse_args()
    logging.basicConfig(filename="autocryptotracker.log", level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")
    logging.info("Starting Auto Crypto Tracker.....")
    fetch_crypto()  # Initial fetch
    schedule.every(args.interval).minutes.do(fetch_crypto)
    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__ == "__main__":
    main()