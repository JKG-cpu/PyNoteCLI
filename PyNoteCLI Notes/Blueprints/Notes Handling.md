Whenever a note is created, it should default to a page called All Notes.

Gonna use json to handle the notes. I'll include these values in the json just to make representation easier
-  Note count
-  Page name
-  Page Tag
-  Page Type
-  Deleted IDs
-  Notes (`dict[int, dict]`)

```json
{
	"note_count": 2,
	"page_name": "My Page",
	"page_tag": "" || "some_tag",
	"page_type": "normal" || "checklist",
	"deleted_ids": [],
	"notes": {
		// Note ID : Note dataclass
		1: NoteDataclass.to_dict() -> dict
	}
}
```

For used ids, just use `if id in dict`. `notes` should be sorted. For getting the next id, check `deleted_ids` and then get the last id in `notes` and add 1 to it.

This should all be managed by a note manager, that is used like this
```python
n = NoteManager()

n.add_note(
	name = "Note Name",
	description = "Some description"
)

n.remove_note(id = 1)
n.remove_note(name = "Note Name")
```

The note manager should handle note creation, deletion, displaying, and editing.

The note data class should be something like this
```python
from dataclasses import dataclass

@dataclass
class Note:
	name: str
	description: str
	id: int

@dataclass
class Checklist(Note):
	checked: bool = False
```
