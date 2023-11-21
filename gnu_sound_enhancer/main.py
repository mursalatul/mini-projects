import subprocess

def volume(vol: str) -> bool:
    # creating command
    volume_command = "pactl set-sink-volume @DEFAULT_SINK@ " + vol + "%"
    volume_command = volume_command.split()

    # running the command
    status = subprocess.run(volume_command).returncode
    return not status # returncode = 0 when successfully volume changed, else 1

def main():
    for i in range(5):
        vol = input("Volume Change: ")
        print(volume(vol))

if __name__ == "__main__":
    main()
