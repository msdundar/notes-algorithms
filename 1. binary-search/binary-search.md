## Binary Search

- Binary search is a divide-and-conquer algorithm; its input is a **sorted** list of elements. If an element you're looking for is in that list, binary search returns the position **where it's located**. Otherwise, binary search returns **null**.

- We can only conduct binary search with ordered lists, such as alphabetically ordered phone list, ordered list of numbers etc.

- In general, for any list of n, binary search will take **log<sub>2</sub>n** steps to run in the worst case, whereas simple search will take **n** steps.

  ![logarithms](images/logarithms.png)

In this book, when I talk about running time in Big O notation (explained a little later), log always means log<sub>2</sub>.

## Running Time

| Running Time | Log(n) vs n |
| ------------ | ----------- |
| ![running-time](images/running-time.png) | ![log-n](images/log-n.png) |

The key idea is that when binary search makes an incorrect guess, the portion of the array that contains reasonable guesses is reduced by at least half. If the reasonable portion had 32 elements, then an incorrect guess cuts it down to have at most 16. Binary search halves the size of the reasonable portion upon every incorrect guess.

> According to 'Programming Pearls', only 10% of professional programmers are able to implement binary search in their code. They can explain it very well, but coding it is a challenge for them.
