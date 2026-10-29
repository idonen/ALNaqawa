# AL-Naqawa prayer tools and reference

AL-Naqawa provides web tools for calculated prayer start times, calculation-method comparisons, Qibla bearings and Islamic-calendar planning. Its public beta MCP endpoint lets compatible AI clients request calculations and timetable files.

**Website:** [alnaqawa.com](https://alnaqawa.com/en) · **MCP setup:** [connection guide](https://alnaqawa.com/en/mcp) · **Endpoint:** `https://alnaqawa.com/mcp`

This repository contains reference documentation, reproducible example requests and a small Python client. It is not the website's backend, a mobile app, a physical clock or an independently validated astronomical dataset. It does not imply affiliation with another prayer app or religious authority.

## Start here

| Task | Reference |
|---|---|
| Connect a compatible AI client | [MCP quickstart](docs/mcp-quickstart.md) |
| Understand the available operations | [Tool reference](docs/tool-reference.md) |
| Investigate different prayer-time results | [Comparison checklist](docs/prayer-time-differences.md) |
| Export a dated timetable | [Timetable workflow](docs/timetable-export.md) |
| Understand terms and limits | [FAQ](docs/faq.md) · [Glossary](docs/glossary.md) |
| Reproduce an example | [Example requests](examples/README.md) |
| Check a statement's source | [Sources and maintenance](docs/sources.md) |

## Connect with MCP

For clients that accept this configuration shape:

```json
{
  "mcpServers": {
    "al-naqawa": {
      "url": "https://alnaqawa.com/mcp"
    }
  }
}
```

Other clients use a remote-connector URL field. Select Streamable HTTP if asked. Client support and any client subscription requirements vary. The AL-Naqawa public beta currently requires no AL-Naqawa API key; this is not an unlimited-use or availability promise.

Ask the client to list tools, search for your city and confirm its country and IANA time zone. Choose an explicit local date and calculation settings before requesting times. Do not guess a city ID or supply prayer times from model memory when the service fails.

## Try the Python example

The client uses Python's standard library. It makes read-only requests to the public beta service.

```text
python scripts/mcp_client.py list
python scripts/mcp_client.py call search_cities --input examples/search-london.json
```

Review the returned location before using it in a calculation. The checked examples are dated snapshots, not today's timetable. See [example instructions](examples/README.md) for saving files without overwriting an existing path.

## Interpretation that belongs with every result

- These are calculated prayer **starts**, not a mosque's Iqamah or Jumuah schedule.
- Keep the city, local date, time zone, method, Asr setting and warnings attached to results.
- Sunrise is distinct from Fajr and is not one of the five daily prayers.
- Some astronomical events can be unavailable at high latitudes; preserve missing values and warnings.
- Calculated Hijri dates help with planning; local moon-sighting announcements may differ.
- Qibla output is an initial bearing relative to true north, not a live phone-sensor compass.
- Generating an ICS file does not set an alarm, create an event in your account or control hardware.

## Status and corrections

Reference checked: **2026-10-30**. Tool schemas are included as a dated snapshot; query `tools/list` for the current contract. City coverage is published in stages. Missing cities must not be silently replaced with other locations.

Use a repository issue for a documentation correction, including the page, source and reproducible request where relevant. Do not post private locations, credentials or account information. This repository provides useful reference material; publication here does not guarantee discovery, search ranking or citation by an AI service.
