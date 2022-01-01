# Single Disctionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# Print the Dictionary Keys
for county in counties_dict:
    print(county)
print("")

for county in counties_dict.keys():
    print(county)
print("")

# Prints the dictionary values
for voters in counties_dict.values():
    print (voters)
print("")

for county in counties_dict:
    print(counties_dict[county])
print("")

for county in counties_dict:
    print(counties_dict.get(county))
print("")

# Prints the Dictionary Keys and Values
for key, value in counties_dict.items():
    print(key, value)
print("")

# Prints text and dictionary key/values
for key, value in counties_dict.items():
    print('{} county has {} registered voters.'.format(key, value))
    print(f'{key} county has {voters} registered voters.') # F-String Format
print("")

# Dictionary inside a dictionary
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

# Prints keys from dictionary in the list of dictionaries using index
for i in range(len(voting_data)):
    print(voting_data[i]["county"])
print("")

# Prints keys from dictionary in the list of dictionaries
for county_dict in voting_data:
    print(county_dict['county'])
