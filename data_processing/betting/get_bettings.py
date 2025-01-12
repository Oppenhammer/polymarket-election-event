import json
import logging
import asyncio
import aiohttp
import aiofiles

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

CONCURRENT_REQUESTS = 10 

async def fetch_position_data(session, proxy_wallet, semaphore, retries=3):

    url = f"https://data-api.polymarket.com/positions?user={proxy_wallet}"
    for attempt in range(retries):
        async with semaphore:
            try:
                logger.info(f"Requesting position data: {url}")
                async with session.get(url, timeout=aiohttp.ClientTimeout(total=30)) as response:
                    response.raise_for_status()
                    data = await response.json()
                    if not data:
                        logger.warning(f"Received empty data: {url}")
                    return data
            except aiohttp.ClientError as e:
                logger.error(f"Request failed (attempt {attempt + 1}/{retries}): {e} ({url})")
                if attempt < retries - 1:
                    await asyncio.sleep(2 ** attempt)  # Exponential backoff
                else:
                    logger.error(f"All retries exhausted, could not fetch data: {url}")
                    return []  
            except Exception as e:
                logger.error(f"Unexpected error: {e} ({url})")
                return []  

async def process_wallet(session, wallet, semaphore):
    """Process a single wallet address."""
    logger.info(f"Processing wallet address: {wallet}")
    positions_data = await fetch_position_data(session, wallet, semaphore)
    results = []
    
    if not positions_data:
        logger.warning(f"No valid data retrieved for wallet {wallet}, skipping.")
        return results
    
    # Process valid data
    for position in positions_data:
        if position.get("title") in [
            "Will Donald Trump win the 2024 US Presidential Election?",
            "Will Kamala Harris win the 2024 US Presidential Election?"
        ]:
            logger.info(f"Matching data found: {position}")
            results.append({
                "wallet": wallet,
                "size": position.get("size"),
                "avgPrice": position.get("avgPrice"),
                "initialValue": position.get("initialValue"),
                "currentValue": position.get("currentValue"),
                "title": position.get("title"),
                "cashPnl": position.get("cashPnl"),
                "percentPnl": position.get("percentPnl"),
                "bettingPosition": position.get("outcome")
            })
    return results

async def process_wallets():
    semaphore = asyncio.Semaphore(CONCURRENT_REQUESTS)  
    async with aiohttp.ClientSession() as session:
       
        async with aiofiles.open('final_Comments_producer/proxy_wallets.json', 'r', encoding='utf-8') as infile:
            wallets = json.loads(await infile.read())  

        tasks = []
        processed_count = 0
        async with aiofiles.open('proxy_wallet_results.json', 'w', encoding='utf-8') as outfile:
            for idx, wallet in enumerate(wallets):
                tasks.append(process_wallet(session, wallet, semaphore))

                # processed once every 100 wallets
                if (idx + 1) % 100 == 0 or (idx + 1) == len(wallets):
                    logger.info(f"Processed up to wallet {idx + 1}, writing to file...")
                    processed_results = await asyncio.gather(*tasks, return_exceptions=True)
                    tasks = []  

                    
                    for result in processed_results:
                        if isinstance(result, Exception):
                            logger.error(f"Error during processing: {result}")
                        elif result: 
                            for entry in result: 
                                await outfile.write(json.dumps(entry, ensure_ascii=False) + "\n")
                                processed_count += 1
                    logger.info(f"Processed and wrote {processed_count} records.")

        # Process remaining tasks (if any)
        if tasks:
            logger.info(f"Processing remaining wallets, count: {len(tasks)}")
            processed_results = await asyncio.gather(*tasks, return_exceptions=True)
            async with aiofiles.open('proxy_wallet_results.json', 'a', encoding='utf-8') as outfile:
                for result in processed_results:
                    if isinstance(result, Exception):
                        logger.error(f"Error during processing: {result}")
                    elif result: 
                        for entry in result:
                            await outfile.write(json.dumps(entry, ensure_ascii=False) + "\n")
                            processed_count += 1
            logger.info("Remaining wallets written to file.")

if __name__ == "__main__":
    try:
        logger.info("Starting to process wallet data...")
        asyncio.run(process_wallets())
        logger.info("Wallet data processing completed.")
    except KeyboardInterrupt:
        logger.info("Program interrupted by user.")
