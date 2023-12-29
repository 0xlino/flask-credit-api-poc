from flask import Flask, request, jsonify
from supabase import create_client, Client
# from supafunc.errors import APIError
from postgrest.exceptions import APIError
from consts import SUPABASE_URL, SUPABASE_KEY
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
from log import logger
from test import test_platform_functionality

app = Flask(__name__)

logger.info('Starting server')

def verify_api_key_from_supabase(request):
    api_key = request.args.get('api_key')
    data = supabase.table('api_keys').select('*').eq('uuid_key', api_key).execute()
    return len(data.data) > 0

def verify_api_key_from_supabase_with_credits(request):
    api_key = request.args.get('api_key') # this is on args because we are using GET, but in prod use the headers like 
    # api_key = request.headers.get('X-Api-Key')
    # data = supabase.table('api_keys').select('*').eq('uuid_key', api_key).execute()
    try:
        data = supabase.table('api_keys').select('*').eq('uuid_key', api_key).execute()
    except APIError as e:
        # we might call to api and the key is not found, let's yeet them away
        logger.error(e)
        return {
            'status': False,
            'message': 'API Key not found',
            'data': [],
            'credits': 0
        }
    # If we got here we have a key, let's check if we have credits on the key
    credits = data.data[0].get('credits')
    if credits <= 0:
        return {
            'status': False,
            'message': 'No Credits on key',
            'data': [],
            'credits': credits
        }
    return {
        'status': len(data.data) > 0,
        'message': 'API Key found',
        'data': data.data,
        'credits': credits
    }

@app.route('/v1/animals', methods=['GET'])
def get_animals():
    verify_a = verify_api_key_from_supabase_with_credits(request)
    if not verify_a.get('status'):
        return jsonify({'error': verify_a.get('message')}), 401
    datac = verify_a.get('data')[0]
    user_uuid = verify_a.get('data')[0].get('uuid_user_id')
    credits = verify_a.get('data')[0].get('credits')
    user_data = supabase.table('users').select('*').eq('uuid', user_uuid).execute()
    if len(user_data.data) == 0:
        return jsonify({'error': 'User not found'}), 404
    
    # test_platform_functionality(request, jsonify, supabase)

    animal_name = request.args.get('name')
    if not animal_name:
        return jsonify({'error': 'No animal name provided'}), 400
    
    animal_data = supabase.table('animals').select('*').ilike('name', f'%{animal_name}%').execute()
    
    supabase.table('api_keys').update({'credits': credits - 1}).eq('uuid_key', request.args.get('api_key')).execute()

    return jsonify({
        'user': user_data.data,
        'credits': credits - 1,
        'animal_data': animal_data.data
    })


if __name__ == '__main__':
    app.run(debug=True)


