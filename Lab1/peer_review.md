<h1>Overview</h1>

<p>
The algorith(s) you used are A* and BFS search and you made a comparison between the outcomes of the two. The problem has been solved for N = 5, 10, 20 and you tried also N = 100. The code, provided by the prof, isn't very understable (not your fault) but I'd have appreciated some comments if I want to be picky. 
</p>


<h1>Performance analysis</h1>

<p>
I ran the script with several values of N and got the following values:
    A*: N = 5 -> 5 elements in 61 visited nodes ( optimal :) )
        N = 10 -> 10 elements in 3149 visited nodes ( optimal :) )
        N = 20 -> 23 elements in 479,873 visited nodes ( must be the best possible, I got the same :) )
        N >= 30 -> eternity and RAM maxed out ( :( )

    BFS: N = 5 -> 5 elements and 3,454 visited nodes ( optimal but much slower  :| )
         N = 10 -> 13 elements and 197,080 visited nodes ( not optimal and very slow :( )
         N = 20 -> 29 elements and 2,172,545 visited nodes ( not optimal and very slow :( )
         N >= 30 -> eternity and RAM maxed out ( :( )

    It's clear that A* is a better choice, but I think it's not ideal for this problem because of the extreme amount of memory needed, for N > 20. Anyway I appreciate you tried more than one solution!
</p>


<h1>What you can improve</h1>

<p>
I noticed the algorith uses a massive amount of RAM (maxing out my 16GB machine and even using virtual memory of hard drive) with N >= 30. I also had that issue that was caused by listing of all the combinations possible instead of leaving them as an optimized iterator. In your case I think it's caused by keeping in memory all the possibile states the algorithm generates!
In the search function I found annoying the log of frontier node addition (who cares!), it is potentially capable of flooding the output, and it did! So I just commented that line. 
I also have preferred if you had made some sort of functions called (A* and BFS) instead of commenting some parts of the code in order to switch between the former or the latter.
Besides, given the amount of time needed to solve the problem (with N > 20), I would have preferred you to implement some sort of for loop with N values in order to run it and potentially go afk instead to continously check it and change the N value after a test is done.


<h1>Comparison with my solution</h1>

<p>
My solution uses an approach based on full exploration of the solution space and computes all the possible combinations, instead of using tree-search algorithims like you did.
In terms of performance, I ran both tests and mine turned out to be better and capable of solving the problem till N = 40 in a few minutes, without maxing out system memory. I think for very small values of N, like 5, however, A* performed better. Honestly, I expected mine to be worse because it explores the whole solution space, but perhaps it is better because of the pruning.


<h1>Conclusions</h1>

<p>
I think yours isn't the fittest algorithm for this kind of problem because these algorithms are known to be computing time "friendly" (not that much) but memory unfriendly unless you have a workstation.
For next assignment I recommend you to make the code more modular and put some more comments, I'm not judging you for the memory issues, I almost randomly fell into windows task manager and noticed it :)
