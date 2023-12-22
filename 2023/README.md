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
    * [Watch](https://www.youtube.com/watch?v=R8qGPFRksCY) Neil Thistlethwaite solve the puzzle.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/1883ibu/2023_day_1_solutions/)
    * The visualisations seemed to have started earlier this year:
        * A neat little [terminal visualisation](https://www.reddit.com/r/adventofcode/comments/1887jd2/2023_day_1_part_2_terminal_visualization/)
        * One that shows the [movements](https://www.reddit.com/r/adventofcode/comments/1885scv/2023_day_1_hither_and_yonder/) through the lines!
        * Someone built a new [website](https://www.reddit.com/r/adventofcode/comments/18396dj/2023_day_0_inspired_by_another_reddit_post_i_also/) for demonstrating their results in the style of Advent of Code.
        * A neat little [Browser Extension](https://www.reddit.com/r/adventofcode/comments/17s0lq5/advent_of_code_charts_browser_extension_to/) that let's you see your private leaderboard in a slightly more interesting way.
  * [Day 2 - Cube Conundrum](./day_02/README.md). Fairly simple string manipulation (probably should have used a regex) and a little bit of maths checking.
    * [Watch](https://www.youtube.com/watch?v=IWCc11nh2QQ) Jonathan Paulson solve it.
    * [Watch](https://www.youtube.com/watch?v=pILyGb8NznI) William Y. Feng explain the problem.
    * [Watch](https://www.youtube.com/watch?v=zq4ckL36kqk) Neil Thistlethwaite solve the puzzle.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/188w447/2023_day_2_solutions/)
    * Visualisations:
        * [Plot of the data](https://www.reddit.com/r/adventofcode/comments/189mh3w/2023_day_2_what_if_redgreenblue_were_xyz_and_i/) by x, y, z instead of colour.
        * [Video of the colours](https://www.reddit.com/r/adventofcode/comments/1890hhm/2023_day_2_part_2python_terminal_visualization/) as you process them.
  * [Day 3 - Gear Ratios](./day_03/README.md). That was a slightly awkward one, needing you to use a grid data structure to calculate.
    * [Watch](https://www.youtube.com/watch?v=Cz528600v-M) Jonathan Paulson solve it.
    * [Watch](https://www.youtube.com/watch?v=6t1dR_-U_zE) William Y. Feng explain the problem.
    * [Watch](https://www.youtube.com/watch?v=ttxnfIpzZMU) Neil Thistlethwaite solve the puzzle.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/189m3qw/2023_day_3_solutions/)
    * Visualisations:
        * A colour coded [schematic](https://www.reddit.com/r/adventofcode/comments/189o4dj/2023_day_3_color_coded_schematic/) of the puzzle.
        * A [terminal visualisation](https://www.reddit.com/r/adventofcode/comments/189qda4/2023_day_3python_terminal_visualization/).
        * A [console visualisation](https://www.reddit.com/r/adventofcode/comments/189sgvx/2023_day_3_console_visualization/)
  * [Day 4 - Scratchcards](./day_04/README.md). Part 1 was a simple points counter, but part 2 was slightly trickier with you having to manipulate 2 different sets of data at the same time (although there might have been better ways of achieving the result.)
    * [Watch](https://www.youtube.com/watch?v=tXnPMSSQgCU) Jonathan Paulson solve it.
    * [Watch](https://www.youtube.com/watch?v=QpPsyMEYAV8) William Y. Feng explain the problem.
    * [Watch](https://www.youtube.com/watch?v=bKuWlocS95Q) Neil Thistlethwaite solve the puzzle.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/18actmy/2023_day_4_solutions/)
    * Visualisations:
        * Neat little [punch card](https://www.reddit.com/r/adventofcode/comments/18ap0qx/2023_day_4_part_2_pygame_punchcard_lotto/) viz.
        * A [terminal](https://www.reddit.com/r/adventofcode/comments/18arb9o/2023_day_04_both_parts_terminalbased_visualization/) viz.
  * [Day 5 - If You Give A Seed A Fertilizer](./day_05/README.md). Ugh. I thought I'd nailed the secret sauce in part 1 by not storing all of the data and just using lookups, turns out I needed to hold all of the sub-lookups too to get the second part to work in any reasonable length of time.
    * [Watch](https://www.youtube.com/watch?v=iqTopXV13LE) Jonathan Paulson solve it.
    * [Watch](https://www.youtube.com/watch?v=_RpZrD3CaDc) William Y. Feng explain the problem.
    * [Watch](https://www.youtube.com/watch?v=OjWhoZ3Icrs) Neil Thistlethwaite solve the puzzle.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/18b4b0r/2023_day_5_solutions/)
    * Visualisations:
        * A Sankey like visualisation of [all of the mappings](https://www.reddit.com/r/adventofcode/comments/18b82w0/2023_day_5_part_2_visualizing_all_the_mapping/).
        * Someone put together a [Python notebook](https://colab.research.google.com/github/derailed-dash/Advent-of-Code/blob/master/src/AoC_2023/Dazbo's_Advent_of_Code_2023.ipynb), and a [nice representation](https://www.reddit.com/r/adventofcode/comments/18bq77i/2023_day_5_part_2_walkthrough_and_a_picture_to/) of the problem space.
  * [Day 6 - Wait For It](./day_06/README.md). Fairly straightforward today. I did think it was going to be a combination optimisation problem, but it was much simpler than that.
    * [Watch](https://www.youtube.com/watch?v=R_tud5SLROs) Jonathan Paulson solve it.
    * [Watch](https://www.youtube.com/watch?v=Q89EpotUuzk) William Y. Feng explain the problem.
    * [Watch](https://www.youtube.com/watch?v=1m6XYKEX_3E) Neil Thistlethwaite solve the puzzle.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/18bwe6t/2023_day_6_solutions/)
  * [Day 7 - Camel Cards](./day_07/README.md). Grouped the hands into their types first, and then sorted the groups individually (bubble sort). Part 2 was straightforward, but I completely forgot about having all Jokers originally, and missed the fact that J < 2 and not actually 2!
    * [Watch](https://www.youtube.com/watch?v=22IrAlrWqu4) Jonathan Paulson solve it.
    * [Watch](https://www.youtube.com/watch?v=DUzKm0n6HgY) William Y. Feng explain the problem.
    * [Watch](https://www.youtube.com/watch?v=YU3fI5ZPyr0) Neil Thistlethwaite solve the puzzle.
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
    * [Watch](https://www.youtube.com/watch?v=AIUNsCpI-hc) Neil Thistlethwaite solve the puzzle.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/18e5ytd/2023_day_9_solutions/)
    * Visualisations:
        * Not specific to this day, but [this](https://www.reddit.com/r/adventofcode/comments/18dzc8t/aoc_2023_challenges_have_felt_oddly_outofplace/) graph shows the completions of p2 v p2 across the years by day (so far).
  * [Day 10 - Pipe Maze](./day_10/README.md). OMG what an absolute pig of a challenge. Part 1 was ok, just a simple depth first search with multiple parallel searches that you need to stop when you've explored the cell before. Part 2 was just a gigantic pain in the ass. Essentially you find the loop then you [flood fill](https://gamedev.stackexchange.com/questions/141460/how-can-i-fill-the-interior-of-a-closed-loop-on-a-tile-map) the resultant 'map' to find all of the enclosed tiles. Except that there are non-visual gaps in the tile walls where the flood also needs to fill. So you need to stretch your map to allow the flood to enter those bits as well. No wonder my code for this puzzle is such a mess.
    * [Watch](https://www.youtube.com/watch?v=M6cy6zkNGRw) Jonathan Paulson solve it.
    * [Watch](https://www.youtube.com/watch?v=zhmzPQwgPg0) William Y. Feng explain the problem.
    * [Watch](https://www.youtube.com/watch?v=JKKh_TMrUtA) Neil Thistlethwaite solve the puzzle.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/18evyu9/2023_day_10_solutions/)
    * Visualisations
        * [Every](https://www.reddit.com/r/adventofcode/comments/18eyms2/2023_day_10_part_2_finding_the_interior_space/) [man](https://www.reddit.com/r/adventofcode/comments/18eyv9b/2023_day_10_part_2_almost_looks_like_a_star/) and his [dog](https://www.reddit.com/r/adventofcode/comments/18f0l5q/2023_day_10_part_2_visualization_of_my_area/) has a [visualisation](https://www.reddit.com/r/adventofcode/comments/18f0z0o/2023_day_10_animating_my_algorithms_to_solve_both/) for [todays](https://www.reddit.com/r/adventofcode/comments/18f3asf/2023_day_10pygame_pixel_perfect_pipes/) [puzzle](https://www.reddit.com/r/adventofcode/comments/18f3diq/2023_day_10_pipe_loop_with_curve_parameter/).
  * [Day 11 - Cosmic Expansion](./day_11/README.md). Part 1 was simple enough and despite the examples using a diagonal line it was possible to use the [Manhatten Distance](https://en.wikipedia.org/wiki/Taxicab_geometry) to find the distance between the points. Part 2 was a bit trickier because you couldn't add the distances 'visually' only virtually to solve the problem in any meaningful time. However, you knew where the empty rows and columns were, so it's just a little bit of math that's required.
    * [Watch](https://www.youtube.com/watch?v=tia99l_AcFM) Jonathan Paulson solve it.
    * [Watch](https://www.youtube.com/watch?v=dBqz6Iv9IB8) William Y. Feng explain the problem.
    * [Watch](https://www.youtube.com/watch?v=WST9IEwy-ag) Neil Thistlethwaite solve the puzzle.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/18fmrjk/2023_day_11_solutions/)
  * [Day 12 - Hot Springs](./day_12/README.md). A lot of cominations to try and calculate in this one! needed to break out an LRU cache so calculations didn't need to be redone all of the time. Combine that with some good old recursion and you end up with a working mess.
    * [Watch](https://www.youtube.com/watch?v=xTGkP2GNmbQ) Jonathan Paulson solve it.
    * [Watch](https://www.youtube.com/watch?v=veJvlIMjv94) William Y. Feng explain the problem.
    * [Watch](https://www.youtube.com/watch?v=W6qUJOl4avU) Neil Thistlethwaite solve the puzzle.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/18ge41g/2023_day_12_solutions/)
    * Visualisations:
        * A neat little [terminal](https://www.youtube.com/watch?v=ZO84hyTS2DA) view.
        * Maybe a helpful [view](https://www.reddit.com/r/adventofcode/comments/18hbjdi/2023_day_12_part_2_this_image_helped_a_few_people/) of the problem?
  * [Day 13 - Point of Incidence](./day_13/README.md). Bit of a head scratcher at first, but to make the coding simpler a 90 degree rotation can be done to allow the horizontal and vertical check to use the same simple code. Part 2 was ok once - "just" work out the row where 1 change would cause the line of reflection.
    * [Watch](https://www.youtube.com/watch?v=KObhCimyl2I) Jonathan Paulson solve it.
    * [Watch](https://www.youtube.com/watch?v=Jzp8INWz5Z0) William Y. Feng explain the problem.
    * [Watch](https://www.youtube.com/watch?v=S0Ek_0zonsQ) Neil Thistlethwaite solve the puzzle.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/18h940b/2023_day_13_solutions/)
  * [Day 14 - Parabolic Reflector Dish](./day_14/README.md). Part 1 was fairly straight forward, just a bit of 'animation'!. For part 2 though you needed to understand that (much like day 8) that there were cycles to the pattern. Then use that and the length of the cycle to work out which part of the cycle the system would be in after 1,000,000,000 iterations.
    * [Watch](https://www.youtube.com/watch?v=4Ms3SN0lpxE) Jonathan Paulson solve it.
    * [Watch](https://www.youtube.com/watch?v=M9SPYhWgWbM) William Y. Feng explain the problem.
    * [Watch](https://www.youtube.com/watch?v=i1CjQiUX2ls) Neil Thistlethwaite solve the puzzle.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/18i0xtn/2023_day_14_solutions/)
  * [Day 15 - Lens Library](./day_15/README.md). After a couple of days of difficult puzzles, a bit of an easier one! Part 1 was a straightforward calculation. Part 2 was an extension of this to include the use of stacks and hashmaps. Only intuition here was that a lens would only appear in a  single box (due to the hash) so I didn't have to mess around with a sub object type within the stack and could keep the lens' focal length in a separate hashmap.
    * [Watch](https://www.youtube.com/watch?v=xcVwTpeMEMM) Jonathan Paulson solve it.
    * [Watch](https://www.youtube.com/watch?v=zwK_Nw0GpKA) William Y. Feng explain the problem.
    * [Watch](https://www.youtube.com/watch?v=Z-1bQtiY8iM) Neil Thistlethwaite solve the puzzle.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/18isayp/2023_day_15_solutions/)
  * [Day 16 - The Floor Will Be Lava](./day_16/README.md)
    * [Watch](https://www.youtube.com/watch?v=RulV5PWHBmw) Jonathan Paulson solve it.
    * [Watch](https://www.youtube.com/watch?v=UWVhYNnTe1w) Neil Thistlethwaite solve the puzzle.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/18jjpfk/2023_day_16_solutions/)
  * [Day 17 - Clumsy Crucible](./day_17/README.md)
    * [Watch](https://www.youtube.com/watch?v=jcZw1jRkUDE) Jonathan Paulson solve it.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/18k9ne5/2023_day_17_solutions/)
    * Visualisations
        * Godot [visualisation](https://www.reddit.com/r/adventofcode/comments/18l0oa4/2023_day_17_part_1_godot_3d_visualization_of_my/).
  * [Day 18 - Lavaduct Lagoon](./day_18/README.md)
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/18l0qtr/2023_day_18_solutions/)
    * Visualisations:
        * A [trench](https://www.reddit.com/r/adventofcode/comments/18l58ce/2023_day_18_part_1_pygame_trench_calculus/) visualisation.
        * A simple [static](https://www.reddit.com/r/adventofcode/comments/18l5ju8/2023_day_18_part_1_maybe_not_that_interesting_but/) visualisation.
        * Another [video](https://www.reddit.com/r/adventofcode/comments/18l63dc/2023_day_18_calculating_a_rectangular_curve_area/).
        * Lava [fill](https://www.reddit.com/r/adventofcode/comments/18lazoq/2023_day_18_part_1_filling_the_lava_lagoon/).
  * [Day 19 - Aplenty](./day_19/README.md)
    * [Watch](https://www.youtube.com/watch?v=vQWe35EEHbI) Jonathan Paulson solve it.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/18ltr8m/2023_day_19_solutions/)
    * Visualisations:
        * Showing the [graph](https://www.reddit.com/r/adventofcode/comments/18lvl0s/2023_day_19_visualization_of_the_workflows/).
        * Showing the graph as a [Sankey](https://www.reddit.com/r/adventofcode/comments/18lyvuv/2023_day_19_part_2_sankey_diagrams_are_cool/).
        * All [possible parts](https://www.reddit.com/r/adventofcode/comments/18m1uxq/2023_day_19_part_2_looking_for_all_possible_parts/).
  * [Day 20 - Pulse Propagation](./day_20/README.md)
    * [Watch](https://www.youtube.com/watch?v=3STpz-M-wiw) Jonathan Paulson solve it.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/18mmfxb/2023_day_20_solutions/)
  * [Day 21 - Step Counter](./day_21/README.md)
    * [Watch](https://www.youtube.com/watch?v=C2dmxCGGH1s) Jonathan Paulson solve it.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/18nevo3/2023_day_21_solutions/)
  * [Day 22 - Sand Slabs](./day_22/README.md)
    * [Watch](https://www.youtube.com/watch?v=N1uYqpCTWJQ) Jonathan Paulson solve it.
    * [Reddit discussion page](https://www.reddit.com/r/adventofcode/comments/18o7014/2023_day_22_solutions/)
  * [Day 23 - xxx](./day_23/README.md)
  * [Day 24 - xxx](./day_24/README.md)
  * [Day 25 - xxx](./day_25/README.md)
