# Connect AL-Naqawa to a compatible MCP client

AL-Naqawa's public beta remote endpoint is `https://alnaqawa.com/mcp`. It uses Streamable HTTP. The current connection details are maintained on the [website's MCP page](https://alnaqawa.com/en/mcp).

## A reliable first conversation

Start by asking the client to discover available tools. Then use a request such as:

> Find London in the United Kingdom. Show the matching city's country and IANA time zone before calculating anything. Use 1 November 2026, Muslim World League and Standard Asr for the calculation. Keep the settings and warnings with the result.

This is an example prompt, not an expected result. A client should call `search_cities`, inspect the returned location and use `get_prayer_times` with the confirmed identifier. If more than one result fits, resolve the ambiguity before calculating.

## Discovery before hardcoded assumptions

The [tool reference](tool-reference.md) describes the current capabilities. A [dated schema snapshot](../reference/tools-2026-10-30.json) records the discovered input contract. Tools and limits can change. Query the live server for current schemas rather than assuming every named preset or parameter remains available forever.

If your client accepts an `mcpServers` JSON object, use the configuration in the [README](../README.md). If it instead offers a remote-server field, enter the endpoint there. These instructions do not establish support in every AI client. Follow the chosen client's own documentation for connection permissions.

## Using the included Python helper

```text
python scripts/mcp_client.py list
python scripts/mcp_client.py call search_cities --input examples/search-london.json
```

Run these commands from the repository root with Python installed. The helper is a small example for this endpoint, not a complete general-purpose MCP SDK. It negotiates a protocol version and reads JSON or event-stream responses. It has a bounded response size and a network timeout; a failure is not permission to invent replacement output.

## What this connection does

It returns calculations, supporting metadata and generated timetable data. It does not authenticate to your calendar, send a message to a mosque, create a phone reminder or operate a clock. Importing a timetable into another application is a separate action that needs your review.

## If a request fails

Record the tool name, non-sensitive arguments and error. Recheck the live schema and try a smaller valid request if appropriate. Report unavailable data explicitly. A missing city, invalid date or service error must remain visible to the user.

Source: [AL-Naqawa MCP capability and setup page](https://alnaqawa.com/en/mcp), checked 2026-10-30; input fields additionally checked against live tool discovery on that date.
