
# Project 4: Reinforcement Learning

## Train a Smartcab How to Drive

----

### Implement a Basic Driving Agent

-

__QUESTION:__ Observe what you see with the agent's behaviour as it takes random actions. Does the SmartCab eventually make it to the destination? Are there any other interesting observations to note?


__Answer:__

The current agent randomly takes actions (from a set of 4) with total disregard of its environment. Since the environment assigns a penalty to each negative action, such as going forward on a red light or when other cars are coming, the current learner keeps getting penalized and is likely to never reach the destination.

From this we can infer that our smart(er) agent has to take into account its state and the waypoints within each step of the episode. By following these updated rules, the agent can avoid incurring negative rewards and arrive the destination in a more direct / intelligent way.


----


### Inform the Driving Agent

-

__QUESTION:__ What states have you identified that are appropriate for modelling the Smartcab and environment? Why do you believe each of these states to be appropriate for this problem?


__Answer:__

In the current environment, the givens which we can use to determine the state are the following:

- The `next_waypoint`: a string denoting the direction of the destination
- The traffic `light`
- The other cars, including `oncoming` traffic as well as from the `left` and `right`

This implementation of the smart agent will build a state from a subset of that the information above. Namely, `next_waypoint` for directions, `light` for traffic light signal and `right` (or `left`) for sideway traffic, and `deadline`.


_Note:_ This implementation chooses to ignore either `left` or `right` because the currently traffic grid system being simulated only allows traffic in one of those directions at a time. Other cars going the other direction would cause an accident or a path change by one of the cars.

Also, we choose to leave out the `deadline` from our state since our current learner doesn't react to the deadline in any way. If our environment allowed the learner to do actions such as drive faster when deadline is getting closer to 0 or perhaps an extra reward for maximizing the time remaining in a trip, only then would it effect the outcome and we would include it in our state.


__OPTIONAL:__ How many states in total exist for the smartcab in this environment? Does this number seem reasonable given that the goal of Q-Learning is to learn and make informed decisions about each state? Why or why not?


...