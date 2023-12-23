# fi-lib

`fi-lib` is a Python library for Finnish language processing. It provides basic functions to conjugate verbs and decline nouns.

## Usage

To use `fi-lib`, import the desired functions from `fi_lib.py`. You can then call these functions with the stem of the word you want to conjugate or decline.

```python
from fi_lib import conjugate_verb, decline_noun

verb = "juosta"
noun = "kissa"

conjugated_verb = conjugate(verb) # Returns a dictionary of conjugated forms
declined_noun = decline(noun) # Returns a dictionary of declined forms
```

Alternatively, you can decline into just one form.

```python
from fi_lib import ablative

ablative_form = ablative(noun) # Returns "kissasta"
```

Other useful functions include syllables, vowel harmony, and consonant gradation.

```python
from fi_lib import syllables, vowel_harmony, strong_to_weak, weak_to_strong

syllables("kissa") # Returns 2
vowel_harmony("kissa") # Returns "back"
strong_to_weak("tikku") # Returns "tiku"
weak_to_strong("kato") # Returns "katto"
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
