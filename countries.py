
# country lists
# North America
countries_caribbean = [
        "Antigua and Barbuda", "Aruba", "Bahamas", "Barbados", 
        "Cayman Islands", "Cuba", "Dominica", "Dominican Republic",
        "Grenada", "Haiti", "Jamaica", "St. Kitts and Nevis", "St. Lucia",
        "St. Vincent and The Grenadines", "Trinidad and Tobago",
        ]

countries_north_america = [
        "Antigua and Barbuda", "Bahamas", "Barbados", "Belize", 
        "Bermuda", "Canada", "Costa Rica", "Cuba", "Dominica",
        "Dominican Republic", "El Salvador", "Grenada", "Guatemala"
        "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama",
        "St. Kitts and Nevis", "St. Lucia", "St. Vincent and The Grenadines",
        "Trinidad and Tobago", "United States",
        ]

countries_central_america = [
        "Belize", "Costa Rica", "El Salvador", "Guatemala", 
        "Honduras", "Nicaragua", "Panama",
        ]

countries_south_america = [
        "Argentina", "Bolivia", "Brazil", "Chile",
        "Colombia", "Ecuador", "Guyana", "Paraguay",
        "Peru", "Suriname", "Uruguay", "Venezuela",
        ]

countries_latin_america = [
        "Antigua and Barbuda", "Argentina", "Bahamas", "Barbados",
        "Bolivia", "Brazil", "Chile", "Costa Rica",
        "Cuba", "Dominica", "Dominican Republic", "El Salvador",
        "Ecuador", "Grenada", "Guatemala", "Haiti", "Honduras",
        "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay",
        "Peru", "St. Kitts and Nevis", "St. Lucia", "St. Vincent and The Grenadines",
        "Trinidad and Tobago", "Uruguay", "Venezuela",
        ]

region_america = []
american_countries = [
        countries_caribbean, countries_north_america, countries_central_america, 
        countries_south_america, countries_latin_america,
        ]

for group in american_countries:
    for country in group:
        region_america.append(country)


# Europe
countries_eu = [
        "Germany", "United Kingdom", "France", "Italy",
        "Spain", "Poland", "Romania", "Netherlands", "Belgium",
        "Czech Republic", "Greece", "Portugal", "Sweden",
        "Hungary", "Austria", "Bulgaria", "Denmark", "Finland",
        "Slovakia", "Ireland", "Croatia", "Lithuania", "Slovenia", 
        "Latvia", "Estonia", "Cyprus", "Luxembourg", "Malta",
        ]

countries_northern_europe = [
        "United Kingdom", "Sweden", "Denmark", 
        "Finland", "Norway", "Ireland", "Lithuania", 
        "Latvia", "Estonia", "Iceland",
    ]

countries_southern_europe = [
        "Turkey", "Italy", "Spain", "Greece", "Portugal",
        "Serbia", "Croatia", "Bosnia and Herzegovina", "Albania",
        "Slovenia", "North Macedonia", "Montenegro", "Malta", "Andorra",
        "San Marino", "Holy See",
    ]

countries_eastern_europe = [
        "Russia", "Ukraine", "Poland", "Romania", 
        "Czech Republic", "Hungary", "Belarus", "Bulgaria", 
        "Slovakia", "Moldova",
    ]

countries_western_europe = [
        "Germany", "France", "Netherlands", "Belgium", "Austria",
        "Switzerland", "Luxembourg", "Liechtenstein", "Monaco",
    ]

region_europe = []
european_countries = [
    countries_northern_europe, countries_southern_europe, 
    countries_eastern_europe, countries_western_europe,
    ]

for group in european_countries:
    for country in group:
        region_europe.append(country)


# Asia
countries_southern_asia = [
        "India", "Pakistan", "Bangladesh", "Afghanistan",
        "Nepal", "Sri Lanka", "Bhutan", "Maldives",
        ]

countries_southeastern_asia = [
        "Indonesia", "Phillipines", "Vietnam", "Thailand", "Burma",
        "Malaysia", "Cambodia", "Laos", "Singapore", "Timor-Leste",
        "Brunei",
        ]

countries_middle_east_asia = [
        "Egypt", "Turkey", "Iran", "Iraq", "Saudi Arabia", "Yemen",
        "Syria", "Jordan", "United Arab Emirates", "Israel", "Lebanon",
        "Oman", "Palestine", "Kuwait", "Qatar", "Bahrain", 
        ]

countries_eastern_asia = [
        "China", "Japan", "South Korea", "North Korea", "Mongolia",
        ]

countries_western_asia = [
        "Iran", "Turkey", "Iraq", "Saudi Arabia", "Yemen", "Syria",
        "Jordan", "Azerbaijan", "United Arab Emirates", "Israel", 
        "Lebanon", "Palestine", "Oman", "Kuwait", "Georgia", "Armenia",
        "Qatar", "Bahrain", "Cyprus", 
        ]

countries_central_asia = [
        "Uzbekistan", "Kazakhstan", "Tajikstan", "Kyrgyzstan", "Turkmenistan",
        ]

region_asia = []
asian_countries = [
        countries_southern_asia, countries_southeastern_asia, countries_middle_east_asia,
        countries_eastern_asia, countries_western_asia, countries_central_asia,
        ]

for group in asian_countries:
    for country in group:
        region_asia.append(country)


# Africa
countries_northern_africa = [
        "Egypt", "Algeria", "Sudan", "Morocco", "Tunisia", "South Sudan",
        "Libya", 
        ]

countries_southern_africa = [
        "South Africa", "Namibia", "Botswana", "Lesotho", "Swaziland",
        ]

countries_central_africa = [
        "Democratic Republic of the Congo", "Angola", "Camaroon", "Chad", "Central African Republic",
        "Republic of the Congo", "Gabon", "Equatorial Guinea", "Sao Tome and Principe",
        ]

countries_eastern_africa = [
        "Ethiopia", "Tanzania", "Kenya", "Uganda", "Mozambique", "Madagascar", "Malawi",
        "Zambia", "Somalia", "Zimbabwe", "South Sudan", "Rwanda", "Burundi", "Eritrea",
        "Mauritius", "Djibouti", "Comoros", "Seychelles", 
        ]

countries_western_africa = [
        "Nigeria", "Ghaman", "Cote d'lvoire", "Niger", "Burkina Faso", "Mali",
        "Senegal", "Guinea", "Benin", "Sierra Leone", "Togo", "Liberia", "Mauritania",
        "Gambia", "Guinea-Bissau", "Cape Verde",
        ]

region_africa = []
african_countries = [
        countries_northern_africa, countries_southern_africa, countries_central_africa,
        countries_eastern_africa, countries_western_africa,
        ]

for group in african_countries:
    for country in group:
        region_africa.append(country)


# Oceana
countries_melanesia = [
        "Papua New Guinea", "Fiji", "Solomon Islands", "Vanuatu",
        ]

countries_micronesia = [
        "Kirbati", "Federated States of Micronesia", "Marshall Islands", 
        "Palau", "Nauru",
        ]

countries_polynesia = [
        "New Zealand", "Samoa", "Tonga", "Tuvalu",
        ]

#revis
region_oceania = [
        "Australia",
        ]
oceanian_countries = [
        countries_melanesia, countries_micronesia, countries_polynesia,
        ]

for group in oceanian_countries:
    for country in group:
        region_oceania.append(country)

regions = [
        region_europe, region_america, 
        region_asia, region_africa, region_oceania,
        ]

country_names = [
        'Antigua and Barbuda', 'Aruba', 'Bahamas', 'Barbados', 'Cayman Islands', 'Cuba', 'Dominica', 'Dominican Republic', 'Grenada', 'Haiti', 
        'Jamaica', 'St. Kitts and Nevis', 'St. Lucia', 'St. Vincent and The Grenadines', 'Trinidad and Tobago', 'Belize', 'Bermuda', 'Canada', 
        'Costa Rica', 'El Salvador', 'Honduras', 'Mexico', 'Nicaragua', 'Panama', 'United States', 'Guatemala', 'Argentina', 
        'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela', 
        'Germany', 'United Kingdom', 'France', 'Italy', 'Spain', 'Poland', 'Romania', 'Netherlands', 'Belgium', 'Czech Republic', 'Greece', 
        'Portugal', 'Sweden', 'Hungary', 'Austria', 'Bulgaria', 'Denmark', 'Finland', 'Slovakia', 'Ireland', 'Croatia', 'Lithuania', 'Slovenia', 
        'Latvia', 'Estonia', 'Cyprus', 'Luxembourg', 'Malta', 'Norway', 'Iceland', 'Turkey', 'Serbia', 'Bosnia and Herzegovina', 'Albania', 
        'North Macedonia', 'Montenegro', 'Andorra', 'San Marino', 'Holy See', 'Russia', 'Ukraine', 'Belarus', 'Moldova', 'Switzerland', 
        'Liechtenstein', 'Monaco', 'India', 'Pakistan', 'Bangladesh', 'Afghanistan', 'Nepal', 'Sri Lanka', 'Bhutan', 'Maldives', 'Indonesia', 
        'Phillipines', 'Vietnam', 'Thailand', 'Burma', 'Malaysia', 'Cambodia', 'Laos', 'Singapore', 'Timor-Leste', 'Brunei', 'Egypt', 'Iran', 
        'Iraq', 'Saudi Arabia', 'Yemen', 'Syria', 'Jordan', 'United Arab Emirates', 'Israel', 'Lebanon', 'Oman', 'Palestine', 'Kuwait', 'Qatar', 
        'Bahrain', 'China', 'Japan', 'South Korea', 'North Korea', 'Mongolia', 'Azerbaijan', 'Georgia', 'Armenia', 'Uzbekistan', 'Kazakhstan', 
        'Tajikstan', 'Kyrgyzstan', 'Turkmenistan', 'Algeria', 'Sudan', 'Morocco', 'Tunisia', 'South Sudan', 'Libya', 'South Africa', 'Namibia', 
        'Botswana', 'Lesotho', 'Swaziland', 'Democratic Republic of the Congo', 'Angola', 'Camaroon', 'Chad', 'Central African Republic', 
        'Republic of the Congo', 'Gabon', 'Equatorial Guinea', 'Sao Tome and Principe', 'Ethiopia', 'Tanzania', 'Kenya', 'Uganda', 'Mozambique', 
        'Madagascar', 'Malawi', 'Zambia', 'Somalia', 'Zimbabwe', 'Rwanda', 'Burundi', 'Eritrea', 'Mauritius', 'Djibouti', 'Comoros', 
        'Seychelles', 'Nigeria', 'Ghaman', "Cote d'lvoire", 'Niger', 'Burkina Faso', 'Mali', 'Senegal', 'Guinea', 'Benin', 'Sierra Leone', 
        'Togo', 'Liberia', 'Mauritania', 'Gambia', 'Guinea-Bissau', 'Cape Verde', 'Papua New Guinea', 'Fiji', 'Solomon Islands', 'Vanuatu', 
        'Kirbati', 'Federated States of Micronesia', 'Marshall Islands', 'Palau', 'Nauru', 'New Zealand', 'Samoa', 'Tonga', 'Tuvalu', 'Australia',
        ]
