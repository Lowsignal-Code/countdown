# Countdown Timer

A minimal command-line countdown timer written in Python. It counts down from a given number of seconds and updates the time in place on a single terminal line.

## Table of Contents

- [Features](#features)
- [Preview](#preview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Limitations](#limitations)
- [License](#license)

## Features

- Counts down from any number of seconds passed as a command-line argument
- Displays remaining time in `MM:SS` format
- Updates the countdown in place on a single line instead of printing a new line every second
- Defaults to 60 seconds if no argument is given
- Can be stopped at any time with `Ctrl+C` without producing an error
- Built entirely on Python's standard library, no external dependencies required

## Preview

```
$ python countdown.py 10
00:07
```

The line above updates in place every second until it reaches `00:00`, at which point it is replaced with `Time's up!`.

## Requirements

- Python 3.7 or newer
- No third-party packages are required; the script relies only on modules included in the Python standard library (`sys`, `time`).

## Installation

Clone the repository:

```bash
git clone https://github.com/<Lowsignal-Code>/<countdown>.git
cd <countdown>
```

No further installation steps are needed since the script has no external dependencies.

## Usage

Run the script from the terminal, passing the number of seconds to count down from:

```bash
python Main.py <seconds>
```

For example, to count down from 5 minutes:

```bash
python Main.py 300
```

If no argument is provided, the timer defaults to 60 seconds:

```bash
python Main.py
```

To stop the timer before it finishes, press `Ctrl+C`.

## How It Works

1. **Reading input** — The number of seconds is read from `sys.argv`. If no argument is provided, it defaults to 60.
2. **Countdown loop** — On each iteration, the remaining seconds are converted into minutes and seconds using `divmod()`, then printed in `MM:SS` format.
3. **In-place updates** — The carriage return character (`\r`) moves the cursor back to the start of the line before each print, so the new value overwrites the old one instead of appearing on a new line. `flush=True` ensures the output is shown immediately rather than being buffered.
4. **Waiting** — `time.sleep(1)` pauses execution for one second between updates.
5. **Finishing** — Once the countdown reaches zero, the loop ends and `Time's up!` is printed in place of the timer.
6. **Graceful interruption** — The entire loop is wrapped in a `try/except KeyboardInterrupt` block, so pressing `Ctrl+C` prints a short `Stopped.` message instead of showing a traceback.

## Limitations

- Runs entirely in the terminal; there is no sound or visual notification when the countdown finishes.
- Timing relies on repeated one-second `time.sleep()` calls, so very long countdowns may drift slightly due to the overhead of each loop iteration.
- Only accepts whole seconds as input; there is no support for formats like `5m` or `1h30m`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
