# playground
This is a playground for making small experiments with different tools like e.g. git, cmake, bazel, ...


## cmake
This folder contains some small experiments with cmake


## kotlin
Playing around with kotlin

## spring 
Playing around with kotlin and spring

# Projects to work on in future

## valgrind
Valgrind is an instrumentation framework for building dynamic analysis tools. There are tools that can detect memory management and threading bugs, as well as tools for profiling your program in detail.
In depth information can be found in the official [manual](https://valgrind.org/docs/manual/manual.html)

You can install valgrind on ubuntu with
```
sudo apt-get install valgrind 
```

### Memcheck
The most famous tool is called Memcheck.
You can use it to detect memory leaks and memory errors. These types of error
are very tricky. 
Please notice that your program will run much slower (e.g 20 to 30 times) and take a lot more memory.

You can run it by the following command.

```
valgrind --leak-check=yes <binary> <optional argument1 argument2 argumentN>
```

### Callgrind
The goal of callgrind is to record the call history between functions in a call graph. The results are written into a file at the end.

If you want to use a GUI you can install kcachegrind, which is a visualisation tool for valgrind profiling output
```
sudo apt install kcachegrind
```

Other things you can do but I won't go into detail
### Cachegrind
Cachegrind simulates the interaction of your program with the cache hierarchy. 
```
valgrind --tool=cachegrind bazel-out/k8-fastbuild/bin/memcheck
```

### Hellgrind
### DRD
### Massif
### DHAT
### Nullgrind
### BVB


Other tools
## cppchecker
## clang-tidy
## clang static analyzer
## jenkins