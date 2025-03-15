# Startup Script

A ssi ple script to start multiple bots in separate tmux sessions on a linux server


## Requirements

- Every bots its won directory with an executable file
- The bot prints a message containingthe word `online` If it start successfully
- ALl bot directories are placed in a `main` directory or in a subdirectory of the main directory


### Possible

- `/main/bot`
- `/main/subdir1/bot`

### No Possible

- `/main/subdir1/subdie2/bot`
- `/main/bot1/bot2`

## How to use the script

1. Modify the `config.py` file
2. Run `startup.py` anywhere on the server
