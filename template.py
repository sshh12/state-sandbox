STATE_TEMPLATE = '''
<!--
- You can format {AbsoluteNumber}s as: 123, ~123 million, ~123B (DO NOT include percentages)
- All monetary amounts should be in USD
- For certain policies or descriptions the answer may be "N/A due to..."
- Use "subgroups" to identify variance among specific populations
- You are expected to fill out all the fields in the template and keep all default attributes
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

# 2. Demographics
## Population Distribution
### Age Groups
- 0-4 years (Pre-school): {AbsoluteNumber}
- 5-17 years (School-age): {AbsoluteNumber}
- 18-24 years (Higher Education/Early Career): {AbsoluteNumber}
- 25-44 years (Early/Mid Career): {AbsoluteNumber}
- 45-64 years (Late Career): {AbsoluteNumber}
- 65-74 years (Early Retirement): {AbsoluteNumber}
- 75+ years (Late Retirement): {AbsoluteNumber}

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

### Religious Composition
- {Religion A}: {Percentage}
- {Religion ...}: {Percentage}
...
- Unaffiliated/No Religion: {Percentage}

## Life Expectancy
- Average Life Expectancy at Birth: {NumberofYears}
- Male Life Expectancy: {NumberofYears}
- Female Life Expectancy: {NumberofYears}
- Subgroup Life Expectancy
  - {Subgroup ...} Life Expectancy: {NumberofYears}
  ...

## Population Growth
- Overall Population Growth Rate: {PercentagePerYear}
- Subgroup Population Growth Rate
  - {Subgroup ...} Population Growth Rate: {PercentagePerYear}
  ...

# 3. Economy
## Economic Indicators
- Gross Domestic Product (GDP in USD): {TotalAmountInUSD}
- GDP Growth Rate: {PercentagePerYear}
- Unemployment Rate: {Percentage}
- Inflation Rate: {Percentage}
- Poverty Rate: {Percentage}
- Gini Coefficient: {Value}

## Sector Contributions to GDP
- Agriculture: {Percentage} of GDP
- {Sector/Industry ...}: {Percentage} of GDP
...

## Government Budget
### Revenue & Expenditure
- Total Revenue: {TotalAmountInUSD}
  - Tax Review From {Category}: {TotalAmountInUSD}
  - Non-Tax Review From {Category}: {TotalAmountInUSD}
...
- Total Expenditure: {TotalAmountInUSD}
  - Expenditure on {Category}: {TotalAmountInUSD}
...
- Budget Surplus/Deficit: {TotalAmountInUSD}
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
- {LocalCurrency}/USD = {ExchangeRate} ({Fixed}, {Floating}, {Pegged})
- {LocalCurrency}/{ForeignCurrency} = {ExchangeRate} ({Fixed}, {Floating}, {Pegged})
...

# 4. Government Policies
## Political Policies
- Government Structure: {DetailedDescription}
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
- Healthcare Spending: {TotalAmountInUSD}
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
### Climate Change
- International Agreements: {ListOfAgreements}
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
- Defense Budget: {TotalAmountInUSD}
- Military Structure: {DetailedDescription}
- {PolicyType ...}: {DetailedDescription}
...

### Immigration Policies
- Visa Requirements: {DetailedDescription}
- {PolicyType ...}: {DetailedDescription}
...

# 5. Social Indicators
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

### Prevalence of Diseases
- {DiseaseName}: {Percentage}
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

# 6. Health and Causes of Death
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

### Electricity Generation Breakdown
- Electricity Generation By {EnergySource ...}: {Megawatts}
...

## Telecommunications
- Internet Penetration Rate: {Percentage}
- Broadband Subscriptions: {Number} per 100 inhabitants
- Mobile Phone Subscriptions: {Number} per 100 inhabitants

## Technology and Innovation
- R&D Expenditure: {TotalAmountInUSD}
- Patents Filed Annually: {AbsoluteNumber}

# 9. Public Opinion and Citizen Sentiment
## Top Concerns Among Citizens
- {Concern ...}: {Percentage}
...

## Recent Polling Data
- Optimistic Perception of Economic Future: {Percentage}
- Overall Government Approval Rating: {Percentage}
- Institution Approval Ratings  
  - {Institution ...} Approval Rating: {Percentage}
  ...
'''