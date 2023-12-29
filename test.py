
def test_platform_functionality(request, jsonify, supabase):
    animal_name = request.args.get('name')
    if not animal_name:
        return jsonify({'error': 'No animal name provided'}), 400
    data = supabase.table('animals').select('*').ilike('name', f'%{animal_name}%').execute()
    len_data = len(data.data)
    if len_data == 0: 
        return jsonify({'error': str(f"No data for term - {animal_name}")}), 500
    return jsonify(data.data)