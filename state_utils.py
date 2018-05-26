


# fips, abb, name, utm zone
# NOTE: alaska covers many UTM zones! may not work
STATES_DATA = [
	['01', 'AL', 'Alabama', 16],
	['02', 'AK', 'Alaska', 5],
	['04', 'AZ', 'Arizona', 12],
	['05', 'AR', 'Arkansas', 15],
	['06', 'CA', 'California', 11],
	['08', 'CO', 'Colorado', 13],
	['09', 'CT', 'Connecticut', 18],
	['10', 'DE', 'Delaware', 18],
	['11', 'DC', 'District of Columbia', 18],
	['12', 'FL', 'Florida', 17],
	['13', 'GA', 'Georgia', 17],
	['15', 'HI', 'Hawaii', 4],
	['16', 'ID', 'Idaho', 11],
	['17', 'IL', 'Illinois', 16],
	['18', 'IN', 'Indiana', 16],
	['19', 'IA', 'Iowa', 15],
	['20', 'KS', 'Kansas', 14],
	['21', 'KY', 'Kentucky', 16],
	['22', 'LA', 'Louisiana', 15],
	['23', 'ME', 'Maine', 19],
	['24', 'MD', 'Maryland', 18],
	['25', 'MA', 'Massachusetts', 19],
	['26', 'MI', 'Michigan', 16],
	['27', 'MN', 'Minnesota', 15],
	['28', 'MS', 'Mississippi', 16],
	['29', 'MO', 'Missouri', 15],
	['30', 'MT', 'Montana', 12],
	['31', 'NE', 'Nebraska', 14],
	['32', 'NV', 'Nevada', 11],
	['33', 'NH', 'New Hampshire', 19],
	['34', 'NJ', 'New Jersey', 18],
	['35', 'NM', 'New Mexico', 13],
	['36', 'NY', 'New York', 18],
	['37', 'NC', 'North Carolina', 17],
	['38', 'ND', 'North Dakota', 14],
	['39', 'OH', 'Ohio', 17],
	['40', 'OK', 'Oklahoma', 14],
	['41', 'OR', 'Oregon', 10],
	['42', 'PA', 'Pennsylvania', 18],
	['72', 'PR', 'Puerto Rico', 19],
	['44', 'RI', 'Rhode Island', 19],
	['45', 'SC', 'South Carolina', 17],
	['46', 'SD', 'South Dakota', 14],
	['47', 'TN', 'Tennessee', 16],
	['48', 'TX', 'Texas', 14],
	['49', 'UT', 'Utah', 12],
	['50', 'VT', 'Vermont', 18],
	['51', 'VA', 'Virginia', 17],
	['53', 'WA', 'Washington', 10],
	['54', 'WV', 'West Virginia', 17],
	['55', 'WI', 'Wisconsin', 16],
	['56', 'WY', 'Wyoming', 13]
]



# ==============================================================================
# state abbreviation to state name
# ==============================================================================

def state_abb_to_full_name(state_abb):
	for x in STATES_DATA:
		if x[1] == state_abb.upper():
			return x[2]
	return None


# ==============================================================================
# state name to state abbreviation
# ==============================================================================

def state_name_to_abb(state_namae):
	for x in STATES_DATA:
		if x[2].upper() == state_name.upper():
			return x[1]
	return None


# ==============================================================================
# state abbreviation to UTM zone
# ==============================================================================

def state_abb_to_utm_zone(state_abb):
	for x in STATES_DATA:
		if x[1] == state_abb.upper():
			return x[3]
	return None
