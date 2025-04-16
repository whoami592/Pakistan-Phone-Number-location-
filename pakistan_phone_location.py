import phonenumbers
from phonenumbers import geocoder, carrier

def get_phone_location(phone_number):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number, None)
        
        # Validate the phone number
        if not phonenumbers.is_valid_number(parsed_number):
            return "Invalid phone number"
        
        # Get location information
        location = geocoder.description_for_number(parsed_number, "en")
        
        # Get carrier information
        carrier_name = carrier.name_for_number(parsed_number, "en")
        
        # Format the result
        result = {
            "phone_number": phone_number,
            "location": location if location else "Location not found",
            "carrier": carrier_name if carrier_name else "Carrier not found"
        }
        
        return result
    
    except phonenumbers.phonenumberutil.NumberParseException:
        return "Error parsing phone number"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    # Example usage
    phone_number = input("Enter Pakistani phone number (e.g., +923409777222): ")
    result = get_phone_location(phone_number)
    
    # Print results
    if isinstance(result, dict):
        print("\nPhone Number Details:")
        print(f"Number: {result['phone_number']}")
        print(f"Location: {result['location']}")
        print(f"Carrier: {result['carrier']}")
    else:
        print(result)

if __name__ == "__main__":
    main()