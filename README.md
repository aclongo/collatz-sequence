# collatz-sequence
This is my solution for the assignment at the end of Chapter 3 in <a href="https://automatetheboringstuff.com/">"Automate the Boring Stuff with Python"</a> - a simple program for executing the collatz sequence. If you don't know what the collatz sequence is, check out its <a href="https://en.wikipedia.org/wiki/Collatz_conjecture">Wikipedia entry</a>.

<p>The program allows the user to enter any postive number.<br>
If the input is valid (see below), it is converted into an integer and passed into the collatz function.<br>
The collatz function checks if the current integer is even or odd:<br>
<ul><li>if it is odd, it gets multiplied by 3 and then 1 is added</li>
<li>if it is even, it gets divided by 2 with floor division to prevent a floating number</li></ul>
When the integer reaches 1, the function ends and returns to the main loop.<br>
At this point the user can decide to collatz another number or end the program.</p>

### Input Validation
Prevents the following situations:
 <ul>
  <li>a string or symbol being entered</li>
  <li>a negative number being entered</li>
</ul>
