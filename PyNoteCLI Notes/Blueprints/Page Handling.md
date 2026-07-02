Create a *page data class* that holds
-  Path to page
-  Page text type (markdown / text)
-  Page type (normal / checklist)
-  Page ID

A Page manager class has methods that allow
-  Page creations
-  Page removals
-  Getting Pages (ID and NAME)
-  Getting all Pages

Whenever a page is created, it creates a blank file with `{page name}-{id}` so that duplicate names are allowed.