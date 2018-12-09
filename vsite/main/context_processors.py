def add_variable_to_context(request):
    name = ''
    if request.user.is_anonymous != True:
        name = request.user.get_short_name() 
        
    return {
        'name' : name
    }