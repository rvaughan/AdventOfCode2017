# Advent Of Code 2023

Code and solutions for [Advent of Code 2023](http://adventofcode.com/2023).
Just maybe not very good ones :)

The code relating to each day of advent is held in its own folder within this
repository. Note that the inputs for each of the days may be unique to my
user, and therefore the inputs to each of the days may need to be tweaked to
run for your input. However, the code should hopefully be valid for your
input.

Each day has two parts to it. Generally the 2nd part is a variation of the 1st
part. I've broken the solutions for each part out into their own individual
python files just for clarity.

**Note:** The code may not be particularly pythonic, or even always that legible.
I may, dependant on time, go back and tidy the code up later. However, I'm
using the competition as a distraction from normal coding duties, so don't
hold your breath.

## Leaderboard

I'm reusing my private [leaderboard](leaderboard.json) from previous years - even managed to get some new recruits to play this year!

## Puzzles

  * [Day 1 - Trebuchet?!](./day_01/README.md). Solved part 1 with a fairly simple digit matcher, and part 2 using a quick and dirty string look ahead. Inefficient (probably) but works on this kind of length of string well enough.
    * [Watch](https://www.youtube.com/watch?v=rnidYOt9m2o) Jonathan Paulson solve it.
    * [Watch](https://www.youtube.com/watch?v=T_us6npCcxw) William Y. Feng explain the problem.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/1883ibu/2023_day_1_solutions/)
    * The visualisations seemed to have started earlier this year:
        * A neat little [terminal visualisation](https://www.reddit.com/r/adventofcode/comments/1887jd2/2023_day_1_part_2_terminal_visualization/)
        * One that shows the [movements](https://www.reddit.com/r/adventofcode/comments/1885scv/2023_day_1_hither_and_yonder/) through the lines!
        * Someone built a new [website](https://www.reddit.com/r/adventofcode/comments/18396dj/2023_day_0_inspired_by_another_reddit_post_i_also/) for demonstrating their results in the style of Advent of Code.
        * A neat little [Browser Extension](https://www.reddit.com/r/adventofcode/comments/17s0lq5/advent_of_code_charts_browser_extension_to/) that let's you see your private leaderboard in a slightly more interesting way.
  * [Day 2 - Cube Conundrum](./day_02/README.md). Fairly simple string manipulation (probably should have used a regex) and a little bit of maths checking.
    * [Watch](https://www.youtube.com/watch?v=IWCc11nh2QQ) Jonathan Paulson solve it.
    * [Watch](https://www.youtube.com/watch?v=pILyGb8NznI) William Y. Feng explain the problem.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/188w447/2023_day_2_solutions/)
    * Visualisations:
        * [Plot of the data](https://www.reddit.com/r/adventofcode/comments/189mh3w/2023_day_2_what_if_redgreenblue_were_xyz_and_i/) by x, y, z instead of colour.
        * [Video of the colours](https://www.reddit.com/r/adventofcode/comments/1890hhm/2023_day_2_part_2python_terminal_visualization/) as you process them.
  * [Day 3 - Gear Ratios](./day_03/README.md). That was a slightly awkward one, needing you to use a grid data structure to calculate.
    * [Watch](https://www.youtube.com/watch?v=Cz528600v-M) Jonathan Paulson solve it.
    * [Watch](https://www.youtube.com/watch?v=6t1dR_-U_zE) William Y. Feng explain the problem.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/189m3qw/2023_day_3_solutions/)
    * Visualisations:
        * A colour coded [schematic](https://www.reddit.com/r/adventofcode/comments/189o4dj/2023_day_3_color_coded_schematic/) of the puzzle.
        * A [terminal visualisation](https://www.reddit.com/r/adventofcode/comments/189qda4/2023_day_3python_terminal_visualization/).
        * A [console visualisation](https://www.reddit.com/r/adventofcode/comments/189sgvx/2023_day_3_console_visualization/)
  * [Day 4 - Scratchcards](./day_04/README.md). Part 1 was a simple points counter, but part 2 was slightly trickier with you having to manipulate 2 different sets of data at the same time (although there might have been better ways of achieving the result.)
    * [Watch](https://www.youtube.com/watch?v=tXnPMSSQgCU) Jonathan Paulson solve it.
    * [Watch](https://www.youtube.com/watch?v=QpPsyMEYAV8) William Y. Feng explain the problem.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/18actmy/2023_day_4_solutions/)
    * Visualisations:
        * Neat little [punch card](https://www.reddit.com/r/adventofcode/comments/18ap0qx/2023_day_4_part_2_pygame_punchcard_lotto/) viz.
        * A [terminal](https://www.reddit.com/r/adventofcode/comments/18arb9o/2023_day_04_both_parts_terminalbased_visualization/) viz.
  * [Day 5 - If You Give A Seed A Fertilizer](./day_05/README.md). Ugh. I thought I'd nailed the secret sauce in part 1 by not storing all of the data and just using lookups, turns out I needed to hold all of the sub-lookups too to get the second part to work in any reasonable length of time.
    * [Watch](https://www.youtube.com/watch?v=iqTopXV13LE) Jonathan Paulson solve it.
    * [Watch](https://www.youtube.com/watch?v=_RpZrD3CaDc) William Y. Feng explain the problem.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/18b4b0r/2023_day_5_solutions/)
    * Visualisations:
        * A Sankey like visualisation of [all of the mappings](https://www.reddit.com/r/adventofcode/comments/18b82w0/2023_day_5_part_2_visualizing_all_the_mapping/).
        * Someone put together a [Python notebook](https://colab.research.google.com/github/derailed-dash/Advent-of-Code/blob/master/src/AoC_2023/Dazbo's_Advent_of_Code_2023.ipynb), and a [nice representation](https://www.reddit.com/r/adventofcode/comments/18bq77i/2023_day_5_part_2_walkthrough_and_a_picture_to/) of the problem space.
  * [Day 6 - Wait For It](./day_06/README.md). Fairly straightforward today. I did think it was going to be a combination optimisation problem, but it was much simpler than that.
    * [Watch](https://www.youtube.com/watch?v=R_tud5SLROs) Jonathan Paulson solve it.
    * [Watch](https://www.youtube.com/watch?v=Q89EpotUuzk) William Y. Feng explain the problem.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/18bwe6t/2023_day_6_solutions/)
  * [Day 7 - Camel Cards](./day_07/README.md). Grouped the hands into their types first, and then sorted the groups individually (bubble sort). Part 2 was straightforward, but I completely forgot about having all Jokers originally, and missed the fact that J < 2 and not actually 2!
    * [Watch](https://www.youtube.com/watch?v=22IrAlrWqu4) Jonathan Paulson solve it.
    * [Watch](https://www.youtube.com/watch?v=DUzKm0n6HgY) William Y. Feng explain the problem.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/18cnzbm/2023_day_7_solutions/)
  * [Day 8 - Haunted Wasteland](./day_08/README.md). Part 1 was eeasy enough. Part 2 started off doing brute force, but that's stupid. The ghost patterns were repetetive, so [Least Common Multiplier](https://www.educative.io/answers/what-is-the-mathlcm-function-in-python) (LCM) seemed the way to go.
    * [Watch](https://www.youtube.com/watch?v=07AMCU8Xyg4) Jonathan Paulson solve it.
    * [Watch](https://www.youtube.com/watch?v=xH9LFkYRTD0) William Y. Feng explain the problem.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/18df7px/2023_day_8_solutions/)
    * Visualisations:
        * This is a brilliant rendition of what is going on using [card tables](https://www.reddit.com/r/adventofcode/comments/18dprr1/2023_day_8_part_2pygame_counting_camel_cycles/).
        * Visualising the input as a [planetary graph](https://www.reddit.com/r/adventofcode/comments/18e2cyt/2023_day_08_part_2_a_planetarysystem_like_graph/)
  * [Day 9 - Mirage Maintenance](./day_09/README.md). Part 1 was easy enough, just a bit of array manipulation. I think I over complicated it in the expectation that part 2 was going to be more complicated than it turned out to be. Part 2 was more complicated then that it needed to be. Booo!
    * [Watch](https://www.youtube.com/watch?v=bOdSvEXoy5Q) Jonathan Paulson solve it.
    * [Watch](https://www.youtube.com/watch?v=Kr_6NquFbxE) William Y. Feng explain the problem.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/18e5ytd/2023_day_9_solutions/)
    * Visualisations:
        * Not specific to this day, but [this](https://www.reddit.com/r/adventofcode/comments/18dzc8t/aoc_2023_challenges_have_felt_oddly_outofplace/) graph shows the completions of p2 v p2 across the years by day (so far).
  * [Day 10 - Pipe Maze](./day_10/README.md). OMG what an absolute pig of a challenge. Part 1 was ok, just a simple depth first search with multiple parallel searches that you need to stop when you've explored the cell before. Part 2 was just a gigantic pain in the ass. Essentially you find the loop then you [flood fill](https://gamedev.stackexchange.com/questions/141460/how-can-i-fill-the-interior-of-a-closed-loop-on-a-tile-map) the resultant 'map' to find all of the enclosed tiles. Except that there are non-visual gaps in the tile walls where the flood also needs to fill. So you need to stretch your map to allow the flood to enter those bits as well. No wonder my code for this puzzle is such a mess.
    * [Watch](https://www.youtube.com/watch?v=M6cy6zkNGRw) Jonathan Paulson solve it.
    * [Watch](https://www.youtube.com/watch?v=zhmzPQwgPg0) William Y. Feng explain the problem.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/18evyu9/2023_day_10_solutions/)
    * Visualisations
        * [Every](https://www.reddit.com/r/adventofcode/comments/18eyms2/2023_day_10_part_2_finding_the_interior_space/) [man](https://www.reddit.com/r/adventofcode/comments/18eyv9b/2023_day_10_part_2_almost_looks_like_a_star/) and his [dog](https://www.reddit.com/r/adventofcode/comments/18f0l5q/2023_day_10_part_2_visualization_of_my_area/) has a [visualisation](https://www.reddit.com/r/adventofcode/comments/18f0z0o/2023_day_10_animating_my_algorithms_to_solve_both/) for [todays](https://www.reddit.com/r/adventofcode/comments/18f3asf/2023_day_10pygame_pixel_perfect_pipes/) [puzzle](https://www.reddit.com/r/adventofcode/comments/18f3diq/2023_day_10_pipe_loop_with_curve_parameter/).
  * [Day 11 - xxx](./day_11/README.md)
  * [Day 12 - xxx](./day_12/README.md)
  * [Day 13 - xxx](./day_13/README.md)
  * [Day 14 - xxx](./day_14/README.md)
  * [Day 15 - xxx](./day_15/README.md)
  * [Day 16 - xxx](./day_16/README.md)
  * [Day 17 - xxx](./day_17/README.md)
  * [Day 18 - xxx](./day_18/README.md)
  * [Day 19 - xxx](./day_19/README.md)
  * [Day 20 - xxx](./day_20/README.md)
  * [Day 21 - xxx](./day_21/README.md)
  * [Day 22 - xxx](./day_22/README.md)
  * [Day 23 - xxx](./day_23/README.md)
  * [Day 24 - xxx](./day_24/README.md)
  * [Day 25 - xxx](./day_25/README.md)
