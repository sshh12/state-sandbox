STATE_TEMPLATE = '''
<!--
- You can format numbers as like: 123, ~123 million, etc. Do not use a percentage unless specified.
- All monetary amounts should be in USD
- For certain policies, descriptions, and values the answer may be "N/A due to..."
- Use "subgroups" to identify variance among specific sub-populations
- You are expected to fill out all the fields in the template and keep all default attributes
- Do not use *italic* or **bold**
-->

# 1. Nation Overview
## Basic Information
- Country Name: {NationName}
- Government Type: {GovernmentType}
- Head of State/Government: {LeaderNameandTitle}
- Capital City: {CapitalCity}
- Total Population: {AbsoluteNumber}
- Currency: {CurrencyName} ({CurrencyCode})
- Land Area: {Areainsqkm}
- National Holidays: {ListOfHolidays}

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

### Sexuality Composition
- Heterosexual: {Percentage}
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
- {Ethnic Group A}: {Percentage}
- {Ethnic ...}: {Percentage}
...
- Others: {Percentage}

### Language Composition
- {Language ...}: {Percentage}
...
- Multilingual: {Percentage}

### Religious Composition
- {Religion ...}: {Percentage}
...
- Unaffiliated/No Religion: {Percentage}

## Life Expectancy
- Average Life Expectancy at Birth: {NumberofYears}
- Male Life Expectancy: {NumberofYears}
- Female Life Expectancy: {NumberofYears}
- Infant Mortality Rate: {Number} per 1,000 live births
- Total Fertility Rate: {Number} children per woman
- Gross Reproduction Rate: {Number} female children per woman
- Subgroup Life Expectancy
  - {Subgroup ...} Life Expectancy: {NumberofYears}
  ...

## Population Growth
- Overall Population Growth Rate: {PercentagePerYear}
- Subgroup Population Growth Rate
  - {Subgroup ...} Population Growth Rate: {PercentagePerYear}
  ...

## Migration
- Net Migration Rate: {Number} per 1,000 population
- Immigration: {DetailedDescription}
- Emigration: {DetailedDescription}

# 3. Economy
## Economic Indicators
- Gross Domestic Product (GDP in USD): {TotalAmountInUSD}
- GDP Growth Rate: {PercentagePerYear}
- Credit Ratings:
  - Standard & Poor's: {RatingLetters}
  - Moody's: {RatingLetters}
  - Fitch: {RatingLetters}
- Unemployment Rate: {Percentage}
- Inflation Rate: {Percentage}
- Poverty Rate: {Percentage}
- Gini Coefficient: {Value} out of 1.0

## Sector Contributions to GDP
- {Sector/Industry ...}: {Percentage} of GDP
...

## Government Budget
### Revenue & Expenditure
- Total Revenue: {TotalAmountInUSD}
  - Tax Review From {Category}: {TotalAmountInUSD}
  ...
  - Non-Tax Review From {Category}: {TotalAmountInUSD}
  ...
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
- {ThreatType/Group ...}: {DetailedDescription}
...

# 5. Government Policies
## Political Policies
- Government Structure: {DetailedDescription}
- Subgroups
  - {Branch/Subgroup ...}: {DetailedDescriptionOfRuleAndPowers}
  ...
- Parties: {Ruling PartyName(s), Opposition PartyName(s)}
- Electoral System: {DetailedDescription}

### Civil Liberties and Political Rights
- Corruption Perception Index (CPI): {Value} out of 100
- Freedom of Speech and Press: {StatusDescription}
- Freedom of {FreedomType}: {StatusDescription}
...

## Economic Policies
### Fiscal Policy
- Taxation Policies: {DetailedDescription}
- Government Spending Priorities: {MajorSectors}
- {PolicyType ...}: {DetailedDescription}
...

### Monetary Policy
- Inflation Targets: {DetailedDescription}
- {PolicyType ...}: {DetailedDescription}
...

### Labor Market Policies
- Minimum Wage: {ValueOrStatusDescription}
- {PolicyType ...}: {DetailedDescription}
...

### Trade Policies
- Tariffs and Quotas: {DetailedDescription}
- {PolicyType ...}: {DetailedDescription}
...

### Investment Policies
- Domestic Investment Incentives: {DetailedDescription}
- {PolicyType ...}: {DetailedDescription}
...

## Social Policies
### Education System
- Structure: {DetailedDescription}
- Key Initiatives: {ListOfInitiatives}
- {PolicyType ...}: {DetailedDescription}
...

### Healthcare System
- System: {DetailedDescription}
- Healthcare Budget: {Percentage} of GDP
- Public Health Initiatives: {ListOfInitiatives}
- {PolicyType ...}: {DetailedDescription}
...

### Social Welfare Programs
- Unemployment Assistance: {DetailedDescription}
- Pension Systems: {DetailedDescription}
- Social Security Nets: {DetailedDescription}
- {PolicyType ...}: {DetailedDescription}
...

### Housing Policies
- Urban Development Plans: {DetailedDescription}
- {PolicyType ...}: {DetailedDescription}
...

## Environmental Policies
### Climate
- International Agreements: {DetailedDescription}
- National Emission Targets: {DetailedDescription}
- Renewable Energy Targets: {DetailedDescription}
- {PolicyType ...}: {DetailedDescription}
...

### Pollution Control Measures
- Industrial Emissions Regulations: {DetailedDescription}
- Waste Management Policies: {DetailedDescription}
- {PolicyType ...}: {DetailedDescription}
...

### Conservation
- {PolicyType ...}: {DetailedDescription}
...

## Foreign Policies
### Diplomatic Relations
- Alliances and Memberships: {DetailedDescription}

### Defense and Security Policies
- {PolicyType ...}: {DetailedDescription}
...

### Immigration Policies
- Visa Requirements: {DetailedDescription}
- {PolicyType ...}: {DetailedDescription}
...

# 6. Social Indicators
## Education Indicators
- Adult Literacy Rate: {Percentage}
- Average Years of Schooling: {NumberofYears}
- Gender Parity Index in Education: {Value}
- Overall Literacy Rate: {Percentage}
- Subgroup Literacy Rates
  - {Subgroup ...} Literacy Rate: {Percentage}
  ...

## Health Indicators
- Maternal Mortality Rate: {Number} per 100,000 live births
- Child Mortality Rate: {Number} per 1,000 live births
- Physician Density: {Number} per 1,000 population
- Hospital Bed Density: {Number} per 1,000 population

### Prevalence of Diseases
- {DiseaseName}: {Number} per 100,000 population
...

## Standard of Living
- Access to Improved Water Sources: {Percentage}
- Access to Improved Sanitation: {Percentage}
- Access to Electricity: {Percentage}
- Human Development Index (HDI): {Value}

## Crime and Safety
- Overall Crime Rate: {Number} per 100,000 population

### Crime Composition
- {CrimeType ...}: {Number} per 100,000 population
...

## Gender Equality
- Gender Inequality Index (GII): {Value} out of 1.0
- Female Labor Force Participation Rate: {Percentage}

# 7. Health and Causes of Death
## Leading Causes of Death
- {Cause ...}: {Percentage} of deaths
...
- Other Causes: {Percentage}

## Health Challenges
- Epidemics/Pandemics: {CurrentStatus}
- Lifestyle Diseases: {DetailedDescriptionAndPrevalence}
- Mental Health Issues: {DetailedDescriptionAndPrevalence}
- Healthcare Accessibility: {SubGroupDisparities}

# 7. Industry Ownership and GDP Breakdown
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

# 8. Infrastructure and Technology
## Transportation Infrastructure
- Road Network: {StatusAndDetailedDescription}
- Railways: {StatusAndDetailedDescription}
- Airports: {StatusAndDetailedDescription}
- Ports and Harbors: {StatusAndDetailedDescription}
- {InfrastructureType ...}: {StatusAndDetailedDescription}
...

## Energy Infrastructure
- Total Electricity Generation: {Megawatts}
- Electricity Generation Breakdown
  - {EnergySource ...}: {Megawatts}
  ...

## Telecommunications
- Internet Penetration Rate: {Percentage}
- Broadband Subscriptions: {Number} per 100 inhabitants
- Mobile Phone Subscriptions: {Number} per 100 inhabitants
- Highspeed Internet Access: {Number} per 100 inhabitants

## Technology and Innovation
- R&D Expenditure: {Percentage} of GDP
- Patents Filed Annually: {AbsoluteNumber}
- Space Program: {DetailedDescription}

# 9. Public Opinion and Citizen Sentiment
## Top Concerns Among Citizens
- {Concern ...}: {Percentage}
...

## Latest Polling Data
- Optimistic Perception of Economic Future: {Percentage}
- Overall Government Approval Rating: {Percentage}
- Institution Approval Ratings  
  - {Institution ...} Approval Rating: {Percentage}
  ...
'''