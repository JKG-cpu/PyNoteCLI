from rich.console import Console
from rich.markdown import Markdown

console = Console()

markdown_text = """
## Hello World
This is a **Markdown** string printed in the terminal.

* Bullet one
* Bullet two

```python
print("Syntax highlighting works too!")
```
"""

# Convert text to a Markdown object and print
md = Markdown(markdown_text)
console.print(md)
