STATE_CONFIG_FORMAT_TEMPLATE = """
<!--
- Follow the template exactly. Filling in {values}, keeping text outside of brackets, and replacing ...s.
- You are expected to fill out ALL the fields in the template and keep ALL default attributes.
- Format {Number} like: 123, ~123 million, 0.12, etc. Do not use a percentage or relative values.
- Format {Percentage} like: 12%, ~12%, 0.01%, etc. Include a percentage sign.
- Format {DetailedDescription} with 1-3 concise sentences. Use technical terms and avoid filler words.
- Format {TotalAmountInUSD} monetary amounts in USD.
- Certain policies, descriptions, and values the answer may be "N/A due to...". For metrics that should exist, but you don't know, use your best guess.
- Do not use *italic* or **bold**. 
- Do not add nested lists or headings not specified in the template.
- Do not include <!-- comments --> in the final output but use them as key guidance.
-->
""".strip()

RANDOM_TEMPLATE = """
<!--
- Event categories must be mutually exclusive and must include a first no-event category.
- Events can be good, bad, or mixed.
- Probabilities and events should be influenced and personalized by the <state>.
- Probabilities must be as real-world realistic as possible.
- Include varients and severity of events (e.g. Cat N Hurricane, etc.) and joint events (e.g. Hurricane + Earthquake).
- Events should be UNRELATED to the government actions of the <state> (these will be determined by another system).
- Events should be consise and unambiguous (no "... changes", it should state what the change is).
- Events that last longer than a year should be stated as "starts" (or "ends").
- Do not add nested lists or headings not specified in the template.
- Do not include <!-- comments --> in the final output but use them as key guidance.
- Do not use *italic* or **bold**. 
-->

# Environmental Events <!-- natural phenomena affecting environment/climate, at least 10 -->
- {%} No notable environmental events
...

# Defense & Military Events <!-- military/security incidents or developments, at least 10 -->
- {%} No notable defense/military events
...

# Economic Events <!-- major financial/market/business developments, at least 10 -->
- {%} No notable economic events
...

# Heath Events <!-- public health/medical developments, at least 10 -->
- {%} No notable health events
...

# Cultural & Social Events <!-- societal/cultural developments, at least 10 -->
- {%} No notable social events
...

# Infrastructure & Technology Events <!-- tech/scientific developments, at least 10 -->
- {%} No notable infrastructure/technology events
...

# International Events <!-- foreign relations/global developments by OTHER nations, at least 10 -->
- {%} No notable international events
...
""".strip()

DIFF_EXECUTIVE_TEMPLATE = """
<!--
- This is a report to state leadership on the changes to the <state> over the last year.
- Do not add nested lists or headings not specified in the template.
- Do not include <!-- comments --> in the final output but use them as key guidance.
- Do not include a greeting or a summary at the end.
- You should include what changes, why it changes, and notable metrics that will reflect the change.
- Focus on the most important events, some might not be that important for the leadership.
- Some sections may be empty if nothing relevant changed. You can re-arrange the sections to focus on the most important updates.
-->

### Executive Summary

<!-- 
- 1 - 2 sentence dense technical overview of what *important* happened, for the leadership of the <state>.
-->

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
""".strip()
