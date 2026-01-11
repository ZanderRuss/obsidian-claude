---
tags:
  - type/moc
type: moc
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.file.title %>

## Overview

<% tp.file.cursor() %>

## Key Concepts

-

## Related Notes

```dataview
LIST
FROM ""
WHERE contains(file.outlinks, this.file.link) OR contains(file.inlinks, this.file.link)
SORT file.mtime DESC
LIMIT 20
```

## Resources

-

## Questions to Explore

-
