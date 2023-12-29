# Flask Credit API POC

# Project Documentation

## Overview
This project is a Flask-based web service interfacing with Supabase for data storage and management. It features API key verification and credit-based access control for its endpoints.

### Key Features:
- API key verification from Supabase.
- Credit system for API usage.
- User and animal data retrieval based on API key and query parameters.

### Dependencies:
- Flask
- Supabase
- PostgREST

## Setup and Installation
1. **Install Required Packages**: 
   ```bash
   pip install Flask supabase postgrest
   ```
2. **Configure Environment Variables**:
   - Set `SUPABASE_URL` and `SUPABASE_KEY` in `consts.py`.

## Usage
1. **Start the Flask Server**:
   ```bash
   python [filename].py
   ```
2. **API Endpoints**:
   - `/v1/animals`: Get animal data based on the name query parameter. Requires API key for access.

### Verifying API Key:
- The API key is verified against the Supabase 'api_keys' table.
- Two methods provided: `verify_api_key_from_supabase` and `verify_api_key_from_supabase_with_credits`.

### Handling Credits:
- Each API call checks and deducts credits associated with the API key.
- Responses include credit information and relevant data or error messages.

## Error Handling
- Errors are logged using a custom logger.
- Exceptions, such as `APIError` from PostgREST, are caught and handled appropriately.

## Testing
- The `test_platform_functionality` function can be used to test the complete functionality.
- It is currently commented out and can be activated for development tests.

## Note
- For production, it's recommended to retrieve the API key from request headers for security purposes.

## Contribution
- Contributions are welcome. Please follow the standard pull request process for contributions.