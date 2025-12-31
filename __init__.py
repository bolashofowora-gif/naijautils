
→ Scroll down and click **“Commit changes”**

---

#### 2. **Create `naijautils/__init__.py`**
- Click **“Add file” → “Create new file”**
- In the filename box, type: `naijautils/__init__.py`  
  (This auto-creates the folder)
- Paste:

```python
from .validators import validate_bvn, validate_nin
from .formatters import format_naira
