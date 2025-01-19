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
- Ethnic Population Growth: {Description}
- Religious Population Growth: {Description}
- Economic Class Population Growth: {Description}

## Migration
<!-- describe the migration patterns (migrating to this state) in detail, including:
- The types of people migrating (e.g. refugees, economic migrants, etc.) and ethnicity
- The sources of migrants (e.g. neighboring countries, distant regions, etc.)
- The destinations of migrants (e.g. urban areas, rural areas, etc.)
- The jobs and industries -->

## People Metrics
- Total Population: {Number} people
- Gallup World Happiness Score: {Number} out of 10
- Human Development Index (HDI): {Number}
- Gender Inequality Index (GII): {Number} out of 1.0
- Female Labor Force Participation Rate: {Percentage}
- Social Mobility Index: {Number} out of 100
- LGBTQ+ Legal Equality Index: {Number} out of 100

## Top People Challenges <!-- e.g. migrants, ethnic or class conflicts, discrimination, etc. Severity and detailed description. Avoid cultural challenges. At least 2. -->
- {Challenge}: {Description}
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
- Ethnic Literacy: {Description} <!-- relationship between literacy and ethnicity -->

## Education Metrics
- Average Years of Schooling: {Number} years
- Gender Parity Index in Education: {Number}
- University Enrollment Rate: {Percentage}
- Primary Schools: {Number}
- Secondary Schools: {Number}
- Universities: {Number}

## Top Education Challenges <!-- e.g. high dropout rates, low literacy, etc. Severity and detailed description. At least 2. -->
- {Challenge}: {Description}
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
- Ethnic Life Expectancy: {Description} <!-- relationship between life expectancy and ethnicity -->

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
...

### Causes of Death Composition <!-- percentage of deaths -->
- Heart Disease: {Percentage}
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
- {Challenge}: {Description}
""".strip(),
    ),
    StateDimension(
        title="Crime",
        template="""
## Justice System
<!-- describe the justice system in detail, including:
- The role, organization, and responsibilities of the courts (if any)
- The role, organization, and responsibilities of law enforcement (if any)
- The role, organization, and responsibilities of the prisons (if any)
- The correlation between crime and poverty, education, and other factors -->
- Government funding -->

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

## Black Market
<!-- describe the black market in detail, including:
- The types of goods and services sold (methods, sources, prices, etc.)
- The enforcement of the black market
- The impact of the black market on the economy -->

## Top Crime Challenges <!-- e.g. high crime rates, drug trafficking, etc. Severity and detailed description. At least 2. -->
- {Challenge}: {Description}
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
- Agriculture: {Description}
- Services: {Description}
- Manufacturing: {Description}
- Construction: {Description}
- Mining: {Description}
- Financial Services: {Description}
- Real Estate: {Description}
- Technology: {Description}
- Transportation: {Description}
- Wholesale and Retail Trade: {Description}
- Tourism and Hospitality: {Description}
- {Sector}: {Description}
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
...

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
- {RevenueSource}: {Percentage}
...
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
...
- Other Expenditure: {Percentage}

### Government Budget Metrics
- Total Annual Revenue: {AmountUSD}
- Total Annual Expenditure: {AmountUSD}

## Credit Ratings
- Standard & Poor's: {RatingLetters}
- Moody's: {RatingLetters}
- Fitch: {RatingLetters}

## Economic Metrics
- Gross Domestic Product (GDP): {AmountUSD}
- GDP Annual Growth Rate: {Percentage} per year
- Currency: {CurrencyName} ({CurrencyCode})
- Unemployment Rate: {Percentage} <!-- % of labor force that is unemployed -->
- Labor Force Participation Rate: {Percentage} <!-- % people ages 15 or older who are employed or seeking work -->
- Poverty Rate: {Percentage} <!-- % of population living below the poverty line -->
- Inflation Rate: {Percentage} <!-- annualized -->
- Gini Coefficient: {Number} out of 1.0
- Average Annual Income: {AmountUSD} per person
- Exchange Rate ({LocalCurrency}/USD): {ExchangeRate}
- Optimistic Perception of Economic Future: {Percentage} <!-- % of population that believes the economy will improve -->

## Top Economic Challenges <!-- e.g. unemployment, inflation, trade imbalances, etc. Severity and detailed description. At least 2. -->
- {Challenge}: {Description}
""".strip(),
        seed_assumptions=[
            "Assume an initial GDP of 2,700,000,000 USD (2.7 billion USD)",
            "Assume all real countries (e.g. USA, China, Russia, etc) for import and export partners",
        ],
    ),
    StateDimension(
        title="International Relations",
        template="""
## Diplomatic Relations
<!-- describe the diplomatic relations in detail, including:
- Major allies and their relationship
- Major rivals and their relationship
- Diplomatic missions abroad
- International agreements and treaties
- Foreign policy and national security -->

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
- Total Exports: {AmountUSD}
- Total Imports: {AmountUSD}

## Top International Relations Challenges <!-- e.g. territorial disputes, trade conflicts, etc. Severity and detailed description. At least 2. -->
- {Challenge}: {Description}
""".strip(),
        seed_assumptions=[
            "Assume all real good types (e.g. electronics, rare metals, grain, oil, etc.)",
            "Assume all real countries (e.g. USA, China, Russia, etc) for import and export partners",
        ],
    ),
    StateDimension(
        title="Defense",
        template="""
## Military System
<!-- describe the military system in detail, including:
- The structure and branches
- Nuclear capabilities
- Technological capabilities
- Sources of equipment (e.g. domestically produced, foreign-made, etc.) -->

## Military Personnel <!-- some of these may be zero -->
- Active Duty Personnel: {Number}
- Reserve Personnel: {Number}

## Military Assets
- Advanced Combat Aircraft (5th/4th gen): {Number} <!-- e.g. F-35, Su-57 level -->
- Basic Combat Aircraft (3rd/2nd gen): {Number} <!-- e.g. MiG-21 level -->
- Transport/Support Aircraft: {Number}
- Combat Helicopters: {Number}
- Support Helicopters: {Number}
- Unmanned Aerial Systems: {Number}
- Major Combat Ships: {Number} <!-- e.g. destroyers, cruisers -->
- Minor Combat Ships: {Number} <!-- e.g. corvettes, patrol boats -->
- Submarines: {Number}
- Support Vessels: {Number}
- Modern Main Battle Tanks: {Number} <!-- e.g. M1A2, T-90 level -->
- Legacy Tanks: {Number} <!-- e.g. T-55 level -->
- Armored Combat Vehicles: {Number}
- Artillery Systems: {Number}
- Ballistic Missile Systems: {Number}
- Air Defense Systems: {Number}
- Satellite Systems: {Number}
- Cyber/Electronic Warfare Units: {Number}
- Special Forces Units: {Number}

## Top Defense Challenges <!-- e.g. terrorism, cyber threats, organized crime, etc. Include risk level and detailed description. At least 2. -->
- {Challenge}: {Description}
""".strip(),
    ),
    StateDimension(
        title="Media",
        template="""
## Media Landscape
<!-- describe the media landscape in detail, including:
- Level of state control and censorship
- Media ownership concentration
- Role of international media
- Level of press freedom
- Digital media adoption
- Media literacy -->

## Media Source Composition <!-- e.g. % of content from each source -->
- Online News: {Percentage}
- Print News: {Percentage}
- TV News: {Percentage}
- Radio News: {Percentage}
- Social Media: {Percentage}
- {MediaSource}: {Percentage}
...

## News Coverage Composition <!-- e.g. coverage of issues, % of media time spent on issues -->
- {MediaIssue}: {Percentage}
...

## Media Metrics
- Press Freedom Index: {Number} out of 100
- Digital Divide Index (Infrastructure): {Number} out of 100
- Digital Divide Index (Socioeconomic): {Number} out of 100
- Social Media Usage: {Percentage} <!-- % of population that uses social media -->
- Average Daily Media Consumption: {Number} hours
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

## Cultural Practices
<!-- describe the cultural practices in detail, including:
- Cusine: traditional dishes, popular dishes, etc.
- Music: traditional music, popular music, etc.
- Art: traditional art, popular art, etc.
- Dance: traditional dance, popular dance, etc.
- Literature: traditional literature, popular literature, etc.
- Film: traditional film, popular film, etc.
- Sports: traditional sports, popular sports, etc. -->

## Cultural Metrics
- Soft Power Index: {Number} of 100
- International Cultural Centers: {Number}
- Protected Cultural Sites: {Number}
- Published Books per Year: {Number}
- Art Galleries: {Number}
- Museums: {Number}
- Theaters: {Number}
- Concert Venues: {Number}

## Top Cultural Challenges <!-- e.g. cultural preservation, cultural diversity, etc. Severity and detailed description. At least 2. -->
- {Challenge}: {Description}
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

## Environmental Metrics
- Total Land Area: {Number} sq km
- CO2 Emissions: {Number} metric tons per capita
- Particulate Matter (PM2.5): {Number} μg/m3
- Air Quality Index: {Number} out of 500
- Number of Endangered Species: {Number}

## Top Environmental Challenges <!-- e.g. pollution, deforestation, etc. Severity and detailed description. At least 2. -->
- {Challenge}: {Description}
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
...

## Technologies
<!-- describe the technologies in detail, including:
- Artificial Intelligence, Quantum Computing, Robotics, Space Program, Biotechnology, etc. 
- How well or poorly the state is doing in each technology -->

## Infrastructure Metrics
- Total Electricity Generation: {Megawatts}
- Mobile Phone Subscriptions: {Percentage}
- Highspeed Internet Access: {Percentage}
- Access to Improved Water Sources: {Percentage}
- Access to Improved Sanitation: {Percentage}
- Access to Electricity: {Percentage}
- Roads: {Number} km
- Railways: {Number} km
- Airports: {Number}
- Ports and Harbors: {Number}

## Infrastructure Challenges
- {Challenge}: {Description}
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
- Country Official Name: {StateName} <!-- The full name of the country, no special characters or colons -->
- Capital City: {CapitalCity} <!-- The full name of the capital city -->

## Political Participation
<!-- describe the political participation in detail, including:
- Age-related Participation
- Gender-related Participation
- Ethnic-related Participation
- Religious-related Participation -->

## Policies <!-- all policy types should have at least 4 policies, many policies should be unique to this country and some may align with non-western values -->
### Civil Rights and Democracy Policies <!-- e.g. voting rights, freedom of speech, assembly, religion -->
- {PolicyType}: {Description}

### Economic and Monetary Policies <!-- e.g. interest rates, inflation targets, financial regulation -->
- {PolicyType}: {Description}

### Fiscal and Tax Policies <!-- e.g. government spending, taxation, debt management -->
- {PolicyType}: {Description}

### Healthcare and Public Health Policies <!-- e.g. medical systems, insurance, drug policy, health research -->
- {PolicyType}: {Description}

### Education and Research Policies <!-- e.g. schools, universities, scientific funding, innovation -->
- {PolicyType}: {Description}

### Social Welfare Policies <!-- e.g. poverty programs, disability support, retirement benefits -->
- {PolicyType}: {Description}

### Justice System Policies <!-- e.g. courts, legal system, criminal law, rehabilitation -->
- {PolicyType}: {Description}

### Law Enforcement Policies <!-- e.g. policing, investigation, public safety, emergency services -->
- {PolicyType}: {Description}

### Defense and Security Policies <!-- e.g. military, intelligence, cybersecurity, terrorism -->
- {PolicyType}: {Description}

### Foreign Relations Policies <!-- e.g. diplomacy, international organizations, foreign aid -->
- {PolicyType}: {Description}

### Immigration and Border Policies <!-- e.g. visas, citizenship, customs, border control -->
- {PolicyType}: {Description}

### Environmental and Climate Policies <!-- e.g. conservation, emissions, wildlife protection -->
- {PolicyType}: {Description}

### Infrastructure and Transportation Policies <!-- e.g. roads, utilities, public transit, urban planning -->
- {PolicyType}: {Description}

### Labor and Employment Policies <!-- e.g. workers rights, job training, workplace safety -->
- {PolicyType}: {Description}

### Technology and Digital Policies <!-- e.g. internet regulation, AI governance, data privacy -->
- {PolicyType}: {Description}

### Culture and Media Policies <!-- e.g. arts funding, broadcasting, sports, heritage preservation -->
- {PolicyType}: {Description}

## Government Metrics
- Corruption Perception Index (CPI): {Number} out of 100
- Direction of Country: {Percentage} believe country is on right track
- Overall Head of State/Government Approval Rating: {Percentage}
- Democracy Index: {Number} out of 10.0 <!-- The Economist Democracy Index -->

## Top Government Challenges <!-- e.g. corruption, political instability, etc. Severity and detailed description. At least 2. -->
- {Challenge}: {Description}
""".strip(),
    ),
    StateDimension(
        title="Public Opinion",
        template="""
## Recent Citizen Quotes <!-- At least 5 that that a random sample of population and their concerns. This should be a mix of people and change every year. Quotes should be rich and specific. Format exactly as shown. -->
- {Name} ({Number} years old, {Gender}, {Ethnicity}, {Religion}, {Occupation}, {AmountUSD} annual income) - "{Quote}"
...

## Recent Headlines <!-- At least 5 recent viral headlines. Avoid generic headlines, make them interesting and specific. As if written by like CNN or Fox News. -->
- "{Headline}"
...
""".strip(),
    ),
]
