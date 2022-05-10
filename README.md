# sandbox_ucam
## From 2020, University of Cambridge. 

Collection of intermediate tools (to be included in other codes), simple useful scripts. Also, below you'll find some `bash`/`zsh` useful tips.

### Git tools
As we work with many *identities*, levels of granularity, LFS, ... is useful to have quick access information

- Run the below to change the default user/email pair when making a commit, from a shared machine
  ```bash
  git config user.name "Francisco Paz-Ch"
  git config user.email _me_@cam.ac.uk
  ```
  If the directories are so organised, consider this [solution](https://www.freecodecamp.org/news/how-to-handle-multiple-git-configurations-in-one-machine/) as well.
- Clone just a particular branch
  ```bash
  git clone --branch <branchname> --single-branch <repo-url>
  ```


### Bash tools
In addition to [paztronomer website: bash section](https://sites.google.com/view/paztronomer/blog/advanced/bash-examples?authuser=0), 
below there are some useful tricks

- List (or execute other command) over a huge amount of files
  ```bash 
  find . -iname "*.fits" | xargs ls -lrt | wc -l
  find . -iname "*.fits" | exec ls -lrt 
  ```
- Getting a substring from a list of files (remember to pipe them correctly)
  ```bash
  awk '{print substr($0,length($0)-10)}’
  awk '{print("mv "$1 " " substr($1,1,11)) substr($0,length($0)-9)}'
  ```
