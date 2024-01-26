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
