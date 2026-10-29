# Prayer-time and integration glossary

These are short working definitions for reading the tools, not comprehensive religious definitions. Confirm religious practice with the guidance relevant to your community.

| Term | Meaning in this documentation |
|---|---|
| Prayer start | A calculated beginning time, distinct from a congregation schedule |
| Iqamah | The mosque's congregation-related timing; not inferred from the generic start calculation |
| Jumuah schedule | A mosque's Friday congregation arrangements; consult that mosque |
| Fajr | A daily prayer label kept distinct from sunrise |
| Sunrise | A separate solar event, not a sixth daily prayer |
| Asr rule | A calculation input; the current AL-Naqawa schema accepts `shafi` or `hanafi` |
| Calculation method | A preset or convention used by the engine; inspect its actual settings |
| High-latitude rule | An explicit setting for relevant seasonal conditions; retain returned warnings |
| Minute adjustment | An explicit offset applied to a named prayer result |
| IANA time zone | A location-aware zone identifier such as `Europe/London`; more informative than a permanent numeric offset |
| UTC instant | An unambiguous moment expressed with UTC or an explicit offset |
| Hijri conversion | A calculated mapping between date labels using a stated calendar method |
| Qibla bearing | An initial direction towards the Kaaba, measured relative to true north |
| MCP | Model Context Protocol; the interface used by compatible clients to discover and call these tools |
| Skill | A package of instructions and supporting resources for an agent; separate from the remote service |
| CSV | A tabular file format suitable for inspection in a spreadsheet |
| ICS | A calendar interchange format; creating the file does not import it or set a reminder |

Sources: [tool schemas](../reference/tools-2026-10-30.json), [AL-Naqawa MCP page](https://alnaqawa.com/en/mcp), [published skill](https://alnaqawa.com/skills/al-naqawa-prayer/SKILL.md). Checked 2026-10-30.
