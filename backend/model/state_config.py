from dataclasses import dataclass, field
from typing import List


@dataclass
class StateDimension:
    title: str
    template: str
    seed_assumptions: List[str] = field(default_factory=list)


DIMENSIONS = [
    StateDimension(
        title="People",
        template="""
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

### Ethnic Composition <!-- at least 5 ethnic groups -->
- {EthnicGroup}: {Percentage}
- Two or more ethnicities: {Percentage}
- Others: {Percentage}

### Language Composition <!-- at least 5 languages -->
- {Language}: {Percentage}
- Multilingual: {Percentage}

### Religious Composition <!-- at least 5 religions -->
- {Religion}: {Percentage}
- Unaffiliated/No Religion: {Percentage}

### Housing Composition
- Owned: {Percentage}
- Rented: {Percentage}
- Homeless: {Percentage}
- Other: {Percentage}

### Population Growth
- Population Annual Growth Rate: {Percentage} per year
- Ethnic Population Growth: {DetailedDescription}
- Religious Population Growth: {DetailedDescription}
- Economic Class Population Growth: {DetailedDescription}

## Migration
- Immigration: {DetailedDescription}
- Immigration Sentiment: {DetailedDescription}
- Immigration Totals: {Number} immigrants annually
- Emigration: {DetailedDescription}
- Emigration Sentiment: {DetailedDescription}
- Emigration Totals: {Number} emigrants annually

## People Metrics
- Total Population: {Number} people
- Gallup World Happiness Score: {Number} out of 10
- Access to Improved Water Sources: {Percentage}
- Access to Improved Sanitation: {Percentage}
- Access to Electricity: {Percentage}
- Human Development Index (HDI): {Number}
- Gender Inequality Index (GII): {Number} out of 1.0
- Female Labor Force Participation Rate: {Percentage}
- Social Mobility Index: {Number} out of 100
- LGBTQ+ Legal Equality Index: {Number} out of 100

## Top People Challenges <!-- e.g. migrants, ethnic or class conflicts, discrimination, etc. Severity and detailed description. Avoid cultural challenges. At least 2. -->
- {Challenge}: {DetailedDescription}
""".strip(),
        seed_assumptions=[
            "Assume a population of 25.68 million",
            "Assume a single fictional country-specific ethnic group and several real groups for the others in the country (e.g. White, Asian, etc)",
            "Assume a single fictional country-specific religious group and several real religions for the others in the country (e.g. Christianity, Islam, etc)",
        ],
    ),
    StateDimension(
        title="Education",
        template="""
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

## Top Education Challenges <!-- e.g. high dropout rates, low literacy, etc. Severity and detailed description. At least 2. -->
- {Challenge}: {DetailedDescription}
""".strip(),
    ),
    StateDimension(
        title="Health",
        template="""
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
### Diseases <!-- percentage of population that has this disease -->
- Obesity: {Percentage}
- Mental Health: {Percentage}
- Diabetes: {Percentage}
- Hypertension: {Percentage}
- Asthma: {Percentage}
- Heart Disease: {Percentage}
- Cancer: {Percentage}
- {DiseaseName}: {Percentage}

### Causes of Death Composition <!-- percentage of deaths -->
- Heart Disease: {Percentage}
- Cancer: {Percentage}
- Stroke: {Percentage}
- Diabetes: {Percentage}
- Accidents: {Percentage}
- Suicide: {Percentage}
- {CauseOfDeath}: {Percentage}
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
""".strip(),
    ),
    StateDimension(
        title="Crime",
        template="""
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
""".strip(),
    ),
    StateDimension(
        title="Economy",
        template="""
## Economic System
<!-- describe the economic system in detail, including:
- The role and responsibilities of the government, private sector, and market
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

### Employment by Sector <!-- percentage of workforce -->
- Agriculture: {Percentage}
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

## Government Budget

### Government Revenue Composition <!-- e.g. % of revenue that comes from each source, some may be zero -->
- Income Tax: {Percentage}
- Corporate Tax: {Percentage}
- Sales Tax/VAT: {Percentage}
- Property Tax: {Percentage}
- Capital Gains Tax: {Percentage}
- Import/Export Duties: {Percentage}
- Social Security Contributions: {Percentage}
- Excise Tax: {Percentage}
- Estate/Inheritance Tax: {Percentage}
- Other Tax Revenue: {Percentage}
- Non-Tax Revenue from State-Owned Enterprises: {Percentage}
- Non-Tax Revenue from Natural Resources: {Percentage}
- Non-Tax Revenue from Government Services: {Percentage}
- Non-Tax Revenue from Fines and Penalties: {Percentage}
- Non-Tax Revenue from Investment Income: {Percentage}
- Other Revenue Sources: {Percentage}

### Government Expenditure Composition <!-- e.g. % of expenditure that goes to each category, some may be zero -->
- Healthcare Expenditure: {Percentage}
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

### Government Budget Metrics
- Total Annual Revenue: {TotalAmountInUSD}
- Total Annual Expenditure: {TotalAmountInUSD}

## Trade <!-- good types include electronics, rare metals, grain, oil, etc. at least 5 imports and 5 exports -->
### Export Goods Composition <!-- e.g. % of exports that come from each good type -->
- {GoodType}: {Percentage}
- Other Export Goods: {Percentage}

### Import Goods Composition <!-- e.g. % of imports that come from each good type -->
- {GoodType}: {Percentage}
- Other Import Goods: {Percentage}

### Export Partner Composition <!-- e.g. % of exports that come from each country -->
- {Country}: {Percentage}
- Other Export Partners: {Percentage}

### Import Partner Composition <!-- e.g. % of imports that come from each country -->
- {Country}: {Percentage}
- Other Import Partners: {Percentage}

### Trade Metrics
- Total Exports: {TotalAmountInUSD}
- Total Imports: {TotalAmountInUSD}

## Credit Ratings
- Standard & Poor's: {RatingLetters}
- Moody's: {RatingLetters}
- Fitch: {RatingLetters}

## Economic Metrics
- Gross Domestic Product (GDP): {TotalAmountInUSD}
- GDP Annual Growth Rate: {Percentage} per year
- Currency: {CurrencyName} ({CurrencyCode})
- Unemployment Rate: {Percentage}
- Labor Force Participation Rate: {Percentage} <!-- % people ages 15 or older who are employed or seeking work -->
- Poverty Rate: {Percentage}
- Inflation Rate: {Percentage}
- Gini Coefficient: {Number} out of 1.0
- Average Annual Income: {TotalAmountInUSD} per person
- Exchange Rate ({LocalCurrency}/USD): {ExchangeRate}
- Population with Optimistic Perception of Economic Future: {Percentage}

## Top Economic Challenges <!-- e.g. unemployment, inflation, trade imbalances, etc. Severity and detailed description. At least 2. -->
- {Challenge}: {DetailedDescription}
""".strip(),
        seed_assumptions=[
            "Assume an initial GDP of 2,700,000,000 USD",
            "Assume all real countries (e.g. USA, China, Russia, etc) for import and export partners",
        ],
    ),
    StateDimension(
        title="Military and Defense",
        template="""
## Military System
<!-- describe the military system in detail, including:
- The structure and branches
- Nuclear capabilities
- Technological capabilities
- Sources of equipment (e.g. domestically produced, foreign-made, etc.) -->

## Military Personnel and Equipment <!-- some of these may be zero -->
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

## Top Defense Challenges <!-- e.g. terrorism, cyber threats, organized crime, etc. Include risk level and detailed description. At least 2. -->
- {Challenge}: {DetailedDescription}
""".strip(),
    ),
    StateDimension(
        title="Media",
        template="""
## Media Outlets <!-- avoid mentioning proper nouns, just types. Include state vs private ownership. E.g. social media, cable news, etc. -->
- {MediaType}: {DetailedDescription}

## News Coverage Composition <!-- e.g. coverage of issues, % of media time spent on issues -->
- {MediaIssue}: {Percentage}

## TV/Film Topic Composition <!-- e.g. % of recent TV shows, movies, etc. spent on topics. Topics can be state propaganda, dramas, comedies, etc. -->
- {Topic}: {Percentage}

## Media Metrics
- Press Freedom Index: {Number} out of 100
- Digital Divide Index (Infrastructure): {Number} out of 100
- Digital Divide Index (Socioeconomic): {Number} out of 100
- Social Media Usage: {Percentage}
""".strip(),
    ),
    StateDimension(
        title="Culture",
        template="""
## Cultural Identity
<!-- describe the cultural identity of the state in detail, including:
- Traditional Values
- Family Values
- Work Values
- Gender Values
- Religious Values
- National Identity and Patriotism
- Nationalism and National Pride
- Attitudes Toward Other Nations/Cultures
- Historical Memory and National Myths
- Variance in culture and values (among age, gender, ethnicity, etc.)
- Individualism vs Collectivism -->

## Sports and Recreation Composition <!-- e.g. % of population that participates in each activity -->
- {SportOrActivity}: {Percentage}

## Cultural Metrics
- Soft Power Index: {Number} of 100
- International Cultural Centers: {Number}

## Top Cultural Challenges <!-- e.g. cultural preservation, cultural diversity, etc. Severity and detailed description. At least 2. -->
- {Challenge}: {DetailedDescription}
""".strip(),
    ),
    StateDimension(
        title="Geography and Environment",
        template="""
## Geographic Features
<!-- describe the geographic features in detail, including:
- mountains, rivers, lakes, deserts, forests, etc.
- level of pollution
- infrastructure/population near coastlines
- natural resources (and scarcity) -->

## Natural Resource Production
- Oil and Gas: {Number} barrels of oil equivalent per day
- Coal: {Number} tons per day
- Precious Metals (Gold/Silver): {Number} ounces per day
- Industrial Metals (Copper/Iron): {Number} tons per day
- Strategic Metals (Uranium/Rare Earth): {Number} tons per day
- {Resource}: {Number} tons per day

## Environmental Metrics
- Total Land Area: {Number} sq km
- CO2 Emissions: {Number} metric tons per capita
- Particulate Matter (PM2.5): {Number} μg/m3
- Air Quality Index: {Number} out of 500
- Number of Endangered Species: {Number}

## Top Environmental Challenges <!-- e.g. pollution, deforestation, etc. Severity and detailed description. At least 2. -->
- {Challenge}: {DetailedDescription}
""".strip(),
        seed_assumptions=["Assume an area of 520k sq km"],
    ),
    StateDimension(
        title="Infrastructure and Technology",
        template="""
## Infrastructure
<!-- describe the transportation infrastructure in detail, including:
- Transportation infrastructure
- Energy infrastructure
- Communication infrastructure
- Status and quality of roads, public transport, railways, airports, ports and harbors.
- Status and quality of energy infrastructure (e.g. power plants, transmission lines, etc.)
- Status and quality of communication infrastructure (e.g. internet, phone, etc.) -->

## Energy Source Composition <!-- e.g. % of energy energy that comes from each source -->
- Natural Gas: {Percentage}
- Renewable Energy: {Percentage}
- Nuclear Energy: {Percentage}
- Coal: {Percentage}
- Hydroelectric: {Percentage}
- {EnergySource}: {Percentage}

## Technologies <!-- How well or poorly the state is doing in each technology -->
- Artificial Intelligence: {DetailedDescription}
- Quantum Computing: {DetailedDescription}
- Robotics: {DetailedDescription}
- Space Program: {DetailedDescription}
- Biotechnology: {DetailedDescription}
- {Technology}: {DetailedDescription}

## Infrastructure Metrics
- Total Electricity Generation: {Megawatts}
- Mobile Phone Subscriptions: {Percentage}
- Highspeed Internet Access: {Percentage}
- Roads: {Number} km
- Railways: {Number} km
- Airports: {Number}
- Ports and Harbors: {Number}

## Infrastructure Challenges
- {Challenge}: {DetailedDescription}
""".strip(),
    ),
    StateDimension(
        title="Government",
        template="""
## Government System
<!-- describe the government system in detail, including:
- The structure, branches, and powers for each. 
- Governing documents, 
- Political parties, 
- Electoral system, 
- Citizenship process. -->

## Government Metadata
- Government Type: {GovernmentType} <!-- In Title Case, use CIA World Factbook terminology -->
- Head of State/Government: {Title} <!-- role or group title, not name -->
- Country Official Name: {StateName} <!-- The full name of the country -->
- Capital City: {CapitalCity} <!-- The full name of the capital city -->

## Political Participation
- Age-related Participation: {DetailedDescription}
- Gender-related Participation: {DetailedDescription}
- Ethnic-related Participation: {DetailedDescription}
- Religious-related Participation: {DetailedDescription}

## Policies <!-- all policy types should have at least 4 policies, many policies should beunique to this country and some may align with non-western values -->

### Civil Liberties and Political Rights Policies <!-- e.g. freedom or restriction of speech, press, assembly, religion -->
- {PolicyType}: {DetailedDescription}

### Fiscal & Labor Policies <!-- e.g. tax rates, minimum wage, unemployment benefits, government spending priorities -->
- {PolicyType}: {DetailedDescription}

### Monetary Policies <!-- e.g. inflation targets, interest rates -->
- {PolicyType}: {DetailedDescription}

### Trade & Investment Policies <!-- e.g. tariffs, trade agreements, domestic investment incentives, foreign investment regulations -->
- {PolicyType}: {DetailedDescription}

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
""".strip(),
    ),
    StateDimension(
        title="Public Opinion",
        template="""
## Top Concerns Among Citizens <!-- At least 5 concerns, be specific (e.g. high cost of living, high crime rate, etc.) -->
- {Concern}: {Percentage}

## Recent Headlines <!-- At least 5 recent viral headlines -->
- "{Headline}"
""".strip(),
    ),
]
