Using pen & Paper write the internal mechanism for sum operation using  reduce function on this given list:[47,11,42,13]

Answer > Drive link ko pic https://drive.google.com/file/d/1kbtTqadlrG1AjgjPpdRBAAhRopeUlrZu/view?usp=drive_link
Here's the internal mechanism for the sum operation using the reduce function on the list [47, 11, 42, 13]

1 numbers = [47, 11, 42, 13]
2 reduce(lambda x, y: x + y, numbers)

3  Internal mechanism

 x   |  y  |  x + y
-----|-----|------
 47  | 11  |  58
 58  | 42  |  100
 100 | 13  |  113

Here's how it works:

1. Take the first two elements of the list: 47 and 11. Add them together to get 58.
2. Take the result 58 and the next element 42. Add them together to get 100.
3. Take the result 100 and the next element 13. Add them together to get 113.

The final result is 113, which is the sum of all elements in the list.

Note: The lambda function lambda x, y: x + y is applied to each pair of elements in the list, and the result is used as the input for the next iteration.