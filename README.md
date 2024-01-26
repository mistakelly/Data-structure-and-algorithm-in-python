# Data-structure-and-algorithm-in-python

## Data-structure

before we start fully with data structure and algorithm
we first of have to understand some concepts right ??

1. what is Data ?
2. what is Data-structure ?
3. why Data-Structure ?

if we are able to answer these three question I think and believe
good to go with Data-structure.

* so what is DATA ?
    as we all know in basic computer, data is what ? 
    an unprocessed raw facts right ?? the data can be
    any type such as images, documents, numbers, strings
    that can be processed by the computer.

* then now what is Data-Structure ?
    Data structure is a way of storing data in the 
    computer, so it can be used efficiently.
    its basically the art of arranging the data in
    a way that allows the computer to perform operations
    on the data efficiently.

## why do we need DATA-STRUCTURE ?

in the early days of programming, programmeers only have one 
wish or mechanism of anaylysing code, which is ?? 😂 guess you
must have known the answer 😂😂, tell me nahhhh 🙏🙏, you don't 
want to talk abi ?? ok oo let me answer which is *("is the code working?")
once their code is working that is like the deal-breaker for them.
it made sense that way, not until developers started noticing that 
two or different persons can actually solve or implement a task in different
ways and still get the same result, and now that their codes that were working
initially, they started to observing that, is like one's code runs faster than 
other right ??,they now start finding a way to calculate it how much time a program
takes to complete and space the program also takes in our computer during runtime, and 
that was when they came up with * TIME COMPLEXITY AND SPACE COMPLEXITY. these two help
us to know how much time and space our program takes during runtime, click link to see how
two different codes solves a problem in with two different approach, would want to anaylyse
the code that runs faster than another yourself[check time efficiency](main.py)
that way we can write efficient programs using the right DATA-STRUCTURE.


## we have various types of DATA-STRUCTURE:
1. Arrays
![array image](arrar.png)
2. linked->list
![linked->list](https://www.simplilearn.com/ice9/free_resources_article_thumb/Linked-List-Soni/singly-linked-list.png)
3. stack
![stack](data:image/png;base64,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)
