import TAHMO

api = TAHMO.apiWrapper()
api.setCredentials('demo', 'DemoPassword1!')

# Example 1: Get metadata from all stations that your account has access to.
stations = api.getStations()
print('Account has access to stations: %s' % ', '.join(list(stations)))

# Example 2: Get all variables and units from the TAHMO API.
print('\n\n')

variables = api.getVariables()
print('Available variables in TAHMO API:')
for variable in variables:
    print('%s [%s] with shortcode "%s"' %
          (variables[variable]['description'], variables[variable]['units'], variables[variable]['shortcode']))

# Example 3: Retrieve a pandas dataframe containing the time serie of surface air observations and save to CSV file.
print('\n\n')

station = 'TA00252'
startDate = '2019-01-01'
endDate = '2019-01-31'
variables = ['te', 'ap']

df = api.getMeasurements(station, startDate=startDate, endDate=endDate, variables=variables)
df.index.name = 'Timestamp'
df.to_csv('timeseries.csv', na_rep='', date_format='%Y-%m-%d %H:%M')
print('Timeseries saved to file "timeseries.csv"')

