import json

def sol(arr):
    business_count = 0

    for business_string in arr:
        # business_string is a stringified json object that represents a business
        business = json.loads(business_string)

        # find opening hours (before 10 military time)
        if 'sunday' in business['hours']:
            sunday_hours = business['hours']['sunday'][0]
            opening_hours = sunday_hours[0]
        
            if int(opening_hours.split(':')[0]) < 10:
                business_count += 1
          
    return business_count