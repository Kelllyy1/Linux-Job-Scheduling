# Scheduling a Shell Script Execution Using `at`

> **NOTE:** The lines not preceded by `//` are the commands to type into the terminal; `//` represents commentary.

---

## Create the File

Use `vim` or `nano` in the terminal (or your favorite local text editor):

```bash
// vim
vim myscript.sh
```

```
// In vim:
//   Click the "i" key on the keyboard to enter "Insert Mode" and enter the contents of the "myscript.sh" file
//   Once done, click "Esc" then type ":wq" to write to the file and then exit.
```

```bash
// nano
nano myscript.sh
```

```
// In nano:
//   Enter the contents of the "myscript.sh" file.
//   Once done, click "Ctrl + O" on keyboard to save file, click "Y"
//   Click "Ctrl + X" on keyboard to exit file
```

---

## Make the File Executable

```bash
// Make the file executable
chmod +x myscript.sh
```

---

## Schedule the Execution

```bash
// Schedule the execution
at 12:04 -f ./myscript.sh
```

---

## Notes

```
// "at" schedules the job
// 12:04 is an arbitrarily chosen time, replace with your desired time of execution
// -f selection means to take input from a file instead of the terminal directly
// ./myscript.sh is the command to execute [it means to run the "myscript.sh" file]
```

If the `at` command is not installed:

```bash
sudo apt install at
```

```
// Then follow instructions in terminal to complete installation
```

---

## Extra Useful Commands

```bash
// View all jobs currently in the queue and their assigned number
atq

// Cancel the job with an assigned number of 2 before it is executed; 2 was arbitrarily chosen
atrm 2
```
