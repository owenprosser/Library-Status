# Library-Status
Shows the number of students currently in the University Library all from the comfort of your shell!

## To run as commmand in bash:
Make the file executable

```
$ chmod +x libraryStatus.py
```

Remove the need for the .py extension to be part of the command

```
$ mv libraryStatus.py libraryStatus
```

Make bin dir 

```
$ mkdir -p ~/bin
```
Copy the file to this dir

```
$ cp libraryStatus ~/bin
```
Add this dir to your PATH

```
export PATH=$PATH":$HOME/bin"
```

Add this line to .bash_profile to make it a permenant change.
