### To Do's
- [x] Edit database path to use `platformdirs`
- [x] Setup folders with `pynote setup`
- [x] Create and save file paths when creating pages
- [ ] Display page => need file paths + notes
- [ ] Edit pages => ***Need to create a CLI text editor (think of vim)***
- [x] Edit pages data class so file_path is a Path object

### 2026-07-02
Added command's for
-  `pynote config`
-  `pynote page`

- [x] Need to create a basic SQL database first in a temp folder, then *(when publishing)*, add the `platformdirs` module.

Gonna start working on the page management after. Need to 
- [x]  Allow page creations
- [x]  Allow different types of pages (normal / checklist, text / markdown)
- [x]  Allow page deletions
- [x]  List pages

***WHEN A PAGE IS CREATED, SET FILE PATH TO N/A => NEED TO REMOVE AND CREATE FILES LATER***

### 2026-07-03
Finished
- [x] Edit database path to use `platformdirs`
- [x] Setup folders with `pynote setup`
- [x] Create and save file paths when creating pages

Need to fix the data class to have file_path (for *pages*) be a Path object

### 2026-07-04
Changed the code so pages were deleted (just needed to do `Path(Page.file_path)`).

Also added a new command which clears the database: `pynote clear`.

### 2026-07-05
Gonna add commands for
- `pynote note add` 
- `pynote note add "..." --page "MyPage"` 
- `pynote note edit`
- `pynote note delete`
- `pynote note move`
- `pynote note list`
- `pynote node list --page "MyPage"`

### 2026-07-08
Gonna rework the pages + notes so that each page file is just json. That way it should be easier to add / manage notes.