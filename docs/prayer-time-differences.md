# Why two prayer-time results can differ

Two results are comparable only when their location, date and settings are known. A difference does not, by itself, establish that one service is faulty or that one calculation convention is universally preferable.

This checklist helps reproduce a difference. It is a technical workflow, not a religious ruling or a verdict about a particular app.

## Align the input before comparing the output

| Input | What to record |
|---|---|
| Location | City identifier, country, coordinates and any region label |
| Date | The civil date in the selected city's time zone |
| Time zone | IANA zone and relevant UTC offset for that date |
| Method | The actual preset or calculation settings used |
| Asr | The selected rule; API labels differ between providers |
| High latitude | The selected adjustment rule and unavailable-event warnings |
| Minute adjustments | Each explicit offset rather than an unexplained corrected time |
| Meaning | Calculated start, mosque start timetable, Iqamah or a separate reminder |

AL-Naqawa exposes a comparison tool that keeps the city and date fixed while comparing two method keys. Read the current schema for the accepted keys. Another provider may use numeric identifiers for its own methods; an identifier from one API is not portable to another.

## A reproducible comparison

First run `search_cities` and inspect the selected city. Then confirm that `mwl` and `isna` remain supported through discovery. Send `compare_prayer_methods` an explicit city ID, date, `method_a`, `method_b` and the same Asr and high-latitude choices. Keep adjustments identical.

Report which outputs differ and the settings supplied. Do not describe the difference as proof that a method is religiously correct. A user may need to follow a local mosque's published guidance even when a generic city calculation is internally consistent.

## Interpret missing values and dates carefully

At some places and seasons, an astronomical event may not be available under the selected convention. Keep the service's warning and missing value instead of filling a plausible-looking time. A different high-latitude setting changes the question being asked and should be disclosed.

“Today” must be resolved in the selected city's time zone. Near midnight, a user's device and the selected city can be on different dates. During daylight-saving changes, keep the date and offset with any timestamp used for conversion.

## Compare like meanings

Calculated prayer starts and congregation schedules are different data. Do not infer a mosque's Iqamah or Friday congregation time from a generic start-time result. Sunrise should also remain a separate label rather than being relabelled Fajr.

## References

- [AL-Naqawa calculation methods](https://alnaqawa.com/en/methods)
- [AL-Naqawa tool input snapshot](../reference/tools-2026-10-30.json)
- [AlAdhan API documentation](https://aladhan.com/prayer-times-api), a separate provider's parameter conventions
- [AlAdhan calculation-method explanation](https://aladhan.com/calculation-methods)

Checked 2026-10-30. This page contains no fixed “today” times and makes no comparative accuracy claim.
