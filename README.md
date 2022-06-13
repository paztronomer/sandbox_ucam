# sandbox_ucam
## From 2020, University of Cambridge. 

Collection of intermediate tools (to be included in other codes), simple useful scripts. Also, below you'll find some `bash`/`zsh` useful tips.

### Bash tools
Besides [paztronomer website: bash section](https://sites.google.com/view/paztronomer/blog/advanced/bash-examples?authuser=0), 
there are some tricks to help in some tasks

- List (or execute other command) over a huge amount of files 
  (`iname` is case-insensitive, whilst `name` isn't)
  ```bash 
  find . -iname "*.fits" | xargs ls -lrt | wc -l
  find . -iname "*.fits" | exec ls -lrt 
  ```
- Getting a substring from a list of files (remember to pipe them correctly)
  ```bash
  awk '{print substr($0,length($0)-10)}’
  awk '{print("mv "$1 " " substr($1,1,11)) substr($0,length($0)-9)}'
  ```
