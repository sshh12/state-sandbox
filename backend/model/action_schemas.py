STATE_CONFIG_FORMAT_TEMPLATE = """
<!--
- Follow the template exactly. Filling in {values}, keeping text outside of brackets, and replacing ...s.
- You are expected to fill out ALL the fields in the template and keep ALL default attributes.
- Format {Number} like: 123, 123 million, 0.12. Do not use a percentage or relative values.
- Format {Percentage} like: 12%, 0.01%.
- Format {Description} with 1-3 concise sentences. Use technical terms and avoid filler words.
- Format {AmountUSD} monetary amounts in USD like $123, $123 million, $0.12.
- Format {Challenge}, {PolicyType}, etc. like "Topic Name" (no styling or quotes)
- Do not use *italic* or **bold**. 
- Do not add nested lists or headings not specified in the template.
- Do not include <!-- comments --> in the final output but use them as key guidance.
-->
""".strip()

RANDOM_EVENTS_TEMPLATE = """
<!--
These are random events the goverment will need to make decisions on.
- Events are mutually exclusive within their category.
- Events must start with a % probability.
- Events should be caused by nature, citizens, businesses, or other states.
- Events can be controversial, bad, or mixed. All should be expected to invoke an opinionated response from the government.
- Events can tip the scales of various dimensions of the state.
- Events should be consise and unambiguous (no "... changes", it should state what the change is).
- Events that last longer than a year should be stated as "starts" (or "ends").
- Event categories must include a first no-event category.
- Event probabilities should be realistic (chance over the course of a year) and influenced by the <state> and known historical events.
- Be specific with varients and severity of events (e.g. Cat N Hurricane, Cyberattack on N industrial facilities, etc.)
- Do not add nested lists or headings not specified in the template.
- Do not include <!-- comments --> in the final output but use them as key guidance.
- Do not use *italic* or **bold**. 
-->

# Environmental and Weather Events <!-- Examples: Natural disasters (hurricanes, floods), climate anomalies (record temperatures, droughts), environmental incidents (oil spills, forest fires), wildlife crises (invasive species, mass die-offs) -->
- x% No notable events
...

# Economic Events <!-- Examples: Market crashes, major company bankruptcies, industry-wide strikes, commodity price shocks, foreign investment withdrawals, currency manipulation by foreign powers, trade embargo impacts -->
- x% No notable events
...

# Defense and Military Events <!-- Examples: Cyber attacks on critical infrastructure, terrorist incidents, border incursions, military equipment failures, foreign spy networks discovered, military tech breaches, armed militia formations -->
- x% No notable events
...

# Health and Crime Events <!-- Examples: Disease outbreaks, drug-resistant infections, organized crime expansion, new synthetic drug epidemics, healthcare system breaches, mass poisoning incidents, bioterror threats -->
- x% No notable events
...

# Cultural and People Events <!-- Examples: Mass protests, religious conflicts, demographic shifts, controversial media influence, education system crises, cultural heritage destruction, social movement radicalization -->
- x% No notable events
...

# Infrastructure and Technology Events <!-- Examples: Critical infrastructure failures, AI system malfunctions, data center breaches, transportation system vulnerabilities, power grid instabilities, water system contamination -->
- x% No notable events
...

# International Relations Events <!-- Examples: Diplomatic expulsions, trade agreement violations, foreign asset seizures, international sanctions threats, refugee crises, foreign interference in domestic affairs -->
- x% No notable events
...
""".strip()

FUTURE_POLICY_TEMPLATE = """
<!-- 
Provide a list of at most 4 actions to respond to the events.
- Action examples: "Ban the use of social media", "Increase funding for anti-cybercrime programs", etc.
- Actions should be specific, realistic, and target the events.
- Actions should have non-obvious negative consequences (don't state this explicitly).
- Actions should not include the effects or risks of the action.
- Actions should be at most 2 sentences. Keep it technical, dense, and concise.
- Actions should reflect the type of <state> and cultural values.
- Events should have at most 1 action each.
- Events that are obviously positive should not have any actions.
- Do not add nested lists or headings not specified in the template.
- Do not include <!-- comments --> in the final output but use them as key guidance.
- Do not use *italic* or **bold**. 

IMPORTANT: Include flawed actions that will make the state worse.
-->
""".strip()

DIFF_EXECUTIVE_TEMPLATE = """
<!--
- This is a report to state leadership on the changes to the <state> over the last year.
- Include both what happened, what changed, and how it was mitigated (if at all) by the state.
- You should include what changes, why it changes, and notable metrics that will reflect the change.
- Focus on the most important events, some might not be that important for the leadership.
- Some sections may be empty if nothing relevant changed.
- Do not add nested lists or headings not specified in the template.
- Do not include <!-- comments --> in the final output but use them as key guidance.
- Do not include a greeting or a summary at the end.
-->

### Executive Summary

<!-- 
- 1 - 2 sentence dense technical overview of what *important* happened, for the leadership of the <state>.
-->

1. **Environment and Weather**:
  - <!-- *Title* -->: <!-- Description -->
  - ...
2. **Economy**:
  - <!-- *Title* -->: <!-- Description -->
  - ...
3. **Defense**:
  - <!-- *Title* -->: <!-- Description -->
  - ...
4. **Health and Crime**:
  - <!-- *Title* -->: <!-- Description -->
  - ...
5. **Culture and People**:
  - <!-- *Title* -->: <!-- Description -->
  - ...
6. **Infrastructure and Technology**:
  - <!-- *Title* -->: <!-- Description -->
  - ...
7. **International Relations**:
  - <!-- *Title* -->: <!-- Description -->
  - ...
""".strip()
