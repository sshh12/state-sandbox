STATE_TEMPLATE = '''
<!--
- Follow the template exactly. Filling in {values}, keeping text outside of brackets, and replacing ...s.
- You are expected to fill out ALL the fields in the template and keep ALL default attributes.
- Format {Number} like: 123, ~123 million, 0.12, etc. Do not use a percentage or relative values.
- Format {Percentage} like: 12%, ~12%, < 0.1%, etc. Include a percentage sign.
- Format {DetailedDescription} with 1-3 concise sentences. Use technical terms and avoid filler words.
- Format {TotalAmountInUSD} monetary amounts in USD.
- Certain policies, descriptions, and values the answer may be "N/A due to...". For metrics that should exist, but you don't know, use your best guess.
- Do not use *italic* or **bold**. 
- Do not add nested lists or headings not specified in the template.
- Do not include <!-- comments --> in the final output but use them as key guidance.
-->

# 1. State Overview
## Basic Information
- Country Name: {StateName}
- Government Type: {GovernmentType}
- Head of State/Government: {Title} <!-- role or group title, not name -->
- Total Population: {Number} people
- Currency: {CurrencyName} ({CurrencyCode})
- Land Area: {Number} sq km

# 2. People
## Population Distribution
### Age Composition
- 0-4 years: {Percentage}
- 5-17 years: {Percentage}
- 18-24 years: {Percentage}
- 25-44 years: {Percentage}
- 45-64 years: {Percentage}
- 65-74 years: {Percentage}
- 75+ years: {Percentage}

### Gender Composition
- Male: {Percentage}
- Female: {Percentage}
- Other: {Percentage}

### Sexuality Composition
- Heterosexual: {Percentage}
- Lesbian/Gay: {Percentage}
- Bisexual: {Percentage}
- Transgender: {Percentage}
- {Sexuality}: {Percentage}
...

### Urban-Rural Composition
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
- Primary Education Complete: {Percentage} <!-- e.g. elementary school -->
- Secondary Education Complete: {Percentage} <!-- e.g. high school -->
- Tertiary Education Complete: {Percentage} <!-- e.g. college -->
- Graduate Degree Complete: {Percentage} <!-- e.g. PhD, Masters, etc. -->

### Ethnic Composition
- {EthnicGroup}: {Percentage}
...
- Two or more ethnicities: {Percentage}
- Others: {Percentage}

### Language Composition
- {Language}: {Percentage}
...
- Multilingual: {Percentage}

### Religious Composition
- {Religion}: {Percentage}
...
- Unaffiliated/No Religion: {Percentage}

### Housing Composition
- Owned: {Percentage}
- Rented: {Percentage}
- Homeless: {Percentage}
- Other: {Percentage}

### Population Growth
- Overall Population Growth Rate: {Percentage} per year
- Ethnic Population Growth: {DetailedDescription} <!-- e.g. how growth is distributed among ethnic groups -->
- Religious Population Growth: {DetailedDescription}
- Economic Class Population Growth: {DetailedDescription}

## Migration
- Immigration: {DetailedDescription} <!-- e.g. legal, illegal, etc. and from where -->
- Immigration Sentiment: {DetailedDescription} <!-- e.g. how do citizens feel about immigrants -->
- Immigration Totals: {Number} immigrants annually
- Emigration: {DetailedDescription}
- Emigration Sentiment: {DetailedDescription} <!-- e.g. how do citizens feel about emigrants -->
- Emigration Totals: {Number} emigrants annually

## People Metrics
- Gallup World Happiness Score: {Number} out of 10
- Access to Improved Water Sources: {Percentage}
- Access to Improved Sanitation: {Percentage}
- Access to Electricity: {Percentage}
- Human Development Index (HDI): {Number}
- Gender Inequality Index (GII): {Number} out of 1.0
- Female Labor Force Participation Rate: {Percentage}
- Social Mobility Index: {Number} out of 100
- LGBTQ+ Legal Equality Index: {Number} out of 100

## Top People Challenges <!-- e.g. discrimination, etc. Severity and detailed description. Avoid cultural challenges. At least 2. -->
- {Challenge}: {DetailedDescription}
...

# 3. Education
## Education System
<!-- describe the education system in detail, including:
- Levels of education
- Types of schools
- Funding
- Curriculum -->

## Literacy
- Adult Literacy Rate: {Percentage}
- Ethnic Literacy: {DetailedDescription} <!-- relationship between literacy and ethnicity -->

## Education Metrics
- Average Years of Schooling: {Number} years
- Gender Parity Index in Education: {Number}
- University Enrollment Rate: {Percentage}
- Primary Schools: {Number}
- Secondary Schools: {Number}
- Universities: {Number}

# 4. Health
## Health System
<!-- describe the health system in detail, including:
- Insurance
- State involvement
- Accessibility
- Waiting times
- Specialized services
- Technological capabilities
- Quality -->

## Life Expectancy
- Average Life Expectancy at Birth: {Number} years
- Male Life Expectancy: {Number} years
- Female Life Expectancy: {Number} years
- Ethnic Life Expectancy: {DetailedDescription} <!-- relationship between life expectancy and ethnicity -->

## Health Statistics
### Diseases
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
- Heart Disease: {Percentage} <!-- percentage of deaths -->
- Cancer: {Percentage}
- Stroke: {Percentage}
- Diabetes: {Percentage}
- Accidents: {Percentage}
- Suicide: {Percentage}
- {CauseOfDeath}: {Percentage}
...
- Other Causes: {Percentage}

## Health Metrics
- Infant Mortality Rate: {Number} per 1,000 live births
- Total Fertility Rate: {Number} children per woman
- Gross Reproduction Rate: {Number} female children per woman
- Maternal Mortality Rate: {Number} per 100,000 live births
- Child Mortality Rate: {Number} per 1,000 live births
- Physician Density: {Number} per 1,000 population
- Hospital Bed Density: {Number} per 1,000 population

## Top Health Challenges <!-- e.g. high healthcare costs, pandemics, etc. Severity and detailed description. At least 2. -->
- {Challenge}: {DetailedDescription}
...

# 5. Crime
## Justice System
<!-- describe the justice system in detail, including:
- The role, organization, and responsibilities of the courts
- The role, organization, and responsibilities of law enforcement
- The role, organization, and responsibilities of the prisons
- Funding -->

## Crime Metrics
- Population Incarcerated: {Percentage}
- Prison Capacity: {Percentage}
- Gun Ownership Rate: {Percentage}
- Violent Crimes: {Number} per 100,000 population
- Property Crimes: {Number} per 100,000 population
- Financial Crimes: {Number} per 100,000 population
- Drug-Related Crimes: {Number} per 100,000 population
- Cybercrime: {Number} per 100,000 population
- Sexual Crimes: {Number} per 100,000 population
- Organized Crime: {Number} per 100,000 population
- Public Order Crimes: {Number} per 100,000 population
- White-Collar Crimes: {Number} per 100,000 population
- State/Political Crimes: {Number} per 100,000 population

## Top Crime Challenges <!-- e.g. high crime rates, drug trafficking, etc. Severity and detailed description. At least 2. -->
- {Challenge}: {DetailedDescription}
...

# 6. Economy
## Economic System
<!-- describe the economic system in detail, including:
- The role and responsibilities of the government, the private sector, and the market 
- Compare and contrast to socialist/communist/free-market/etc. systems
- The role of the central bank (if any) -->

## Sectors
### Industries  <!-- e.g. for each sector describe industries, ownership, and specializations within it, some sectors may be nearly nonexistent -->
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
- Agriculture: {Percentage} <!-- percentage of GDP -->
- Services: {Percentage}
- Manufacturing: {Percentage}
- Construction: {Percentage}
- Mining: {Percentage}
- Financial Services: {Percentage}
- Real Estate: {Percentage}
- Technology: {Percentage}
- Transportation: {Percentage}
- Wholesale and Retail Trade: {Percentage}
- Tourism and Hospitality: {Percentage}
- {Sector}: {Percentage}
...

### Employment by Sector
- Agriculture: {Percentage} <!-- percentage of workforce -->
- Services: {Percentage}
- Manufacturing: {Percentage}
- Construction: {Percentage}
- Mining: {Percentage}
- Financial Services: {Percentage}
- Real Estate: {Percentage}
- Technology: {Percentage}
- Transportation: {Percentage}
- Wholesale and Retail Trade: {Percentage}
- Tourism and Hospitality: {Percentage}
- {Sector}: {Percentage}
...

## Government Budget
### Revenue
- Total Annual Revenue: {TotalAmountInUSD} 
  - Income Tax: {Percentage} <!-- note that some of these could be zero -->
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
- Total Annual Expenditure: {TotalAmountInUSD} 
  - Healthcare Expenditure: {Percentage} <!-- note that some of these could be zero -->
  - Education Expenditure: {Percentage}
  - Defense and Military Expenditure: {Percentage}
  - Infrastructure Expenditure: {Percentage}
  - Social Welfare Expenditure: {Percentage}
  - Environmental Protection Expenditure: {Percentage}
  - Public Safety and Law Enforcement Expenditure: {Percentage}
  - Housing and Urban Development Expenditure: {Percentage}
  - Agriculture and Rural Development Expenditure: {Percentage}
  - Debt Service (Interest Payments) Expenditure: {Percentage}
  - {ExpenditureCategory}: {Percentage}
  ...

## Trade <!-- good types include electronics, rare metals, grain, oil, etc. at least 5 imports and 5 exports -->
### Imports and Exports
- Total Exports: {TotalAmountInUSD}
  - Exports of {GoodType}: {Percentage}
  ...
  - Other Exports: {Percentage}
- Total Imports: {TotalAmountInUSD}
  - Imports for {GoodType}: {Percentage}
  ...
  - Other Imports: {Percentage}

### Trade Partners
- Export Partners
  - {Country}: {Percentage}
  ...
  - Other Export Partners: {Percentage}
- Import Partners
  - {Country}: {Percentage}
  ...
  - Other Import Partners: {Percentage}

## Credit Ratings
- Standard & Poor's: {RatingLetters}
- Moody's: {RatingLetters}
- Fitch: {RatingLetters}

## Economic Metrics
- Gross Domestic Product (GDP): {TotalAmountInUSD}
- GDP Growth Rate: {Percentage} per year
- Unemployment Rate: {Percentage}
- Labor Force Participation Rate: {Percentage} <!-- % people ages 15 or older who are employed or seeking work -->
- Poverty Rate: {Percentage}
- Inflation Rate: {Percentage}
- Gini Coefficient: {Number} out of 1.0
- Average Income: {TotalAmountInUSD} per person
- Exchange Rate ({LocalCurrency}/USD): {ExchangeRate}
- Population with Optimistic Perception of Economic Future: {Percentage}

## Top Economic Challenges <!-- e.g. unemployment, inflation, etc. Severity and detailed description. At least 2. -->
- {Challenge}: {DetailedDescription}
...

# 7. Military and Defense
## Military System
<!-- describe the military system in detail, including:
- The structure and branches
- Nuclear capabilities
- Technological capabilities
- Sources of equipment (e.g. domestically produced, foreign-made, etc.) -->

## Military Metrics <!-- some of these may be zero -->
- Active Duty Personnel: {Number}
- Reserve Personnel: {Number}
- Fighter Jets: {Number}
- Bombers: {Number}
- UAVs: {Number}
- Helicopters: {Number}
- Transport Aircraft: {Number}
- Aircraft Carriers: {Number}
- Nuclear Submarines: {Number}
- Destroyers: {Number}
- Frigates: {Number}
- Tanks: {Number}
- Artillery Systems: {Number}
- Infantry Fighting Vehicles: {Number}
- Armored Personnel Carriers: {Number}
- Nuclear ICMBs: {Number}
- Ballistic Missiles: {Number}
- Anti-Ballistic Missile Systems: {Number}
- Cyber Defense Specialists: {Number}
- Reconnaissance Satellites: {Number}
- Communication Satellites: {Number}

### Top Defense Challenges <!-- e.g. terrorism, cyber threats, organized crime, etc. Include risk level and detailed description. At least 2. -->
- {Challenge}: {DetailedDescription}
...

# 8. Media
## Media Outlets <!-- avoid mentioning proper nouns, just types. Include state vs private ownership. -->
- {MediaType}: {DetailedDescription}
...

### Media Coverage <!-- e.g. coverage of issues, % of media time spent on issues -->
- {MediaIssue}: {Percentage}
...

## Media Metrics
- Press Freedom Index: {Number} out of 100
- Digital Divide Index (Infrastructure): {Number} out of 100
- Digital Divide Index (Socioeconomic): {Number} out of 100
- Social Media Usage: {Percentage}

# 9. Culture
## Cultural Identity
### Cultural Values
- Traditional Values: {DetailedDescription}
- Family Values: {DetailedDescription}
- Work Values: {DetailedDescription}
- Gender Values: {DetailedDescription}
- Religious Values: {DetailedDescription}
- Individualism vs Collectivism: {DetailedDescription}

### Sports and Recreation
- {SportOrActivity}: {DetailedDescription}
...

## Cultural Metrics
- Soft Power Index: {Number} of 100
- International Cultural Centers: {Number}

## Top Cultural Challenges <!-- e.g. cultural preservation, cultural diversity, etc. Severity and detailed description. At least 2. -->
- {Challenge}: {DetailedDescription}
...

# 10. Geography and Environment
## Geographic Features
<!-- describe the geographic features in detail, including:
- mountains, rivers, lakes, deserts, forests, etc.
- level of pollution
- infrastructure/population near coastlines
- natural resources (and scarcity) -->

## Natural Resource Production <!-- some of these may be zero -->
- Oil and Gas: {Number} barrels of oil equivalent per day
- Coal: {Number} tons per day
- Precious Metals (Gold/Silver): {Number} ounces per day
- Industrial Metals (Copper/Iron): {Number} tons per day
- Strategic Metals (Uranium/Rare Earth): {Number} tons per day
- {Resource}: {Number} tons per day
...

## Environmental Metrics
- CO2 Emissions: {Number} metric tons per capita
- Particulate Matter (PM2.5): {Number} μg/m3
- Air Quality Index: {Number} out of 500
- Number of Endangered Species: {Number}

## Top Environmental Challenges <!-- e.g. deforestation, pollution, etc. Severity and detailed description. At least 2. -->
- {Challenge}: {DetailedDescription}
...

# 11. Infrastructure and Technology
## Transportation Infrastructure
<!-- describe the transportation infrastructure in detail, including:
- Status, quality, and quantity of roads, public transport, railways, airports, ports and harbors. -->

## Energy Sources
- Natural Gas: {Percentage}
- Renewable Energy: {Percentage}
- Nuclear Energy: {Percentage}
- Coal: {Percentage}
- Hydroelectric: {Percentage}
- {EnergySource}: {Percentage}
...

## Technologies
- Artificial Intelligence: {DetailedDescription}
- Quantum Computing: {DetailedDescription}
- Robotics: {DetailedDescription}
- Space Program: {DetailedDescription}
- Biotechnology: {DetailedDescription}
- {Technology}: {DetailedDescription}
...

## Infrastucture Metrics
- Total Electricity Generation: {Megawatts}
- Mobile Phone Subscriptions: {Percentage}
- Highspeed Internet Access: {Percentage}
- Roads: {Number} km
- Railways: {Number} km
- Airports: {Number}
- Ports and Harbors: {Number}

## Infrastructure Challenges <!-- e.g. infrastructure decay, lack of infrastructure, etc. Severity and detailed description. At least 2. -->
- {Challenge}: {DetailedDescription}
...

# 12. Government
## Government System
<!-- describe the government system in detail, including:
- The structure, branches, and powers for each. 
- Governing documents, 
- Political parties, 
- Electoral system, 
- Citizenship process. -->

## Political Participation
- Age-related Participation: {DetailedDescription}
- Gender-related Participation: {DetailedDescription}
- Ethnic-related Participation: {DetailedDescription}
- Religious-related Participation: {DetailedDescription}

## Policies <!-- all policy types should have at least 4 policies, can include both "good" and "bad" policies -->

### Civil Liberties and Political Rights Policies <!-- e.g. freedom or restriction of speech, press, assembly, religion -->
- {PolicyType}: {DetailedDescription}
...

### Fiscal & Labor Policies <!-- e.g. tax rates, minimum wage, unemployment benefits, government spending priorities -->
- {PolicyType}: {DetailedDescription}
...

### Monetary Policies <!-- e.g. inflation targets, interest rates -->
- {PolicyType}: {DetailedDescription}
...

### Trade & Investment Policies <!-- e.g. tariffs, trade agreements, domestic investment incentives, foreign investment regulations -->
- {PolicyType}: {DetailedDescription}
...

### Education Policies <!-- e.g. school systems, educational reforms -->
- {PolicyType}: {DetailedDescription}
...

### Healthcare Policies <!-- e.g. healthcare systems, healthcare reforms -->
- {PolicyType}: {DetailedDescription}
...

### Criminal Justice Policies <!-- e.g. police forces, prisons, courts, drug laws, substance abuse policies, etc. -->
- {PolicyType}: {DetailedDescription}
...

### Housing Policies <!-- e.g. housing policies, housing reforms -->
- {PolicyType}: {DetailedDescription}
...

### Media Policies <!-- e.g. media regulations, media ownership -->
- {PolicyType}: {DetailedDescription}
...

### Social & Cultural Policies <!-- e.g. social security systems, social welfare programs, equality laws, cultural policies, cultural reforms -->
- {PolicyType}: {DetailedDescription}
...

### Environmental Policies <!-- e.g. international agreements, carbon pricing, industrial emissions regulations, waste management, conservation laws -->
- {PolicyType}: {DetailedDescription}
...

### Diplomatic Policies <!-- e.g. alliances, memberships, foreign policy -->
- {PolicyType}: {DetailedDescription}
...

### Defense Policies <!-- e.g. defense budgets, military alliances, security policies, drafts -->
- {PolicyType}: {DetailedDescription}
...

### Immigration Policies <!-- e.g. visa requirements, immigration laws -->
- {PolicyType}: {DetailedDescription}
...

## Government Metrics
- Corruption Perception Index (CPI): {Number} out of 100
- Direction of Country: {Percentage} believe country is on right track
- Overall Head of State/Government Approval Rating: {Percentage}

## Top Government Challenges <!-- e.g. corruption, political instability, etc. Severity and detailed description. At least 2. -->
- {Challenge}: {DetailedDescription}
...

# 13. Public Opinion
## Top Concerns Among Citizens <!-- At least 5 concerns -->
- {Concern}: {Percentage}
...

## Recent Headlines <!-- At least 3 recent viral headlines -->
- "{Headline}"
...
'''.strip()

RANDOM_TEMPLATE = '''
<!--
- Event categories must be mutually exclusive and must include a first no-event category.
- Events can be good, bad, or mixed.
- Probabilities and events should be influenced and personalized by the <state>.
- Probabilities must be as real-world realistic as possible.
- Include varients of events (e.g. Cat 1 Hurricane, Cat 2 Hurricane, etc.) or joint events (e.g. Hurricane + Earthquake).
- Include at least 10 events per category.
- Events should be UNRELATED to the government (no new policies, laws, etc.).
- Events should be consise and unambiguous (no "... changes", it should state what the change is).
- Events that last longer than a month should be stated as "starts" (or existing events "ends").
- Do not add nested lists or headings not specified in the template.
- Do not include <!-- comments --> in the final output but use them as key guidance.
- Do not use *italic* or **bold**. 
-->

# Environmental Events <!-- natural phenomena affecting environment/climate -->
- {%} No notable environmental events
...

# Defense & Military Events <!-- military/security incidents or developments -->
- {%} No notable defense/military events
...

# Economic Events <!-- major financial/market/business developments -->
- {%} No notable economic events
...

# Heath Events <!-- public health/medical developments -->
- {%} No notable health events
...

# Cultural & Social Events <!-- societal/cultural developments -->
- {%} No notable social events
...

# Infrastructure & Technology Events <!-- tech/scientific developments -->
- {%} No notable infrastructure/technology events
...

# International Events <!-- foreign relations/global developments by OTHER nations -->
- {%} No notable international events
...
'''.strip()

DIFF_EXECUTIVE_TEMPLATE = '''
<!--
- This is a report to state leadership on the changes to the <state> over the last month.
- Do not add nested lists or headings not specified in the template.
- Do not include <!-- comments --> in the final output but use them as key guidance.
- You should include what changes, why it changes, and notable metrics that will reflect the change.
- Focus on the most important events, some might not be that important for the leadership.
- Some sections may be empty if nothing relevant changed. You can re-arrange the sections to focus on the most important updates.
-->

### Executive Summary

<!-- 1 - 2 sentence dense technical overview of what *important* happened, address to the leadership of the <state> -->

1. **Economy**:
  - <!-- *Title* -->: <!-- Description -->
  - ...
2. **Social & Cultural**:
  - <!-- *Title* -->: <!-- Description -->
  - ...
3. **Health & Crime**:
  - <!-- *Title* -->: <!-- Description -->
  - ...
4. **Defense & Military**:
  - <!-- *Title* -->: <!-- Description -->
  - ...
5. **Infrastructure & Technology**:
  - <!-- *Title* -->: <!-- Description -->
  - ...
5. **International Relations**:
  - <!-- *Title* -->: <!-- Description -->
  - ...
'''.strip()

DIFF_TEMPLATE = '''
<!--
- Detailed line-by-line diff of the <state>. ALL items in <state> should be included.
- Note both what changes and what didn't change. ALL changes should include at least a brief explanation.
- Be realistic about what could have changed and the amount of change
- Use the same formatting/categories as the <state>.
- Do not include <!-- comments --> in the final output but use them as key guidance.
- Do not use *italic* or **bold**. 
-->

...# Topic <!-- for all the headers in the <state> -->
Key: Value1 -> Value2 (due to ...) <!-- example of change with detailed explanation -->
Key: Value (no change) <!-- example of no change -->
Key: (new) Value (due to ...) <!-- example of a new field that was added to a list -->
(removed Key due to ...) <!-- example of a field that was removed from a list -->
...
'''.strip()
