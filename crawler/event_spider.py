import requests
import json
import time
import datetime
import pytz
import logging


# Configure logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def parse_time(timestamp):
    """Convert ISO format time to human-readable format in US Eastern Time."""
    eastern_tz = pytz.timezone('America/New_York')
    dt = datetime.datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
    dt_eastern = dt.astimezone(eastern_tz)
    return dt_eastern.strftime('%Y-%m-%d %H:%M:%S')

def transform_captured_data(comments_data):
    """Transform captured data to display format."""
    transformed_comments = []
    for comment in comments_data:
        # Extract and transform necessary fields
        username = comment.get('profile', {}).get('name', 'Unknown')
        published_time = parse_time(comment.get('createdAt', ''))
        content = comment.get('body', '')
        likes = len(comment.get('reactions', []))
        userAddress = comment.get('userAddress', '')
        proxyWallet = comment.get('profile', {}).get('proxyWallet', '')
        baseAddress = comment.get('profile', {}).get('baseAddress', '')

        # Create output format
        transformed_comment = {
            "username": username,
            "published_time": published_time,
            "content": content,
            "likes": likes,
            "userAddress": userAddress,
            "proxyWallet": proxyWallet,
            "baseAddress": baseAddress
        }
        logger.info("Transformed comment: %s", transformed_comment)
        transformed_comments.append(transformed_comment)
    return transformed_comments

def fetch_comments():
    """Fetch comments from API and transform to display format."""
    # Initialize with a known parent_entity_id
    initial_entity_id = 903193
    entity_id_queue = [initial_entity_id]
    visited_entity_ids = set()
    max_retries = 5
    retry_delay = 2

    with open("raw_comments.json", "w", encoding="utf-8") as f:
        while entity_id_queue:
            entity_id = entity_id_queue.pop(0)
            if entity_id in visited_entity_ids:
                continue
            logger.info(f"Processing parent_entity_id: {entity_id}")
            params = {
                "parent_entity_type": "Event",
                "parent_entity_id": entity_id,
                "get_positions": "true",
                "get_reports": "true",
                "ascending": "false",
                "order": "createdAt",
                "limit": 40,
                "offset": 0,
                "holders_only": "false"
            }
            empty_response_count = 0
            visited_entity_ids.add(entity_id)

            while True:
                for attempt in range(max_retries):
                    try:
                        response = requests.get("https://gamma-api.polymarket.com/comments", params=params)
                        response.raise_for_status()
                        comments_data = response.json()

                        if isinstance(comments_data, list):
                            if not comments_data:
                                empty_response_count += 1
                                logger.info("No more comments available for this parent_entity_id.")
                                break

                            transformed_comments = transform_captured_data(comments_data)
                            for comment in transformed_comments:
                                json.dump(comment, f, ensure_ascii=False)
                                f.write("\n")
                            
                            # Extract and queue new parent_entity_ids
                            new_entity_ids = {
                                c.get("parentEntityID") for c in comments_data if "parentEntityID" in c
                            }
                            unvisited_new_ids = new_entity_ids - visited_entity_ids
                            if unvisited_new_ids:
                                logger.info(f"Found new parent_entity_ids: {unvisited_new_ids}")
                            entity_id_queue.extend(unvisited_new_ids)
                            
                            empty_response_count = 0
                            params['offset'] += params['limit']
                        else:
                            logger.warning("Returned data is not a list, possible error message: %s", comments_data)
                            break

                    except requests.exceptions.RequestException as e:
                        logger.error(f"Request failed: {e}")
                        if attempt < max_retries - 1:
                            logger.info(f"Retrying... (Attempt {attempt + 2}/{max_retries})")
                            time.sleep(retry_delay)
                        else:
                            logger.error("Max retry attempts reached, stopping request for this ID.")
                            break
                else:
                    continue
                break

if __name__ == "__main__":
    fetch_comments()
