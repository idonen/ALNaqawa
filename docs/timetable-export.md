# Export a prayer timetable with its calculation context

An exported timetable is more useful when its location, dates and calculation settings remain attached. A file without that context can be mistaken for another city's schedule or a mosque's congregation timetable.

## Select and confirm

Use `search_cities` to select a currently available city and confirm its country and IANA time zone. Choose a local start date, a supported calculation method and the Asr rule. State any high-latitude setting and minute adjustments explicitly.

The `generate_timetable` tool supports CSV or ICS with a bounded range of 1–32 days in the schema checked on 2026-10-30. Use an explicit `days` value rather than relying on a default. Split longer ranges into bounded requests and check date boundaries before joining files.

## CSV or ICS?

| Format | Appropriate use | Review before use |
|---|---|---|
| CSV | Inspection in a spreadsheet or a printing workflow | City, dates, column labels, settings and missing events |
| ICS | Import into a compatible calendar | Calendar time-zone display, date range and duplicate imports |

The service describes ICS output as calculated start markers, using UTC instants and omitting unavailable events. It does not attach a claimed prayer duration or a built-in alarm. A receiving application may apply its own defaults, so inspect the imported entries before relying on their display or reminders.

## Save with the example client

The [example folder](../examples/README.md) contains dated request files. Confirm the example city before use, then run:

```text
python scripts/mcp_client.py call generate_timetable --input examples/timetable-london.json --save timetable.csv
```

The helper refuses to overwrite an existing file. Choose a new path if the output already exists. Saving a file locally and importing it into a calendar are separate steps.

## Acceptance checks

Read the first and last dates, confirm the city and selected method, and inspect the warnings. If the range crosses a clock change, compare the exported instants and their local display in the destination calendar. Avoid importing overlapping ranges repeatedly without first understanding how that calendar handles duplicates.

A timetable export is calculated information. It is not a mosque's Iqamah schedule, a local moon-sighting announcement or a guarantee that a notification will sound.

Sources: [AL-Naqawa MCP page](https://alnaqawa.com/en/mcp), [published prayer skill](https://alnaqawa.com/skills/al-naqawa-prayer/SKILL.md) and [dated tool schema](../reference/tools-2026-10-30.json). Checked 2026-10-30.
