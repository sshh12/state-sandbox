STATE_TEMPLATE = '''
<!--
- Follow the template exactly. Filling in {values}, keeping text outside of brackets, and replacing ...s.
- You are expected to fill out all the fields in the template and keep all default attributes
- You can format numbers as like: 123, ~123 million, etc. Do not use a percentage unless specified.
- You can format percentages as like: 12%, ~12%, < 0.1%, etc.
- All monetary amounts should be in USD
- Certain policies, descriptions, and values the answer may be "N/A due to...". For metrics that should exist, but you don't know, use your best guess.
- Use "subgroups" to identify variance among specific sub-populations
- Do not use *italic* or **bold**. 
- Do not add nested lists or headings not specified in the template.
-->

# 1. Nation Overview
## Basic Information
- Country Name: {NationName}
- Government Type: {GovernmentType}
- Head of State/Government: {Title} <!-- role or group title, not name -->
- Total Population: {AbsoluteNumber}
- Currency: {CurrencyName} ({CurrencyCode})
- Land Area: {Area} sq km

# 2. Demographics
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

### Sexuality Composition <!-- reported by census -->
- Heterosexual: {Percentage}
- Lesbian/Gay: {Percentage}
- Bisexual: {Percentage}
- Transgender: {Percentage}
- {Sexuality}: {Percentage}
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

### Education Composition
- No Schooling: {Percentage}
- Some Primary Education: {Percentage} <!-- e.g. elementary school -->
- Primary Education Complete: {Percentage}
- Some Secondary Education: {Percentage} <!-- e.g. high school -->
- Secondary Education Complete: {Percentage}
- Some Tertiary Education: {Percentage} <!-- e.g. college -->
- Tertiary Education Complete: {Percentage}
- PhD or Masters: {Percentage}

### Ethnic Composition
- {EthnicGroup}: {Percentage}
...
- Two or more races: {Percentage}
- Others: {Percentage}

### Language Composition
- {Language}: {Percentage}
...
- Multilingual: {Percentage}

### Religious Composition
- {Religion}: {Percentage}
...
- Unaffiliated/No Religion: {Percentage}

### Population Growth
- Overall Population Growth Rate: {Percentage} per year
- Ethnic Population Growth: {DetailedDescription}
- Religious Population Growth: {DetailedDescription}

### Migration
- Immigration: {DetailedDescription}
- Immigration Sentiment: {DetailedDescription} <!-- e.g. how do citizens feel about immigrants -->
- Immigration Totals: {Number} immigrants annually
- Emigration: {DetailedDescription}
- Emigration Sentiment: {DetailedDescription} <!-- e.g. how do citizens feel about emigrants -->
- Emigration Totals: {Number} emigrants annually

## Standard of Living
- Gallup World Happiness Score: {Value} out of 10
- Access to Improved Water Sources: {Percentage}
- Access to Improved Sanitation: {Percentage}
- Access to Electricity: {Percentage}
- Human Development Index (HDI): {Value}

## Education
- Education System: {DetailedDescription}
  - {EducationLevel}: {DetailedDescription}
  ...
- Adult Literacy Rate: {Percentage}
- Average Years of Schooling: {Value} years
- Gender Parity Index in Education: {Value}
- Ethnic Literacy: {DetailedDescription} <!-- relationship between literacy and ethnicity -->

## Equality
- Gender Inequality Index (GII): {Value} out of 1.0
- Female Labor Force Participation Rate: {Percentage}
- Racial/Ethnic Wage Gap: {DetailedDescription}
- Social Mobility Index: {Value} out of 100
- LGBTQ+ Legal Equality Index: {Value} out of 100

### Social Challenges <!-- e.g. ethnic tensions, religious tensions, etc. -->
- {SocialChallenge}: {DetailedDescription}
...

# 3. Health & Crime
## Health System
- Health System: {DetailedDescription}
- Health Insurance: {DetailedDescription} <!-- e.g. private, public, mixed, etc. -->
- Health Care Accessibility: {DetailedDescription} <!-- e.g. costs, wait times, etc. -->

### Life Expectancy
- Average Life Expectancy at Birth: {Value} years
- Male Life Expectancy: {Value} years
- Female Life Expectancy: {Value} years
- Ethnic Life Expectancy: {DetailedDescription} <!-- relationship between life expectancy and ethnicity -->

### Diseases <!-- for living diseases -->
- Obesity: {Number} in 100,000 population
- Mental Health: {Number} in 100,000 population
- Diabetes: {Number} in 100,000 population
- Hypertension: {Number} in 100,000 population
- Asthma: {Number} in 100,000 population
- Heart Disease: {Number} in 100,000 population
- Cancer: {Number} in 100,000 population
- {DiseaseName}: {Number} in 100,000 population
...

### Causes of Death
- Heart Disease: {Percentage} of deaths
- Cancer: {Percentage} of deaths
- Stroke: {Percentage} of deaths
- Diabetes: {Percentage} of deaths
- Accidents: {Percentage} of deaths
- Suicide: {Percentage} of deaths
- {CauseOfDeath}: {Percentage} of deaths
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

## Crime Statistics
- Overall Crime Rate: {Number} per 100,000 population
  - Homicide Rate: {Number} per 100,000 population
  - Assault Rate: {Number} per 100,000 population
  - Sexual Violence Rate: {Number} per 100,000 population
  - Burglary Rate: {Number} per 100,000 population
  - Theft Rate: {Number} per 100,000 population
  - Fraud Rate: {Number} per 100,000 population
  - Drug-Related Crime Rate: {Number} per 100,000 population
  - {CrimeType} Rate: {Number} per 100,000 population
  ...
- Corruption Perception Index (CPI): {Value} out of 100

## Crime Challenges <!-- e.g. hate crimes, gun violence, drug violence, etc. -->
- {CrimeChallenge}: {DetailedDescription}
...

# 5. Economy
## Economic Indicators
- Gross Domestic Product (GDP in USD): {TotalAmountInUSD}
- GDP Growth Rate: {Percentage} per year
- Credit Ratings:
  - Standard & Poor's: {RatingLetters}
  - Moody's: {RatingLetters}
  - Fitch: {RatingLetters}
- Unemployment Rate: {Percentage}
- Poverty Rate: {Percentage}
- Inflation Rate (Annualized): {Percentage}
- Gini Coefficient: {Value} out of 1.0
- Average Income: {TotalAmountInUSD}
- Public Economic Sentiment: {DetailedDescription}

## Industry Ownership
- Private Sector: {Percentage} of GDP
- State-Owned Enterprises (SOEs): {Percentage} of GDP
- Mixed Ownership: {Percentage} of GDP
- Public-Private Partnerships (PPPs): {Percentage} of GDP

## Sectors
### Industries  <!-- e.g. for each sector describe industries and specializations within it, some sectors may be nearly nonexistent -->
- Agriculture: {DetailedDescription}
- Services: {DetailedDescription}
- Manufacturing: {DetailedDescription}
- Construction: {DetailedDescription}
- Mining: {DetailedDescription}
- Financial Services: {DetailedDescription}
- Real Estate: {DetailedDescription}
- Technology: {DetailedDescription}
- Transportation: {DetailedDescription}
- Wholesale and Retail Trade: {DetailedDescription}
- Tourism and Hospitality: {DetailedDescription}
- {Sector}: {DetailedDescription}
...

### Sector Contributions to GDP
- Agriculture: {Percentage} of GDP
- Services: {Percentage} of GDP
- Manufacturing: {Percentage} of GDP
- Construction: {Percentage} of GDP
- Mining: {Percentage} of GDP
- Financial Services: {Percentage} of GDP
- Real Estate: {Percentage} of GDP
- Technology: {Percentage} of GDP
- Transportation: {Percentage} of GDP
- Wholesale and Retail Trade: {Percentage} of GDP
- Tourism and Hospitality: {Percentage} of GDP
- {Sector}: {Percentage} of GDP
...

### Employment by Sector
- Agriculture: {Percentage} of workforce
- Services: {Percentage} of workforce
- Manufacturing: {Percentage} of workforce
- Construction: {Percentage} of workforce
- Mining: {Percentage} of workforce
- Financial Services: {Percentage} of workforce
- Real Estate: {Percentage} of workforce
- Technology: {Percentage} of workforce
- Transportation: {Percentage} of workforce
- Wholesale and Retail Trade: {Percentage} of workforce
- Tourism and Hospitality: {Percentage} of workforce
- {Sector}: {Percentage} of workforce
...

## Economic Challenges <!-- e.g. unemployment, inflation,etc. -->
- {EconomicChallenge}: {DetailedDescription}
...

## Government Budget
### Revenue
- Total Revenue: {TotalAmountInUSD} <!-- note that some of these could be zero -->
  - Income Tax: {Percentage}
  - Corporate Tax: {Percentage}
  - Sales Tax/VAT: {Percentage} 
  - Property Tax: {Percentage}
  - Capital Gains Tax: {Percentage}
  - Import/Export Duties: {Percentage}
  - Social Security Contributions: {Percentage}
  - Excise Tax: {Percentage}
  - Estate/Inheritance Tax: {Percentage}
  - Non-Tax Revenue from State-Owned Enterprises: {Percentage}
  - Non-Tax Revenue from Natural Resources: {Percentage}
  - Non-Tax Revenue from Government Services: {Percentage}
  - Non-Tax Revenue from Fines and Penalties: {Percentage}
  - Non-Tax Revenue from Investment Income: {Percentage}
  - Other Revenue Sources: {Percentage}

### Expenditure
- Total Expenditure: {TotalAmountInUSD} <!-- note that some of these could be zero -->
  - Healthcare Expenditure: {TotalAmountInUSD}
  - Education Expenditure: {TotalAmountInUSD}
  - Defense and Military Expenditure: {TotalAmountInUSD}
  - Infrastructure Expenditure: {TotalAmountInUSD}
  - Social Welfare Expenditure: {TotalAmountInUSD}
  - Environmental Protection Expenditure: {TotalAmountInUSD}
  - Public Safety and Law Enforcement Expenditure: {TotalAmountInUSD}
  - Housing and Urban Development Expenditure: {TotalAmountInUSD}
  - Agriculture and Rural Development Expenditure: {TotalAmountInUSD}
  - Debt Service (Interest Payments) Expenditure: {TotalAmountInUSD}
  - {ExpenditureCategory}: {TotalAmountInUSD}
  ...
- National Debt: {TotalAmountInUSD}

## Trade
- Total Exports: {TotalAmountInUSD}
  - Exports from {Sector}: {Percentage}
  ...
  - Other Exports: {Percentage}
- Total Imports: {TotalAmountInUSD}
  - Imports for {Sector}: {Percentage}
  ...
  - Other Imports: {Percentage}

### Main Trading Partners
- Export Partners
  - {Country}: {Percentage}
  ...
  - Other Export Partners: {Percentage}
- Import Partners
  - {Country}: {Percentage}
  ...
  - Other Import Partners: {Percentage}

## Exchange Rate <!-- only for USD -->
- {LocalCurrency}/USD = {ExchangeRate}

# 6. Military
### Military Organization
- Military Structure: {DetailedDescription}
  - {SubgroupOrBranchName}: {DetailedDescription}
  ...
- Public Military Sentiment: {DetailedDescription}

## Capabilities
### Personnel <!-- e.g. active duty, reserve, national guard, etc. -->
- {PersonnelType}: {AbsoluteNumber}
...

### Equipment <!-- Be sure to include the {AbsoluteNumber} for each equipment type, for some this may be zero -->
- Air Force Equipment
  - {EquipmentType}: {AbsoluteNumber}
  ...
- Naval Equipment
  - Aircraft Carriers: {AbsoluteNumber}
  - Nuclear Submarines: {AbsoluteNumber}
  - {EquipmentType}: {AbsoluteNumber}
  ...
- Ground Forces Equipment
  - {EquipmentType}: {AbsoluteNumber}
  ...
- Strategic Forces
  - Nuclear ICMBs: {AbsoluteNumber}
  - {EquipmentType}: {AbsoluteNumber}
  ...
- Cyber and Electronic Warfare
  - {EquipmentType}: {AbsoluteNumber}
  ...
- Space Assets
  - Military Satellites: {AbsoluteNumber}
  - {EquipmentType}: {AbsoluteNumber}
  ...

### Security Threats
- Terrorism: {DetailedDescription}
- Cybersecurity Threats: {DetailedDescription}
- {ThreatTypeOrGroup}: {DetailedDescription}
...

# 7. Media
## Media Landscape
- Press Freedom Index: {Value} out of 100
- Media Ownership: {DetailedDescription}

### Major Media Outlets <!-- avoid mentioning proper nouns, just types -->
- {MediaType}: {DetailedDescription}
...

### Media Coverage <!-- e.g. coverage of issues, % of media time spent on issues -->
- {MediaIssue}: {Percentage}
...

### Digital Media
- Digital Divide Index - Infrastructure: {Value} out of 100
- Digital Divide Index - Socioeconomic: {Value} out of 100
- Social Media Usage: {Percentage}

# 8. Culture
## Cultural Identity
### Cultural Values
- Traditional Values: {DetailedDescription}
- Family Values: {DetailedDescription}
- Work Ethics: {DetailedDescription}
- Gender Roles: {DetailedDescription}
- Individualism vs Collectivism: {DetailedDescription}
- Religious Values: {DetailedDescription}

### Cultural Challenges
- {CulturalChallenge}: {DetailedDescription}
...

### Sports and Recreation
- {SportOrActivity}: {DetailedDescription}
...

## Cultural Influence
- Soft Power Index: {Value} of 100
- International Cultural Centers: {AbsoluteNumber}
- Cultural Exchange Programs: {DetailedDescription}

## Cultural Events
- National Holidays: {AbsoluteNumber}
- Religious Holidays: {AbsoluteNumber}
- Memorial Days: {AbsoluteNumber}
- Cultural Festivals: {AbsoluteNumber}

# 9. Infrastructure and Technology
## Transportation Infrastructure <!-- avoid mentioning proper nouns -->
- Road Network: {DetailedDescription}
- Public Transport: {DetailedDescription}
- Railways: {DetailedDescription}
- Airports: {DetailedDescription}
- Ports and Harbors: {DetailedDescription}
- {InfrastructureType}: {DetailedDescription}
...

## Energy Infrastructure
- Total Electricity Generation: {Megawatts}
  - Natural Gas: {Percentage}
  - Renewable Energy: {Percentage}
  - Nuclear Energy: {Percentage}
  - Coal: {Percentage}
  - Hydroelectric: {Percentage}
  - {EnergySource}: {Percentage}
  ...

## Telecommunications
- Internet Penetration Rate: {Number} per 100 inhabitants
- Broadband Subscriptions: {Number} per 100 inhabitants
- Mobile Phone Subscriptions: {Number} per 100 inhabitants
- Highspeed Internet Access: {Number} per 100 inhabitants

## Technology and Innovation
- R&D Expenditure: {Percentage} of GDP

### Technologies
- Artificial Intelligence: {DetailedDescription}
- Quantum Computing: {DetailedDescription}
- Robotics: {DetailedDescription}
- Space Program: {DetailedDescription}
- Biotechnology: {DetailedDescription}
- {Technology}: {DetailedDescription}
...

### Infrastructure Challenges <!-- e.g. infrastructure decay, lack of infrastructure, etc. -->
- {InfrastructureChallenge}: {DetailedDescription}
...

# 10. Government 
## Government Structure
- Government Structure: {DetailedDescription}
- Key Governing Documents: {DetailedDescription} <!-- what they are and what they are about -->
- Political Parties: {DetailedDescription}
- Electoral System: {DetailedDescription}

## Government Powers
- {GovernmentBranchOrRole}: {DetailedDescription} <!-- be detailed about what they can and cannot do -->
...

## Policies <!-- all policy types should have at least 3 policies -->

### Civil Liberties and Political Rights Policies <!-- e.g. freedom or restriction of speech, press, assembly, religion -->
- {PolicyType}: {DetailedDescription}
...

### Fiscal Policies <!-- e.g. tax rates, government spending priorities -->
- {PolicyType}: {DetailedDescription}
...

### Monetary Policies <!-- e.g. inflation targets, interest rates -->
- {PolicyType}: {DetailedDescription}
...

### Labor Market Policies <!-- e.g. minimum wage, unemployment benefits -->
- {PolicyType}: {DetailedDescription}
...

### Trade Policies <!-- e.g. tariffs, trade agreements -->
- {PolicyType}: {DetailedDescription}
...

### Investment Policies <!-- e.g. domestic investment incentives, foreign investment regulations -->
- {PolicyType}: {DetailedDescription}
...

### Education Policies <!-- e.g. school systems, educational reforms -->
- {PolicyType}: {DetailedDescription}
...

### Healthcare Policies <!-- e.g. healthcare systems, healthcare reforms -->
- {PolicyType}: {DetailedDescription}
...

### Drug and Substance Control Policies <!-- e.g. drug laws, substance abuse policies -->
- {PolicyType}: {DetailedDescription}
...

### Criminal Justice and Law Enforcement Policies <!-- e.g. police forces, prisons, courts -->
- {PolicyType}: {DetailedDescription}
...

### Social Welfare Policies <!-- e.g. social security systems, social welfare programs -->
- {PolicyType}: {DetailedDescription}
...

### Housing Policies <!-- e.g. housing policies, housing reforms -->
- {PolicyType}: {DetailedDescription}
...

### Media Policies <!-- e.g. media regulations, media ownership -->
- {PolicyType}: {DetailedDescription}
...

### Cultural Policies <!-- e.g. cultural policies, cultural reforms -->
- {PolicyType}: {DetailedDescription}
...

### Climate Policies <!-- e.g. international agreements, carbon pricing -->
- {PolicyType}: {DetailedDescription}
...

### Pollution Control Policies <!-- e.g. industrial emissions regulations, waste management -->
- {PolicyType}: {DetailedDescription}
...

### Conservation Policies <!-- e.g. conservation laws, environmental regulations -->
- {PolicyType}: {DetailedDescription}
...

### Diplomatic Policies <!-- e.g. alliances, memberships, foreign policy -->
- {PolicyType}: {DetailedDescription}
...

### Defense, Military, and Security Policies <!-- e.g. defense budgets, military alliances, security policies, drafts -->
- {PolicyType}: {DetailedDescription}
...

### Immigration Policies <!-- e.g. visa requirements, immigration laws -->
- {PolicyType}: {DetailedDescription}
...

# 11. Public Opinion
## Top Concerns Among Citizens
- {Concern}: {Percentage}
...

## Political Participation
- Age-related Participation: {DetailedDescription}
- Gender-related Participation: {DetailedDescription}
- Ethnic-related Participation: {DetailedDescription}
- Religious-related Participation: {DetailedDescription}

## Latest Polling Data
- Optimistic Perception of Economic Future: {Percentage}
- Direction of Country: {Percentage} believe country is on right track
- Overall Government Approval Rating: {Percentage}
'''