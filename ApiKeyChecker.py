import requests
import pyfiglet

def print_banner():
    # Create a big banner using pyfiglet
    print("\n\n")
    ascii_banner = pyfiglet.figlet_format("APIKey   Checker")
    print(ascii_banner)
    # Assuming a terminal width of 80 for right alignment of developer info
    dev_info = "mahfuz33r.github.io"
    print(dev_info.rjust(80))
    print("=" * 80)
    print()

def evaluate_response(service, response):
    """
    Evaluate the response for a given service.
    Returns a tuple (is_valid, simple_message) where:
      - is_valid is True if the API key is valid.
      - simple_message is None for valid keys or a simple string ("INVALID" or "UNAUTHORIZED") if not.
    """
    try:
        data = response.json()
    except ValueError:
        data = None

    # For Google Maps Geocoding API & Google Places API
    if service in ["Google Maps Geocoding API", "Google Places API"]:
        if data and "status" in data:
            if data["status"] in ["OK", "ZERO_RESULTS"]:
                return True, None
            else:
                return False, "INVALID"
        else:
            return False, "INVALID"

    elif service == "Google Maps Static Maps API":
        content_type = response.headers.get("Content-Type", "").lower()
        if "image" in content_type:
            return True, None
        else:
            return False, "INVALID"

    elif service == "Google OAuth Token":
        if data and "error" in data:
            return False, "INVALID"
        elif response.status_code == 200:
            return True, None
        else:
            return False, "INVALID"

    elif service == "Facebook Graph API":
        if data and "error" in data:
            return False, "UNAUTHORIZED"
        elif response.status_code == 200:
            return True, None
        else:
            return False, "INVALID"

    elif service in ["YouTube Data API", "Firebase Firestore", "Google Cloud Billing API", "Google Cloud Storage"]:
        if data and "error" in data:
            return False, "UNAUTHORIZED" if response.status_code in [401, 403] else "INVALID"
        elif response.status_code == 200:
            return True, None
        else:
            return False, "INVALID"

    # For header-based services (AWS API Gateway, OpenAI API Key)
    else:
        if response.status_code == 200:
            if service == "OpenAI API Key" and data and "error" in data:
                return False, "INVALID"
            return True, None
        elif response.status_code in [401, 403]:
            return False, "UNAUTHORIZED"
        else:
            return False, "INVALID"

def check_api_key(api_key):
    """
    Check the provided API key against multiple service endpoints.
    
    Update placeholder values (YOUR_PROJECT_ID, PROJECT_ID, and AWS endpoint URL) as needed.
    """
    # URL-based services (API key in URL)
    services = {
        "Google Maps Geocoding API": f"https://maps.googleapis.com/maps/api/geocode/json?address=Dhaka&key={api_key}",
        "Google Maps Static Maps API": f"https://maps.googleapis.com/maps/api/staticmap?center=45,10&zoom=3&size=400x400&key={api_key}",
        "Google Places API": f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=Dhaka&key={api_key}",
        "Firebase Firestore": f"https://firestore.googleapis.com/v1/projects/YOUR_PROJECT_ID/databases/(default)/documents?key={api_key}",
        "Google Cloud Billing API": f"https://cloudbilling.googleapis.com/v1/projects/PROJECT_ID/billingInfo?key={api_key}",
        "Google Cloud Storage": f"https://storage.googleapis.com/storage/v1/b?project=PROJECT_ID&key={api_key}",
        "YouTube Data API": f"https://www.googleapis.com/youtube/v3/channels?part=id&forUsername=GoogleDevelopers&key={api_key}",
        "Facebook Graph API": f"https://graph.facebook.com/v16.0/me?access_token={api_key}",
        "Google OAuth Token": f"https://oauth2.googleapis.com/tokeninfo?access_token={api_key}"
    }
    
    # Header-based services (API key via headers)
    header_services = {
        "AWS API Gateway": {
            "url": "https://your-api-id.execute-api.your-region.amazonaws.com/your-stage/resource",
            "headers": {"x-api-key": api_key}
        },
        "OpenAI API Key": {
            "url": "https://api.openai.com/v1/models",
            "headers": {"Authorization": f"Bearer {api_key}"}
        }
    }
    
    print("\n🔍 Checking API Key Validity...\n")
    
    # Check URL-based services
    for service, url in services.items():
        try:
            response = requests.get(url, timeout=10)
            is_valid, msg = evaluate_response(service, response)
            if is_valid:
                print(f"✅ {service}: VALID")
                print(f"   Test URL: {url}")
            else:
                print(f"❌ {service}: {msg}")
        except Exception:
            print(f"⚠️ {service}: Error checking API key")
    
    # Check header-based services
    for service, info in header_services.items():
        url = info["url"]
        headers = info.get("headers", {})
        try:
            response = requests.get(url, headers=headers, timeout=10)
            is_valid, msg = evaluate_response(service, response)
            if is_valid:
                print(f"✅ {service}: VALID")
                print(f"   Test URL: {url}  (Headers: {headers})")
            else:
                print(f"❌ {service}: {msg}")
        except Exception:
            print(f"⚠️ {service}: Error checking API key")

def main():
    print_banner()
    print("Enter your API keys (comma-separated):\n")
    keys_input = input().strip()
    keys = [k.strip() for k in keys_input.split(",") if k.strip()]
    
    for key in keys:
        print(f"\n========== Checking API key: {key} ==========")
        check_api_key(key)
        print("============================================\n")

if __name__ == "__main__":
    main()
