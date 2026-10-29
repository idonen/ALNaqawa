# Dated example requests

The examples use a fixed date and a public city. They are reproducible requests, not today's prayer times. Search results checked on 2026-10-30 identified London, United Kingdom as city `58153`, time zone `Europe/London`; another result was City of London. Always confirm which place the user intends.

| Request | Tool | Purpose |
|---|---|---|
| [search-london.json](search-london.json) | `search_cities` | Inspect the location matches |
| [methods.json](methods.json) | `list_calculation_methods` | Discover the actual supported presets |
| [prayer-london.json](prayer-london.json) | `get_prayer_times` | Fixed-date one-day calculation |
| [compare-london.json](compare-london.json) | `compare_prayer_methods` | MWL versus ISNA with matching inputs |
| [timezone-new-york.json](timezone-new-york.json) | `convert_timezone` | Convert an unambiguous UTC instant |
| [timetable-london.json](timetable-london.json) | `generate_timetable` | Three-day CSV export |

## Run one example

```text
python scripts/mcp_client.py call get_prayer_times --input examples/prayer-london.json
```

The `*.response.json` files retain actual responses when the corresponding live request succeeded during preparation. They are dated snapshots, not an independent accuracy standard. If the live service changes, report the difference and update the evidence after checking it.

To save a generated CSV:

```text
python scripts/mcp_client.py call generate_timetable --input examples/timetable-london.json --save timetable.csv
```

The helper refuses to overwrite an existing file. Generated download URLs may be temporary and are not retained as permanent reference links. No example imports a calendar, creates an alarm or sends data to another person.
