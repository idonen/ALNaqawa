# AL-Naqawa MCP tool reference

Discovery snapshot: 2026-10-30. This is a dated input reference. Use live `tools/list` for the current contract. The examples and client do not constitute the server implementation.

| Tool | Purpose | Required input |
|---|---|---|
| `search_cities` | Search available cities by name and country. Results include stable IDs and IANA time zones. | `query` |
| `list_calculation_methods` | List the actual presets supported by the shared prayer engine, with their settings. |  |
| `get_prayer_times` | Get up to seven days of calculated prayer start times, sunrise, settings and warnings. | `city_id`, `date` |
| `compare_prayer_methods` | Compare all five prayers with the same city, date, Asr rule and adjustments. | `city_id`, `date`, `method_a`, `method_b` |
| `get_qibla` | Get the initial bearing towards the Kaaba, measured clockwise from true north. | `city_id` |
| `convert_calendar` | Convert Hijri and Gregorian dates in either direction with an explicit calendar method. | `direction` |
| `get_calendar_month` | Get a Hijri or Gregorian month with corresponding dates in the other calendar. | `calendar`, `year`, `month` |
| `list_islamic_days` | List calculated planning dates, with local moon-sighting and observance qualifications. | `gregorian_year` |
| `convert_timezone` | Convert an unambiguous timestamp to another IANA time zone, including daylight saving. | `instant`, `time_zone` |
| `generate_timetable` | Create a CSV or ICS file for up to 32 days, with the city and calculation settings attached. | `city_id`, `date` |

## Input details

Provider-specific method keys and identifiers are not interchangeable with another API. A supported-preset count is not a claim of greater accuracy or religious authority.

### search_cities

- `query`: string.
- `country`: string.
- `limit`: integer; minimum 1; maximum 20; default 8.

### list_calculation_methods


### get_prayer_times

- `city_id`: integer; maximum 2147483647; greater than 0.
- `date`: string.
- `method`: string; 55 supported keys in the snapshot; see the JSON reference.
- `asr_rule`: string; one of `shafi`, `hanafi`; default "shafi".
- `high_latitude`: string; one of `automatic`, `none`, `middleOfTheNight`, `seventhOfTheNight`, `twilightAngle`; default "automatic".
- `ramadan`: boolean; default false.
- `adjustments`: object.
- `days`: integer; minimum 1; maximum 7; default 1.

### compare_prayer_methods

- `city_id`: integer; maximum 2147483647; greater than 0.
- `date`: string.
- `method`: string; 55 supported keys in the snapshot; see the JSON reference.
- `asr_rule`: string; one of `shafi`, `hanafi`; default "shafi".
- `high_latitude`: string; one of `automatic`, `none`, `middleOfTheNight`, `seventhOfTheNight`, `twilightAngle`; default "automatic".
- `ramadan`: boolean; default false.
- `adjustments`: object.
- `method_a`: string.
- `method_b`: string.

### get_qibla

- `city_id`: integer; maximum 2147483647; greater than 0.

### convert_calendar

- `direction`: string; one of `gregorian-to-hijri`, `hijri-to-gregorian`.
- `date`: string.
- `hijri`: object.
- `method`: string; one of `islamic-umalqura`, `islamic-civil`; default "islamic-umalqura".
- `adjustment`: integer; minimum -2; maximum 2; default 0.

### get_calendar_month

- `calendar`: string; one of `hijri`, `gregorian`.
- `year`: integer; minimum 1300; maximum 2100.
- `month`: integer; minimum 1; maximum 12.
- `method`: string; one of `islamic-umalqura`, `islamic-civil`; default "islamic-umalqura".
- `adjustment`: integer; minimum -2; maximum 2; default 0.

### list_islamic_days

- `gregorian_year`: integer; minimum 1900; maximum 2100.
- `method`: string; one of `islamic-umalqura`, `islamic-civil`; default "islamic-umalqura".
- `adjustment`: integer; minimum -2; maximum 2; default 0.

### convert_timezone

- `instant`: string.
- `time_zone`: string.

### generate_timetable

- `city_id`: integer; maximum 2147483647; greater than 0.
- `date`: string.
- `method`: string; 55 supported keys in the snapshot; see the JSON reference.
- `asr_rule`: string; one of `shafi`, `hanafi`; default "shafi".
- `high_latitude`: string; one of `automatic`, `none`, `middleOfTheNight`, `seventhOfTheNight`, `twilightAngle`; default "automatic".
- `ramadan`: boolean; default false.
- `adjustments`: object.
- `days`: integer; minimum 1; maximum 32; default 31.
- `format`: string; one of `csv`, `ics`; default "csv".

## Interpretation

Always retain location, local date, time zone, selected settings and warnings. A calculated start is not a mosque congregation schedule. A generated file does not create an account event or alarm.

Source: actual discovery response in [tools-2026-10-30.json](../reference/tools-2026-10-30.json). See [sources and maintenance](sources.md).
