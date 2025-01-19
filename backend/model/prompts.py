STATE_CONFIG_FORMAT_TEMPLATE = """
<!--
- Follow the template exactly. Filling in {values}, keeping text outside of brackets, and replacing ...s.
- You are expected to fill out ALL the fields in the template and keep ALL default attributes.
- Format {Number} like: 123, 123 million, 0.12. Do not use a percentage or relative values.
- Format {Percentage} like: 12%, 0.01%.
- Format {Description} with 1-3 concise sentences. Use technical terms and avoid filler words.
- Format {AmountUSD} monetary amounts in USD like $123, $123 million, $0.12.
- Do not use *italic* or **bold**. 
- Do not add nested lists or headings not specified in the template.
- Do not include <!-- comments --> in the final output but use them as key guidance.
-->
""".strip()

RANDOM_TEMPLATE = """
<!--
These are random events the goverment will need to make decisions on.
- Events are mutually exclusive within their category.
- Event categories must include a first no-event category.
- Events must start with a % probability.
- Events should be caused by nature, citizens, businesses, or other states.
- Events can be controversial, bad, or mixed. All should be expected to invoke an opinionated response from the government.
- Events can tip the scales of various dimensions of the state.
- Events should be consise and unambiguous (no "... changes", it should state what the change is).
- Events that last longer than a year should be stated as "starts" (or "ends").
- Event probabilities should be realistic and influenced by the <state>.
- Include varients and severity of events (e.g. Cat N Hurricane, etc.) and joint events (e.g. Hurricane + Earthquake).
- Do not add nested lists or headings not specified in the template.
- Do not include <!-- comments --> in the final output but use them as key guidance.
- Do not use *italic* or **bold**. 
-->

# Environmental and Weather Events <!-- natural phenomena affecting environment/climate, at least 10 -->
- x% No notable events
...

# Economic Events <!-- major financial/market developments, at least 10 -->
- x% No notable events
...

# Defense and Military Events <!-- military/security incidents or developments, at least 10 -->
- x% No notable events
...

# Health and Crime Events <!-- public health/medical developments, organized crime, at least 10 -->
- x% No notable events
...

# Cultural and Social Events <!-- societal/cultural developments, at least 10 -->
- x% No notable events
...

# Infrastructure and Technology Events <!-- tech/scientific developments, at least 10 -->
- x% No notable events
...

# International Relations Events <!-- diplomatic/international developments, at least 10 -->
- x% No notable events
...
""".strip()

FUTURE_POLICY_TEMPLATE = """
<!-- 
Provide a list of at most 4 actions to respond to the events.
- Action examples: "Ban the use of social media", "Increase funding for anti-cybercrime programs", etc.
- Actions should be specific, realistic, and target the events.
- Actions should have non-obvious negative consequences (don't state this explicitly).
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

1. **Environmental and Weather**:
  - <!-- *Title* -->: <!-- Description -->
  - ...
2. **Economic**:
  - <!-- *Title* -->: <!-- Description -->
  - ...
3. **Defense & Military**:
  - <!-- *Title* -->: <!-- Description -->
  - ...
4. **Health & Crime**:
  - <!-- *Title* -->: <!-- Description -->
  - ...
5. **Cultural and Social**:
  - <!-- *Title* -->: <!-- Description -->
  - ...
6. **Infrastructure & Technology**:
  - <!-- *Title* -->: <!-- Description -->
  - ...
5. **International Relations**:
  - <!-- *Title* -->: <!-- Description -->
  - ...
""".strip()
