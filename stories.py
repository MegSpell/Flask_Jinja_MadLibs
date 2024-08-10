"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a code, a title, a list of prompts,
    and the text of the template.

        >>> s = Story(
        ...     "simple",
        ...     "A Simple Tale",
        ...     ["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, code, title, words, text):
        """Create story with words and template text."""

        self.code = code
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1 = Story(
    "history",
    "A History Tale",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    "omg",
    "An Excited Adventure",
    ["noun", "verb"],
    """OMG!! OMG!! I love to {verb} a {noun}!"""
)

story3 = Story(
    "horse",
    "The Hungry Horse",
    ["adjective", "verb_ending_ing", "place", "adjective_2", "food", "adjective_3"],
    """The {adjective} horse {verb_ending_ing} into {place} and demanded a {adjective_2} {food}, surprising everyone with its {adjective_3} appetite!"""
)

story4 = Story(
    "puppy",
    "The Playful Puppy",
    ["adjective", "noun", "place", "verb_ending_ing", "adjective2"],
    """The {adjective} puppy found a {noun} in {place} and couldn't stop {verb_ending_ing} with it, making everyone laugh at its {adjective2} energy!"""
)

story5 = Story(
    "cooking",
    "The Unusual Recipe",
    ["Place", "Name", "food", "noun", "adjective", "verb_ending_in_ed"],
    """While cooking in {Place}, {Name} accidently mixed a {food} with a {noun} creating the most {adjective} dish anyone had ever {verb_ending_in_ed}!"""
)

# Make dict of {code:story, code:story, ...}
stories = {s.code: s for s in [story1, story2, story3, story4, story5]}