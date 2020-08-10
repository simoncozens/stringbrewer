<a name="stringbrewer"></a>
# stringbrewer: Generate random strings matching a pattern.

Patterns are specified in the StringBrewer pattern language, and are made
up of two parts: a *recipe* and a set of *ingredients*. A recipe is
essentially a modified form of regular expression; whitespace is not
significant, and each ingredient name is replaced by its definition. An
*ingredient* is a space-separated list of items; each item is either a
character (specified either as a literal character or as a Unicode
codepoint in hexadecimal), a range of characters separated by hyphens,
or a union of items separated by commas. Ingredients may also contain
references to other ingredients.

This is best understood by example. The pattern below generates
Telugu morphemes::

    # Generate random Telugu-like morphemes
    (Base HalantGroup{0,2} TopPositionedVowel?){1,3}

    Base = క-న,ప-హ
    Halant = 0C4D
    HalantGroup = Halant Base
    TopPositionedVowel = 0C46-0C48,0C4A-0C4C

The first line is a comment; the second is the recipe, and the blank line
denotes the beginning of the ingredients list. Let's look at the ingredients.
A ``Base`` is any character either in the range ``0x0C15-0C28`` or ``0C2A-0C39``.
(We specified these as literals, just because we could). A ``Halant`` is the
character ``0x0C4D``. A ``HalantGroup`` is a halant followed by a base.

Now you understand the ingredients, the recipe is simple to understand if you
think in terms of regular expression syntax: a base followed by zero, one or
two halant groups, plus an optional top-positioned vowel, all repeated between
one and three times.

<a name="stringbrewer.StringBrewer.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(from_string=None, from_file=None, recipe=None, ingredients=None)
```

Initializes a StringBrewer object

You must provide *either* a file name, a string, or a recipe
string and ingredients dictionary.

**Arguments**:

- `from_file` - A file name of a file containing a pattern.
- `from_string` - A pattern in a string.
- `recipe` - The recipe part of a pattern.
- `ingredients` - A dictionary of regular expressions.

<a name="stringbrewer.StringBrewer.generate_all"></a>
#### generate\_all

```python
 | generate_all()
```

Generates a list of all combinations.

If there are more than 100,000 combinations, an exception
is raised to avoid running out of memory.

<a name="stringbrewer.StringBrewer.generate"></a>
#### generate

```python
 | generate(min_length=0, max_length=None)
```

Generates a single random combination.

**Arguments**:

- `min_length` - Minimum length (zero if not specified)
- `max_length` - Maximum length (no maximum if not specified)

