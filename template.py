STATE_TEMPLATE = '''
<!--
- Follow the template exactly. Filling in {values}, keeping text outside of brackets, and replacing ...s.
- You are expected to fill out all the fields in the template and keep all default attributes
- You can format numbers as like: 123, ~123 million, etc. Do not use a percentage unless specified.
- All monetary amounts should be in USD
- Certain policies, descriptions, and values the answer may be "N/A due to..."
- Use "subgroups" to identify variance among specific sub-populations
- Do not use *italic* or **bold**
-->

# 1. Nation Overview
## Basic Information
- Country Name: {NationName}
- Government Type: {GovernmentType}
- Head of State/Government: {LeaderNameandTitle} <!-- role or group title, not name -->
- Total Population: {AbsoluteNumber}
- Currency: {CurrencyName} ({CurrencyCode})
- Land Area: {Areainsqkm}

# 2. Demographics, Health, and Crime
## Population Distribution
### Age Groups
- 0-4 years: {AbsoluteNumber}
- 5-17 years: {AbsoluteNumber}
- 18-24 years: {AbsoluteNumber}
- 25-44 years: {AbsoluteNumber}
- 45-64 years: {AbsoluteNumber}
- 65-74 years: {AbsoluteNumber}
- 75+ years: {AbsoluteNumber}

### Gender Composition
- Male: {Percentage}
- Female: {Percentage}
- Other: {Percentage}

### Sexuality Composition
- Heterosexual: {Percentage}
- Lesbian/Gay: {Percentage}
- Bisexual: {Percentage}
- Transgender: {Percentage}
- {Sexuality ...}: {Percentage}
...

### Urban vs. Rural
- Urban Population: {Percentage}
- Rural Population: {Percentage}

### Economic Composition
- Upper Class: {Percentage}
- Upper Middle Class: {Percentage}
- Middle Class: {Percentage}
- Lower Middle Class: {Percentage}
- Working Class: {Percentage}
- Below Poverty Line: {Percentage}

### Ethnic Composition
- {EthnicGroup ...}: {Percentage}
...
- Two or more races: {Percentage}
- Others: {Percentage}

### Language Composition
- {Language ...}: {Percentage}
...
- Multilingual: {Percentage}

### Religious Composition
- {Religion ...}: {Percentage}
...
- Unaffiliated/No Religion: {Percentage}

### Population Growth
- Overall Population Growth Rate: {Percentage} per year
- Subgroup Population Growth Rate
  - {Subgroup ...} Population Growth Rate: {Percentage} per year
  ...

### Migration
- Net Migration Rate: {Number} per 1,000 population
- Immigration: {DetailedDescription} immigrants annually
- Emigration: {DetailedDescription} emigrants annually

## Standard of Living
- Gallup World Happiness Score: {Value} out of 10
- Access to Improved Water Sources: {Percentage}
- Access to Improved Sanitation: {Percentage}
- Access to Electricity: {Percentage}
- Human Development Index (HDI): {Value}

## Education
- Education System: {DetailedDescription}
- Adult Literacy Rate: {Percentage}
- Average Years of Schooling: {NumberofYears} years
- Gender Parity Index in Education: {Value}
- Subgroup Literacy Rates
  - {Subgroup ...} Literacy Rate: {Percentage}
  ...

## Health
### Health System
- Health System: {DetailedDescription}
- Health Insurance: {DetailedDescription}
- Health Care Accessibility: {DetailedDescription}
- Health Care Costs: {DetailedDescription}

### Life Expectancy
- Average Life Expectancy at Birth: {NumberofYears} years
- Male Life Expectancy: {NumberofYears} years
- Female Life Expectancy: {NumberofYears} years
- Subgroup Life Expectancy
  - {Subgroup ...} Life Expectancy: {NumberofYears} years
  ...

### Diseases (Living)
- Obesity: {Number} in 100,000 population
- Mental Health: {Number} in 100,000 population
- {DiseaseName}: {Number} in 100,000 population
...

### Causes of Death
- Heart Disease: {Percentage} of deaths
- Cancer: {Percentage} of deaths
- Stroke: {Percentage} of deaths
- Diabetes: {Percentage} of deaths
- Accidents: {Percentage} of deaths
- Suicide: {Percentage} of deaths
- {Cause ...}: {Percentage} of deaths
...
- Other Causes: {Percentage} of deaths

### Health Indicators
- Infant Mortality Rate: {Number} per 1,000 live births
- Total Fertility Rate: {Number} children per woman
- Gross Reproduction Rate: {Number} female children per woman
- Maternal Mortality Rate: {Number} per 100,000 live births
- Child Mortality Rate: {Number} per 1,000 live births
- Physician Density: {Number} per 1,000 population
- Hospital Bed Density: {Number} per 1,000 population

## Crime
- Overall Crime Rate: {Number} per 100,000 population
- Crime Composition:
  - Homicide Rate: {Number} per 100,000 population
  - Assault Rate: {Number} per 100,000 population
  - Sexual Violence Rate: {Number} per 100,000 population
  - Burglary Rate: {Number} per 100,000 population
  - Theft Rate: {Number} per 100,000 population
  - Fraud Rate: {Number} per 100,000 population
  - Drug-Related Crime Rate: {Number} per 100,000 population
  - {CrimeType ...} Rate: {Number} per 100,000 population
  ...

## Equality
- Gender Inequality Index (GII): {Value} out of 1.0
- Female Labor Force Participation Rate: {Percentage}
- Racial/Ethnic Wage Gap: {DetailedDescription}
- Social Mobility Index: {Value} out of 100
- LGBTQ+ Legal Equality Index: {Value} out of 100

# 3. Economy
## Economic Indicators
- Gross Domestic Product (GDP in USD): {TotalAmountInUSD}
- GDP Growth Rate: {Percentage} per year
- Credit Ratings:
  - Standard & Poor's: {RatingLetters}
  - Moody's: {RatingLetters}
  - Fitch: {RatingLetters}
- Unemployment Rate: {Percentage}
- Inflation Rate: {Percentage}
- Poverty Rate: {Percentage}
- Gini Coefficient: {Value} out of 1.0
- Average Income: {TotalAmountInUSD}
- Average Disposable Income: {TotalAmountInUSD}

## Sector Contributions to GDP
- Agriculture: {Percentage} of GDP
- Industry: {Percentage} of GDP
- Services: {Percentage} of GDP
- Manufacturing: {Percentage} of GDP
- Construction: {Percentage} of GDP
- Mining and Quarrying: {Percentage} of GDP
- Financial Services: {Percentage} of GDP
- Real Estate: {Percentage} of GDP
- Information and Communications: {Percentage} of GDP
- Transportation and Storage: {Percentage} of GDP
- Wholesale and Retail Trade: {Percentage} of GDP
- Tourism and Hospitality: {Percentage} of GDP
- {Sector/Industry ...}: {Percentage} of GDP
...

## Industry Ownership
- Private Sector: {Percentage} of GDP
- State-Owned Enterprises (SOEs): {Percentage} of GDP
- Mixed Ownership: {Percentage} of GDP
- Public-Private Partnerships (PPPs): {Percentage} of GDP

## Key Industries
### Leading Industries by GDP Output
- {Industry ...}: {Percentage} of GDP
...

### Employment by Industry
- {Industry ...}: {Percentage} of workforce
...

## Government Budget
### Revenue
- Total Revenue: {TotalAmountInUSD}
  - Tax Revenue From {Category}: {TotalAmountInUSD}
  ...
  - Non-Tax Revenue From {Category}: {TotalAmountInUSD}
  ...

### Expenditure
- Total Expenditure: {TotalAmountInUSD}
  - Healthcare Expenditure: {TotalAmountInUSD}
  - Education Expenditure: {TotalAmountInUSD}
  - Defense Expenditure: {TotalAmountInUSD}
  - Infrastructure Expenditure: {TotalAmountInUSD}
  - Social Welfare Expenditure: {TotalAmountInUSD}
  - Environmental Protection Expenditure: {TotalAmountInUSD}
  - Public Safety and Law Enforcement Expenditure: {TotalAmountInUSD}
  - Housing and Urban Development Expenditure: {TotalAmountInUSD}
  - Agriculture and Rural Development Expenditure: {TotalAmountInUSD}
  - Debt Service (Interest Payments) Expenditure: {TotalAmountInUSD}
  - {Category ...}: {TotalAmountInUSD}
  ...
- National Debt: {TotalAmountInUSD}

## Trade
- Total Exports: {TotalAmountInUSD}
  - Exports from {Category}: {TotalAmountInUSD}
  ...
- Total Imports: {TotalAmountInUSD}
  - Imports from {Category}: {TotalAmountInUSD}
  ...

### Main Trading Partners
- Export Partners
  - {Country ...}: {Percentage}
  ...
- Import Partners
  - {Country ...}: {Percentage}
  ...

## Currency Exchange Rate
- {LocalCurrency}/USD = {ExchangeRate} ({Fixed}, {Floating}, {Pegged}) <!-- must include USD -->
- {LocalCurrency}/{ForeignCurrency} = {ExchangeRate} ({Fixed}, {Floating}, {Pegged})
...

# 4. Military
## Structure
- Military Structure: {DetailedDescription}
- Military Budget: {Percentage} of GDP

### Military Organization
- {Subgroup/BranchName ...}: {DetailedDescription}
...

## Capabilities
### Personnel
- {Personnel/Subgroup ...}: {AbsoluteNumber}
...

### Equipment
- Air Force Equipment
  - {EquipmentType ...}: {AbsoluteNumber}
  ...
- Naval Equipment
  - {EquipmentType ...}: {AbsoluteNumber}
  ...
- Ground Forces Equipment
  - {EquipmentType ...}: {AbsoluteNumber}
  ...
- Strategic Forces
  - {EquipmentType ...}: {AbsoluteNumber}
  ...
- Cyber and Electronic Warfare
  - {EquipmentType ...}: {AbsoluteNumber}
  ...
- Space Assets
  - {EquipmentType ...}: {AbsoluteNumber}
  ...

### Security Threats
- Terrorism: {DetailedDescription}
- Cybersecurity Threats: {DetailedDescription}
- {ThreatType/Group ...}: {DetailedDescription}
...

# 5. Media and Culture
## Media Landscape
- Press Freedom Index: {Value} out of 100
- Media Ownership: {DetailedDescription}

### Major Media Outlets <!-- avoid mentioning proper nouns -->
- {MediaType ...}: {DetailedDescription}
...

### Digital Media Metrics
- Digital Divide Index - Infrastructure: {Value} out of 100
- Digital Divide Index - Socioeconomic: {Value} out of 100
- Social Media Usage: {Percentage}

## Cultural Identity
### Cultural Values
- Traditional Values: {DetailedDescription}
- Predominant Social Norms: {DetailedDescription}

### Sports and Recreation
- {Sport/Activity ...}: {DetailedDescription}
...

## Cultural Influence
- Soft Power Index: {Value} of 100
- International Cultural Centers: {AbsoluteNumber}
- Cultural Exchange Programs: {DetailedDescription}

## Cultural Events
- National Holidays: {DetailedDescription}
- {Event ...}: {DetailedDescription}
...

# 6. Infrastructure and Technology
## Transportation Infrastructure <!-- avoid mentioning proper nouns -->
- Road Network: {DetailedDescription}
- Public Transport: {DetailedDescription}
- Railways: {DetailedDescription}
- Airports: {DetailedDescription}
- Ports and Harbors: {DetailedDescription}
- {InfrastructureType ...}: {DetailedDescription}
...

## Energy Infrastructure
- Total Electricity Generation: {Megawatts}
  - Natural Gas: {Percentage}
  - Renewable Energy: {Percentage}
  - Nuclear Energy: {Percentage}
  - Coal: {Percentage}
  - Hydroelectric: {Percentage}
  - {EnergySource ...}: {Percentage}
  ...

## Telecommunications
- Internet Penetration Rate: {Percentage}
- Broadband Subscriptions: {Number} per 100 inhabitants
- Mobile Phone Subscriptions: {Number} per 100 inhabitants
- Highspeed Internet Access: {Number} per 100 inhabitants

## Technology and Innovation
- R&D Expenditure: {Percentage} of GDP
- Patents Filed Annually: {AbsoluteNumber}

### Technologies
- Artificial Intelligence: {DetailedDescription}
- Quantum Computing: {DetailedDescription}
- Robotics: {DetailedDescription}
- Space Program: {DetailedDescription}
- Biotechnology: {DetailedDescription}
- {Technology ...}: {DetailedDescription}
...

# 7. Government Policies <!-- all types should have at least 2 policies -->
### Political Policies
- Government Structure: {DetailedDescription}
  - {Branch/Subgroup ...}: {DetailedDescriptionOfRuleAndPowers}
  ...
- Parties: {Ruling PartyName(s), Opposition PartyName(s)}
- Electoral System: {DetailedDescription}
- {PolicyType ...}: {DetailedDescription}
...

### Civil Liberties and Political Rights Policies
- Corruption Perception Index (CPI): {Value} out of 100
- Freedoms
  - Freedom of Speech and Press: {StatusDescription}
  - Freedom of {FreedomType}: {StatusDescription}
  ...
- {PolicyType ...}: {DetailedDescription}
...

### Fiscal Policies <!-- e.g. tax rates, government spending priorities -->
- {PolicyType ...}: {DetailedDescription}
...

### Monetary Policies <!-- e.g. inflation targets, interest rates -->
- {PolicyType ...}: {DetailedDescription}
...

### Labor Market Policies <!-- e.g. minimum wage, unemployment benefits -->
- {PolicyType ...}: {DetailedDescription}
...

### Trade Policies <!-- e.g. tariffs, trade agreements -->
- {PolicyType ...}: {DetailedDescription}
...

### Investment Policies <!-- e.g. domestic investment incentives, foreign investment regulations -->
- {PolicyType ...}: {DetailedDescription}
...

### Education Policies <!-- e.g. school systems, educational reforms -->
- {PolicyType ...}: {DetailedDescription}
...

### Healthcare Policies
- {PolicyType ...}: {DetailedDescription}
...

### Social Welfare Policies
- {PolicyType ...}: {DetailedDescription}
...

### Housing Policies
- {PolicyType ...}: {DetailedDescription}
...

### Media Policies
- {PolicyType ...}: {DetailedDescription}
...

### Cultural Policies
- {PolicyType ...}: {DetailedDescription}
...

### Climate Policies
- International Agreements: {DetailedDescription}
- {PolicyType ...}: {DetailedDescription}
...

### Pollution Control Policies
- Industrial Emissions Regulations: {DetailedDescription}
- Waste Management: {DetailedDescription}
- {PolicyType ...}: {DetailedDescription}
...

### Conservation Policies <!-- e.g. conservation laws, environmental regulations -->
- {PolicyType ...}: {DetailedDescription}
...

### Diplomatic Policies <!-- e.g. alliances, memberships, foreign policy -->
- {PolicyType ...}: {DetailedDescription}
...

### Defense, Military, and Security Policies
- {PolicyType ...}: {DetailedDescription}
...

### Immigration Policies <!-- e.g. visa requirements, immigration laws -->
- {PolicyType ...}: {DetailedDescription}
...

# 8. Public Opinion and Citizen Sentiment
## Top Concerns Among Citizens
- {Concern ...}: {Percentage}
...

## Latest Polling Data
- Optimistic Perception of Economic Future: {Percentage}
- Direction of Country: {Percentage} believe country is on right track
- Overall Government Approval Rating: {Percentage}
- Institution Approval Ratings  
  - {Institution ...} Approval Rating: {Percentage}
  ...
'''