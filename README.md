# NeoScope

NeoScope is a Python-based tool designed to offer real-time monitoring of system operations specifically for Windows systems. The tool helps enhance efficiency and performance by providing continuous updates on CPU, RAM, and Disk usage.

## Features

- Real-time monitoring of CPU, RAM, and Disk usage.
- Logs system statistics at user-defined intervals.
- Displays the last 10 entries of system stats in a clear and concise format.
- Simple interface that runs in the terminal.

## Requirements

- Python 3.x
- `psutil` library

You can install the required library using pip:

```bash
pip install psutil
```

## Usage

To start monitoring your system, simply run the `neoscope.py` script:

```bash
python neoscope.py
```

By default, the program logs statistics every 5 seconds. You can change this interval by specifying a different `log_interval` when creating the NeoScope instance.

## How It Works

NeoScope continuously checks the system's CPU, RAM, and Disk usage, and logs the data into a file named `neoscope_log.txt`. It also displays the most recent statistics right in your terminal for easy viewing.

## Stopping the Monitoring

To stop the monitoring process, simply press `Ctrl+C` in your terminal.

## License

This project is licensed under the MIT License.