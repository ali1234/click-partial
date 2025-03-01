Work-in-progress code.

Does your click CLI have a lot of subcommands that construct the same objects
over and over, using the same options?

click-partial is to click.commands what functools.partial is to functions.

click-partial allows you to build re-usable decorators that automatically
construct objects (or do other things) using a collection of options, while
hiding the details (and all the options) from your subcommands.

Your click CLI without click-partial: [example_before.py](example_before.py)

Your click CLI with click-partial: [example_after.py](example_after.py)