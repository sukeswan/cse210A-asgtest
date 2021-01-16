# Test scripts for CSE201A

To run this project: 

1. Clone the repo or download the source code. If cloning, please make sure to switch over to the branch called `version3`. That is the most up to date branch. That can be done by running the command `git checkout version3`

2. Switch into the homework 1 folder using the command `cd cse210A-asgtest-hw1-arith`

3. Run the test cases with the command `./test.sh`. This will run makefile which will download pyinstaller onto your computer, make an executable callled arith, and then run the test cases.

4. To manually run the test cases, use the command `make main`. 

5. To delete the `arith` executable, you can run the command `make clean`


The screenshots of the expected behavior can be found under `HW1 Output.pdf`

The git logs for this project are under the `git logs` folder. Becasue I worked on three branches in sequence, I included the git logs for all three branches. I worked first with master, then version2, then version3. 

NOTE: As I am just learning what ASTs are and how to use them, I followed the tutorial linked [here](https://ruslanspivak.com/lsbasi-part7/). It comes reccomended by Prof Flanagan and Sherry, the TA. I also worked with Donald Stewart on the Makefile and we talked about ASTs and programming languages. 




These test scripts are prepared based on [Sohum Banerjea's work](https://github.com/SohumB/cse210A-asgtest/tree/master).
